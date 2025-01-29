import click
import configparser
import os
from postgres import Postgres

config = configparser.ConfigParser()
config.read('/home/james/PycharmProjects/mapadh/CONFIG.ini')
PG_CONNECTION_STRING = config['Connections']['mapadh-db']


@click.command()
@click.option("--station_geoids", required=True, type=click.STRING)
@click.option("--dry_run", is_flag=True)
def add_route(station_geoids, dry_run):
    """
    python scripts/utils.py --station_geoids "132,131,129,130,133,135,134,109,136,159,160,157,206"

    :param route_id:
    :param station_geoids:
    :param dry_run:
    :return:
    """

    db = Postgres(PG_CONNECTION_STRING)

    # obtain the value that route_id is currently set to in the table and increment in the new added route
    current_max_route_id = db.one("SELECT MAX(route_id) FROM geocrud.censustrips_route")
    route_id = current_max_route_id + 1

    geoids = station_geoids.split(",")
    records = ""
    seq_id = 1
    for geoid in geoids:
        records += "({0},{1},{2}),".format(route_id, seq_id, geoid)
        seq_id += 1

    sql_cmd = """INSERT INTO geocrud.censustrips_route(route_id, seq_id, station_id) values {0}""".format(
        records
    )
    sql_cmd = sql_cmd[:-1]

    if dry_run:
        print(sql_cmd)
    else:
        db.run(sql_cmd)


if __name__ == "__main__":
    add_route()
