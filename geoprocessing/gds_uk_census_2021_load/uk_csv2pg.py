import configparser
import glob
import os
import pandas as pd
from sqlalchemy import create_engine


def load_csv_into_pg(csv_fname, pg_conn_str):
    if os.path.exists(csv_fname):
        pg_engine = create_engine(pg_conn_str)
        pg_table_name = os.path.splitext(os.path.basename(csv_fname))[0]

        df = None
        df = pd.read_csv(csv_fname)

        if df is not None:
            print('Loading: {0}'.format(csv_fname))
            df.to_sql(
                con=pg_engine,
                name=pg_table_name,
                schema='geods',
                index=True,
                index_label='id'
            )

def main():
    config = configparser.ConfigParser()
    config.read('../../CONFIG.ini')
    pg_conn_str =  (config['Connections']['mapadh-db']).replace('postgresql+psycopg2', 'postgresql')

    for csv_fname in glob.glob('/home/james/geodata/GeographicDS_UK_Census2021/GeoDS/variable_tables_csv/csv/*.csv'):
        load_csv_into_pg(
            csv_fname=csv_fname,
            pg_conn_str=pg_conn_str
        )

if __name__ == '__main__':
    main()

