CREATE TABLE censustrips.uk_oa_2021_uk008(
    id serial,
    oa_code varchar,
    all_persons numeric,
    male numeric,
    female numeric,
    geom public.geometry(multipolygon, 27700)
)