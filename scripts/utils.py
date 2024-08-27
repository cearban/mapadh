import click
import configparser
import os
from postgres import Postgres

config = configparser.ConfigParser()
config.read('/home/james/PycharmProjects/mapadh/CONFIG.ini')
PG_CONNECTION_STRING = config['Connections']['mapadh-db']


@click.command()
@click.option("--route_id", required=True, type=click.INT)
@click.option("--station_geoids", required=True, type=click.STRING)
@click.option("--dry_run", is_flag=True)
def add_route(route_id, station_geoids, dry_run):
    """
    python scripts/utils.py --route_id 2 --station_geoids "132,131,129,130,133,135,134,109,136,159,160,157,206"

    :param route_id:
    :param station_geoids:
    :param dry_run:
    :return:
    """
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
        db = Postgres(PG_CONNECTION_STRING)
        db.run(sql_cmd)


if __name__ == "__main__":
    add_route()





