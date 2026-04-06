INSERT INTO censustrips.uk_oa_2021_uk008
(
 oa_code, all_persons, male, female, geom
)
select "OA" as oa_code, uk008001 as all_persons, uk008002 as male, uk008003 as female, g.geom
from geods.uk008
left join(
 select geoid as oa_code, geom from nrs.scotland_oa_2022_bfc
 union all
 select oa21cd as oa_code, geom from ons.ew_oa_2021_bfc
 union all
 select dz2021_cd as oa_code, geom from nisra.nireland_dz_2021
) g on (geods.uk008."OA" = g.oa_code)