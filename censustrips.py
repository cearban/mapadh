"""
   we don`t need no (geo)django!
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, VARCHAR
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class OutputArea(Base):
    """
    A representation of a 2021 census OutputArea using the harmonized
    UK census data created by the GeoDS folks
    """
    __tablename__ = 'uk_oa_2021_uk008'
    __table_args__ = {'schema': 'censustrips'}
    id = Column(Numeric, primary_key=True)
    oa_code = Column(VARCHAR())
    all_persons = Column(Numeric)
    male = Column(Numeric)
    female = Column(Numeric)
    geom = Column(Geometry(geometry_type='MULTIPOLYGON', srid=27700))


class RailwayStation(Base):
    """
    A representation of a railway station
    """
    __tablename__ = 'railway_stations'
    __table_args__ = {'schema': 'censustrips'}
    gid = Column(Integer, primary_key=True)
    code = Column(Integer)
    identifier = Column(VARCHAR)
    name = Column(VARCHAR(length=70))
    geom = Column(Geometry(geometry_type='POINT', srid=27700))


class Railway(Base):
    """
    A representation of a railway
    """
    __tablename__ = 'railways_lines'
    __table_args__ = {'schema': 'censustrips'}
    gid = Column(Integer, primary_key=True)
    code = Column(Integer)
    identifier = Column(VARCHAR(length=13))
    name = Column(VARCHAR(length=70))
    geom = Column(Geometry(geometry_type='MULTILINESTRING', srid=27700))


class CensusTripsRoute(Base):
    """
    A representation of a railway trip route between stations
    """
    __tablename__ = 'censustrips_route'
    __table_args__ = {'schema': 'censustrips'}
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer)
    seq_id = Column(Integer)
    station_id = Column(Integer, ForeignKey('censustrips.railway_stations.gid'))
    station = relationship("RailwayStation")


def list_output_areas(session):
    query = session.query(OutputArea).order_by(OutputArea.code)
    for oa in query:
        print(oa.code)


def list_stations(session):
    query = session.query(RailwayStation).order_by(RailwayStation.name)
    for stn in query:
        print(stn.name)


# TODO: this is just a test to check we are getting stuff back for the 2021 OA data. We will want to handle the difft
#  census years data in the same function by passing in a year parameter

# TODO: based on the names of the first and last station we can create a name for the route

# TODO: rather than hardcoding which attribute is returned, make this user-defined

# TODO: as per what was done in "lives on the line" noted in the pdf under docs, search for OAs
#  within some distance e.g. 200m of each station and average the stat etc

def fetch_buffered_population_along_route(route_id, pg_conn_str, buffer_distance=200):
    """
    do what is done in docs/live_on_the_line_article.pdf and draw a 200m buffer around each station point and find
    within that 200m buffer all overlapping OAs. If only one OA overlaps then use the single value associated with
    that OA otherwise take an average from all of the overlapping OAs.
    :param route_id:
    :param pg_conn_str:
    :buffer_distance:
    :return:
    """
    d = {'route_name': {'title': None}}
    engine = create_engine(pg_conn_str)
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch the stops for this route_id
    stops = session.query(CensusTripsRoute).filter_by(route_id=route_id)
    stop_id = 1

    first_station_name, last_station_name = None, None

    # for each stop in the route
    for s in stops:
        try:
            stn = session.query(RailwayStation).filter_by(name=s.station.name).one()

            # buffer the station point by the buffer_distance and find all of the overlapping OAs
            overlapping_output_areas = session.query(OutputArea).filter(
                OutputArea.geom.ST_Overlaps(stn.geom.ST_Buffer(buffer_distance))
            )

            # get the count of OAs that overlap with the buffer region
            count_of_overlapping_oas = overlapping_output_areas.count()

            # calculate the average value of the census variable across this set of overlapping OAs
            all_persons_total = 0
            for oa in overlapping_output_areas:
                all_persons_total += oa.all_persons
            all_persons_avg = all_persons_total / overlapping_output_areas.count()

            # instead of returning the OA code, return the count of OAs that overlap
            d[str(stop_id)] = {
                'station_name': s.station.name, #this works because of the relationship btwn CensusTripsRoute obj and RailwayStation obj
                'oa_code': 'Number of overlapping Output Areas is {0}'.format(str(count_of_overlapping_oas)),
                'oa_all_persons': int(all_persons_avg), #sqlalchemy return values as Decimal('92') etc and then jsonify in app.py complains...
            }

            if stop_id == 1:
                first_station_name = s.station.name
            else:
                last_station_name = s.station.name

            stop_id += 1
        except sqlalchemy.orm.exc.NoResultFound:
            print("Warning! {} is not a station, skipped".format(s.station.name))

    # set the name of the route - setting
    d['route_name']['title'] = 'Population in the 2021 OA taking a rail journey from {0} to {1}'.format(first_station_name, last_station_name)

    return d


def fetch_population_along_route(route_id, pg_conn_str):
    # set the first element of the dict that will be returned to the Route Name with a placeholder value that later
    # we will populate
    d = {'route_name': {'title': None}}
    engine = create_engine(pg_conn_str)
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch the stops for this route_id
    stops = session.query(CensusTripsRoute).filter_by(route_id=route_id)
    stop_id = 1

    first_station_name, last_station_name = None, None

    # for each stop in the route
    for s in stops:
        try:
            # get RailwayStation object that matches the station_name
            #
            stn = session.query(RailwayStation).filter_by(name=s.station.name).one()

            # get OutputArea whose polygon geometry contains the RailwayStation object point geometry
            # weird results happen if do an intersects, looks like it`s using MBR to do the test?
            oa = session.query(OutputArea).filter(
                OutputArea.geom.ST_Contains(stn.geom)
            ).one()
            d[str(stop_id)] = {
                'station_name': s.station.name, #this works because of the relationship btwn CensusTripsRoute obj and RailwayStation obj
                'oa_code': oa.oa_code,
                'oa_all_persons': int(oa.all_persons), #sqlalchemy return values as Decimal('92') etc and then jsonify in app.py complains...
            }
            if stop_id == 1:
                first_station_name = s.station.name
            else:
                last_station_name = s.station.name

            stop_id += 1
        except sqlalchemy.orm.exc.NoResultFound:
            print("Warning! {} is not a station, skipped".format(s.station.name))

    # set the name of the route - setting
    d['route_name']['title'] = 'Population in the 2021 OA taking a rail journey from {0} to {1}'.format(first_station_name, last_station_name)

    return d

