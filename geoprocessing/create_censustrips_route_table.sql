-- noinspection SqlNoDataSourceInspectionForFile

CREATE TABLE censustrips.censustrips_route(
    id serial primary key,
    route_id integer,
    seq_id integer,
    station_id integer references censustrips.railway_stations  (gid)
)