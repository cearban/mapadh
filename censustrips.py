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
    A representation of a census OutputArea
    """
    __tablename__ = 'gb_oa_2011'
    __table_args__ = {'schema': 'geocrud'}
    gid = Column(Integer, primary_key=True)
    oacode = Column(VARCHAR(length=9))
    popx = Column(Numeric)
    popy = Column(Numeric)
    totpop = Column(Numeric)
    totpop01 = Column(Numeric)
    totadult = Column(Numeric)
    tot16to74 = Column(Numeric)
    totemploy = Column(Numeric)
    ttwbasepop = Column(Numeric)
    hhdpop = Column(Numeric)
    commpop = Column(Numeric)
    dwelling = Column(Numeric)
    hhdspace = Column(Numeric)
    hhdocc = Column(Numeric)
    hhdempty = Column(Numeric)
    hrp16to64 = Column(Numeric)
    male = Column(Numeric)
    female = Column(Numeric)
    age0to4 = Column(Numeric)
    age5to7 = Column(Numeric)
    age8to9 = Column(Numeric)
    age10to14 = Column(Numeric)
    age15 = Column(Numeric)
    age16to17 = Column(Numeric)
    age18to19 = Column(Numeric)
    age20to24 = Column(Numeric)
    age25to29 = Column(Numeric)
    age30to44 = Column(Numeric)
    age45to59 = Column(Numeric)
    age60to64 = Column(Numeric)
    age65to74 = Column(Numeric)
    age75to84 = Column(Numeric)
    age85to89 = Column(Numeric)
    age90plus = Column(Numeric)
    single = Column(Numeric)
    married = Column(Numeric)
    samesex = Column(Numeric)
    separated = Column(Numeric)
    divorced = Column(Numeric)
    widowed = Column(Numeric)
    whitetot = Column(Numeric)
    whitebr = Column(Numeric)
    whiteoth = Column(Numeric)
    mixedeth = Column(Numeric)
    indian = Column(Numeric)
    pakistani = Column(Numeric)
    bangladesh = Column(Numeric)
    chinese = Column(Numeric)
    otherasian = Column(Numeric)
    blafrican = Column(Numeric)
    blcarib = Column(Numeric)
    blother = Column(Numeric)
    othereth = Column(Numeric)
    cobengland = Column(Numeric)
    cobwales = Column(Numeric)
    cobscot = Column(Numeric)
    cobni = Column(Numeric)
    cobroi = Column(Numeric)
    coboldeu = Column(Numeric)
    cobneweu = Column(Numeric)
    cobother = Column(Numeric)
    passnone = Column(Numeric)
    passuk = Column(Numeric)
    passroi = Column(Numeric)
    passeu = Column(Numeric)
    passnoneu = Column(Numeric)
    passafrica = Column(Numeric)
    passmea = Column(Numeric)
    passnam = Column(Numeric)
    passcam = Column(Numeric)
    passsam = Column(Numeric)
    passocean = Column(Numeric)
    catholic = Column(Numeric)
    otchrist = Column(Numeric)
    totchrist = Column(Numeric)
    buddhist = Column(Numeric)
    hindu = Column(Numeric)
    jewish = Column(Numeric)
    muslim = Column(Numeric)
    sikh = Column(Numeric)
    otrel = Column(Numeric)
    tototrel = Column(Numeric)
    noreligion = Column(Numeric)
    religionns = Column(Numeric)
    vghealth = Column(Numeric)
    ghealth = Column(Numeric)
    fairhealth = Column(Numeric)
    badhealth = Column(Numeric)
    vbadhealth = Column(Numeric)
    eaemppt = Column(Numeric)
    eaempft = Column(Numeric)
    easelfemp = Column(Numeric)
    eaunemp = Column(Numeric)
    eafutist = Column(Numeric)
    eiretired = Column(Numeric)
    eifutist = Column(Numeric)
    eihome = Column(Numeric)
    eisickdis = Column(Numeric)
    eiother = Column(Numeric)
    agricult = Column(Numeric)
    extractive = Column(Numeric)
    manufact = Column(Numeric)
    energysup = Column(Numeric)
    watersup = Column(Numeric)
    construct = Column(Numeric)
    retail = Column(Numeric)
    transport = Column(Numeric)
    accommfood = Column(Numeric)
    infocomms = Column(Numeric)
    finserv = Column(Numeric)
    propserv = Column(Numeric)
    proftech = Column(Numeric)
    administ = Column(Numeric)
    pubaddef = Column(Numeric)
    education = Column(Numeric)
    health = Column(Numeric)
    otherind = Column(Numeric)
    empandmgr = Column(Numeric)
    highprof = Column(Numeric)
    lowprof = Column(Numeric)
    intermed = Column(Numeric)
    smempseem = Column(Numeric)
    lowsuper = Column(Numeric)
    semirout = Column(Numeric)
    routine = Column(Numeric)
    neverwork = Column(Numeric)
    ltunemp = Column(Numeric)
    notclass = Column(Numeric)
    noquals = Column(Numeric)
    qual1 = Column(Numeric)
    qual2 = Column(Numeric)
    qualapp = Column(Numeric)
    qual3 = Column(Numeric)
    qual4 = Column(Numeric)
    qualother = Column(Numeric)
    stud16to17 = Column(Numeric)
    stud18plus = Column(Numeric)
    ftsemploy = Column(Numeric)
    ftsunemp = Column(Numeric)
    ftsecinact = Column(Numeric)
    ttwhome = Column(Numeric)
    ttwtrain = Column(Numeric)
    ttwtube = Column(Numeric)
    ttwbus = Column(Numeric)
    ttwmbike = Column(Numeric)
    ttwcar = Column(Numeric)
    ttwcarpass = Column(Numeric)
    ttwtaxi = Column(Numeric)
    ttwbike = Column(Numeric)
    ttwfoot = Column(Numeric)
    ttwother = Column(Numeric)
    pens1pers = Column(Numeric)
    other1pers = Column(Numeric)
    pensfamily = Column(Numeric)
    manokid = Column(Numeric)
    madepkid = Column(Numeric)
    mandepkid = Column(Numeric)
    conokid = Column(Numeric)
    codepkid = Column(Numeric)
    condepkid = Column(Numeric)
    lpdepkid = Column(Numeric)
    lpndepkid = Column(Numeric)
    othdepkid = Column(Numeric)
    allstudent = Column(Numeric)
    otherpens = Column(Numeric)
    otherhhd = Column(Numeric)
    dwunshared = Column(Numeric)
    dwshared = Column(Numeric)
    detached = Column(Numeric)
    semidetach = Column(Numeric)
    terrace = Column(Numeric)
    flatpur = Column(Numeric)
    flatconsha = Column(Numeric)
    commbuild = Column(Numeric)
    caravmob = Column(Numeric)
    ownout = Column(Numeric)
    ownmort = Column(Numeric)
    ownshare = Column(Numeric)
    soccouncil = Column(Numeric)
    socother = Column(Numeric)
    privrentl = Column(Numeric)
    privrento = Column(Numeric)
    rentfree = Column(Numeric)
    nocars = Column(Numeric)
    car1 = Column(Numeric)
    car2 = Column(Numeric)
    car3 = Column(Numeric)
    car4plus = Column(Numeric)
    pers1hhd = Column(Numeric)
    pers2hhd = Column(Numeric)
    pers3hhd = Column(Numeric)
    pers4hhd = Column(Numeric)
    pers5hhd = Column(Numeric)
    pers6hhd = Column(Numeric)
    pers7hhd = Column(Numeric)
    pers8phhd = Column(Numeric)
    abhrp = Column(Numeric)
    c1hrp = Column(Numeric)
    c2hrp = Column(Numeric)
    dehrp = Column(Numeric)
    geom = Column(Geometry(geometry_type='MULTIPOLYGON', srid=27700))


class RailwayStation(Base):
    """
    A representation of a railway station
    """
    __tablename__ = 'railway_stations'
    __table_args__ = {'schema': 'geocrud'}
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
    __table_args__ = {'schema': 'geocrud'}
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
    __table_args__ = {'schema': 'geocrud'}
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer)
    seq_id = Column(Integer)
    station_id = Column(Integer, ForeignKey('geocrud.railway_stations.gid'))
    station = relationship("RailwayStation")


def list_output_areas(session):
    query = session.query(OutputArea).order_by(OutputArea.code)
    for oa in query:
        print(oa.code)


def list_stations(session):
    query = session.query(RailwayStation).order_by(RailwayStation.name)
    for stn in query:
        print(stn.name)


def fetch_population_along_route(route_id):
    d = {}
    pg_conn_str = None  # TODO need this - put password somewhere not here!
    engine = create_engine(pg_conn_str)
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch the stops for this route_id
    stops = session.query(CensusTripsRoute).filter_by(route_id=route_id)
    stop_id = 1

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
            d[stop_id] = {
                'station_name': s.station.name, #this works because of the relationship btwn CensusTripsRoute obj and RailwayStation obj
                'oa_code': oa.oacode,
                'oa_totpop01': int(oa.totpop01), #sqlalchemy return values as Decimal('92') etc and then jsonify in app.py complains...
                'oa_totpop11': int(oa.totpop)
            }
            stop_id += 1
        except sqlalchemy.orm.exc.NoResultFound:
            print("Warning! {} is not a station, skipped".format(s.station.name))

    return d

