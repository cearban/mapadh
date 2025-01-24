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
    __table_args__ = {'schema': 'censustrips'}
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


class OutputArea21(Base):
    """
    A representation of a 2021 census OutputArea
    """
    __tablename__ = 'gb_oa_2021'
    __table_args__ = {'schema': 'censustrips'}
    id = Column(Numeric, primary_key=True)
    oa_code = Column(VARCHAR())
    oa_code_11 = Column(VARCHAR())
    change1121 = Column(VARCHAR())
    lsoa_code = Column(VARCHAR())
    totpop = Column(Numeric)
    hhd = Column(Numeric)
    pop_dens = Column(Numeric)
    dwellings = Column(Numeric)
    hhdpop = Column(Numeric)
    commpop = Column(Numeric)
    male = Column(Numeric)
    female = Column(Numeric)
    age_0_2 = Column(Numeric)
    age_3_4 = Column(Numeric)
    age_5_7 = Column(Numeric)
    age_8_9 = Column(Numeric)
    age_10_14 = Column(Numeric)
    age_15 = Column(Numeric)
    age_16_17 = Column(Numeric)
    age_18_19 = Column(Numeric)
    age_20_24 = Column(Numeric)
    age_25_29 = Column(Numeric)
    age_30_34 = Column(Numeric)
    age_35_39 = Column(Numeric)
    age_40_44 = Column(Numeric)
    age_45_49 = Column(Numeric)
    age_50_54 = Column(Numeric)
    age_55_59 = Column(Numeric)
    age_60_64 = Column(Numeric)
    age_65 = Column(Numeric)
    age_66_69 = Column(Numeric)
    age_70_74 = Column(Numeric)
    age_75_79 = Column(Numeric)
    age_80_84 = Column(Numeric)
    age_85_pl = Column(Numeric)
    divorced = Column(Numeric)
    msnotapply = Column(Numeric)
    formciv = Column(Numeric)
    civil_os = Column(Numeric)
    civil_ss = Column(Numeric)
    married_os = Column(Numeric)
    married_ss = Column(Numeric)
    single = Column(Numeric)
    sep_civ = Column(Numeric)
    sepmarried = Column(Numeric)
    survciv = Column(Numeric)
    widowed = Column(Numeric)
    aabwbang = Column(Numeric)
    aabwchin = Column(Numeric)
    aabwindia = Column(Numeric)
    aabwoth = Column(Numeric)
    aabwpak = Column(Numeric)
    bbwcaafr = Column(Numeric)
    bbwcacar = Column(Numeric)
    bbwcaoth = Column(Numeric)
    mixedeth = Column(Numeric)
    othereth = Column(Numeric)
    whitetot = Column(Numeric)
    whitebr = Column(Numeric)
    cobafrica = Column(Numeric)
    cobanocoth = Column(Numeric)
    cobbriosea = Column(Numeric)
    cobeuother = Column(Numeric)
    cobeu14 = Column(Numeric)
    cobeu2 = Column(Numeric)
    cobeu8 = Column(Numeric)
    cobnoneu = Column(Numeric)
    cobuk = Column(Numeric)
    cobmea = Column(Numeric)
    cobamca = Column(Numeric)
    rbuddhist = Column(Numeric)
    rchrist = Column(Numeric)
    rhindu = Column(Numeric)
    rjewish = Column(Numeric)
    rmuslim = Column(Numeric)
    noreligion = Column(Numeric)
    noanswer = Column(Numeric)
    otherrel = Column(Numeric)
    rsikh = Column(Numeric)
    badhealth = Column(Numeric)
    fairhealth = Column(Numeric)
    ghealth = Column(Numeric)
    vbadhealth = Column(Numeric)
    vghealth = Column(Numeric)
    eaemp = Column(Numeric)
    eaeself = Column(Numeric)
    eaunemp = Column(Numeric)
    eafutist = Column(Numeric)
    eiltsdis = Column(Numeric)
    eihfam = Column(Numeric)
    eioth = Column(Numeric)
    eiret = Column(Numeric)
    eistu = Column(Numeric)
    agricult = Column(Numeric)
    extractive = Column(Numeric)
    manufact = Column(Numeric)
    energysup = Column(Numeric)
    ind_dna = Column(Numeric)
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
    nssecdna = Column(Numeric)
    l123hmapro = Column(Numeric)
    l1011lstec = Column(Numeric)
    l12semrou = Column(Numeric)
    l13routine = Column(Numeric)
    l14nwltune = Column(Numeric)
    l15ftstu = Column(Numeric)
    l456lmapro = Column(Numeric)
    l7inter = Column(Numeric)
    l89seoacc = Column(Numeric)
    lq_appren = Column(Numeric)
    lq_na = Column(Numeric)
    lq_level1 = Column(Numeric)
    lq_level2 = Column(Numeric)
    lq_level3 = Column(Numeric)
    lq_level4 = Column(Numeric)
    lq_no = Column(Numeric)
    lq_other = Column(Numeric)
    edu_na = Column(Numeric)
    notstudent = Column(Numeric)
    student = Column(Numeric)
    multoth = Column(Numeric)
    multdepkid = Column(Numeric)
    pens1pers = Column(Numeric)
    other1pers = Column(Numeric)
    pensfamily = Column(Numeric)
    condepkid = Column(Numeric)
    conokid = Column(Numeric)
    codepkid = Column(Numeric)
    lpndepkid = Column(Numeric)
    lpdepkid = Column(Numeric)
    mandepkid = Column(Numeric)
    madepkid = Column(Numeric)
    manokid = Column(Numeric)
    singoth = Column(Numeric)
    at_mobile = Column(Numeric)
    at_detach = Column(Numeric)
    at_comm = Column(Numeric)
    at_flat = Column(Numeric)
    at_anyconv = Column(Numeric)
    at_othconv = Column(Numeric)
    at_semdet = Column(Numeric)
    at_terr = Column(Numeric)
    ten_rentfr = Column(Numeric)
    ten_ownout = Column(Numeric)
    ten_ownmort = Column(Numeric)
    ten_proth = Column(Numeric)
    ten_prllla = Column(Numeric)
    ten_so = Column(Numeric)
    ten_sroth = Column(Numeric)
    ten_srrent = Column(Numeric)
    cva_1 = Column(Numeric)
    cva_2 = Column(Numeric)
    cva_3pl = Column(Numeric)
    cva_no = Column(Numeric)
    pers1hhd = Column(Numeric)
    pers2hhd = Column(Numeric)
    pers3hhd = Column(Numeric)
    pers4hhd = Column(Numeric)
    pers5hhd = Column(Numeric)
    pers6plhhd = Column(Numeric)
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
def fetch_2021_population_along_route(route_id, pg_conn_str):
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
            oa = session.query(OutputArea21).filter(
                OutputArea21.geom.ST_Contains(stn.geom)
            ).one()
            d[str(stop_id)] = {
                'station_name': s.station.name, #this works because of the relationship btwn CensusTripsRoute obj and RailwayStation obj
                'oa_code': oa.oa_code,
                'oa_totpop': int(oa.totpop)
            }
            if stop_id == 1:
                first_station_name = s.station.name
            else:
                last_station_name = s.station.name

            stop_id += 1
        except sqlalchemy.orm.exc.NoResultFound:
            print("Warning! {} is not a station, skipped".format(s.station.name))

    # set the name of the route - setting
    # TODO: it will not always be ScotRail!
    d['route_name']['title'] = '(2021) ScotRail rail journey from {0} to {1}'.format(first_station_name, last_station_name)

    return d


# TODO: based on the names of the first and last station we can create a name for the route

# TODO: rather than hardcoding which attribute is returned, make this user-defined

# TODO: as per what was done in "lives on the line" noted in the pdf under docs, search for OAs
#  within some distance e.g. 200m of each station and average the stat etc
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
                'oa_code': oa.oacode,
                'oa_totpop01': int(oa.totpop01), #sqlalchemy return values as Decimal('92') etc and then jsonify in app.py complains...
                'oa_totpop11': int(oa.totpop)
            }
            if stop_id == 1:
                first_station_name = s.station.name
            else:
                last_station_name = s.station.name

            stop_id += 1
        except sqlalchemy.orm.exc.NoResultFound:
            print("Warning! {} is not a station, skipped".format(s.station.name))

    # set the name of the route - setting
    # TODO: it will not always be ScotRail!
    d['route_name']['title'] = 'ScotRail rail journey from {0} to {1}'.format(first_station_name, last_station_name)

    return d

