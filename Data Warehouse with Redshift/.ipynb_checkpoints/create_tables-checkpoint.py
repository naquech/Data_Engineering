import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


"This function calls all the drop table \n
 statements in the sql_queries.py file"

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

        
"This function calls all the create table \n
 statements in the sql_queries.py file"

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

        
"This function connects to the Redshift cluster and \n
 the database. Calls the function that drop and cerate the \n
 tables"

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()