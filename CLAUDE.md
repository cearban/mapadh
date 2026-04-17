# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

**mapadh** is a Flask web app that queries census and railway geospatial data from PostGIS and returns population statistics along rail routes. The core idea (from the "Lives on the Line" article in `docs/`) is: given a rail route defined as an ordered sequence of stations, find the 2021 UK census Output Area (OA) data associated with each station and render it as HTML or JSON.

## Running the app

```bash
export FLASK_APP=app.py
flask run
```

Requires `CONFIG.ini` in the project root (not committed — see below). Dependency management uses `uv` with Python 3.14.

```bash
uv sync          # install deps
uv run flask run # run via uv
```

## Configuration

`CONFIG.ini` must exist in the project root with a PostgreSQL connection string:

```ini
[Connections]
mapadh-db=postgresql+psycopg2://censustrips:<password>@localhost:5432/censustrips
```

## Key endpoints

- `GET /censustrips_route/<route_id>` — HTML table of population per station (exact OA containing station point)
- `GET /censustrips_buffered_route/<route_id>` — HTML table using 200m buffer + average across intersecting OAs
- `GET /censustrips_route_json/<route_id>` — JSON version of the above
- `GET /censustrips_buffered_route_json/<route_id>` — JSON version of buffered

## Database schema

All tables live in the `censustrips` PostgreSQL schema with PostGIS geometry columns in SRID 27700 (British National Grid):

- `censustrips.uk_oa_2021_uk008` — 2021 UK census Output Areas (MULTIPOLYGON), with `all_persons`, `male`, `female` from the GeoDS unified census dataset
- `censustrips.railway_stations` — station points (POINT)
- `censustrips.railways_lines` — railway line geometry (MULTILINESTRING)
- `censustrips.censustrips_route` — ordered sequences of stations forming routes (`route_id`, `seq_id`, `station_id` FK to `railway_stations`)

## Adding a new route

Use the CLI utility (run from the project root):

```bash
python scripts/utils.py --station_geoids "132,131,129,130,133"
# dry run to preview the SQL:
python scripts/utils.py --station_geoids "132,131,129,130,133" --dry_run
```

The `station_geoids` are the `gid` values from `censustrips.railway_stations`.

## Architecture notes

- `censustrips.py` defines the SQLAlchemy ORM models and the two query functions (`fetch_population_along_route`, `fetch_buffered_population_along_route`). Each call creates a new engine + session — no connection pooling across requests.
- `app.py` reads `CONFIG.ini` at module load time (not per-request). The `PG_CONNECTION_STRING` global is used by all route handlers.
- The buffered variant uses `ST_Intersects` (not `ST_Overlaps`) — `ST_Overlaps` returned zero results for rural stations like Ardlui where the station point falls entirely within a single OA boundary.
- `oa_all_persons` is cast to `int` before returning because SQLAlchemy returns `Decimal` values that `jsonify` cannot serialize.
- The template (`templates/route.jinja2`) receives the full dict keyed by stop number, with `route_name` as a special first key.
