import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ 
        - Each file is in JSON format and contains metadata about a song and the artist of that song.
        - Args: filepath and db cursor. 
        - Return: none
        - Reads the song and saves it in a data frame
        - Pulls song information and inserts it to the songs table
        - Pulls artist information and inserts it to the artist table
    """
    
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = (df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]).tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = (df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 
                       'artist_longitude']].values[0]).tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
        - The log files are in JSON format and based on the songs dataset 
        - Args: filepath and db cursor. 
        - Return: none
        - Reads the song and saves it in a data frame
        - Converts the ts column from 'int' to 'timestamp' data type
        - Pulls timestamp information and inserts it to the time table
        - Pulls user information and inserts it to the users table
        - Pulls record information and inserts it to the songplay table
    """
    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = list((t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday))
    column_labels = list(('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday'))
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (index, pd.to_datetime(row.ts, unit='ms'), int(row.userId), row.level, songid, artistid, 
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
     """
        - Args: filepath, db cursor, db connection, function to process  
        - Return: none
        - Process all files for every given function
    """
        
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
     """
        - Return: none
        - Creates db connection 
        - Calls the process data function for each of the data sets provided
    """
        
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()