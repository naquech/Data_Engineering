import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


"This function copies the data from S3 bucket \n
 to the staging table"

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


"This function runs the insert staments \n
 to the staging tables"

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


"This function connects to the Redshift cluster and \n
 the database. loads the data from the staging tables to \n
 the analytics tables on Redshift"

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()