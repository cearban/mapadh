-- SQL to create route 3 from Edinburgh -> Kings Cross
-- station_id = gid of geocrud.railway_stations
INSERT INTO geocrud.censustrips_route
(route_id, seq_id, station_id)
values
(3, 1, 327),
(3, 2, 342),
(3, 3, 345),
(3, 4, 395),
(3, 5, 393),
(3, 6, 388),
(3, 7, 676),
(3, 8, 668),
(3, 9, 1070),
(3, 10,1792),
(3, 11, 2252);