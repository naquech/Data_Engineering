# Project: Data Warehouse

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
The task is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs the users are listening to. 

## Project Datasets
The datasets that reside in S3.
<ul>
    <li>Song data: s3://udacity-dend/song_data</li>
    <li>Log data: s3://udacity-dend/log_data</li>
    <li>Log data json path: s3://udacity-dend/log_json_path.json</li>
</ul>

## Schema for Song Play Analysis

<p>
    <b>Fact Table</b><br>
    songplay: records in event data associated with song plays</p>
    <b>Columns:</b> songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
</p>

<p>
    <b>Dimension Tables</b><br>
    <ol>
        <li>user_table: ser_id, first_name, last_name, gender, level</li>
        <li>song_table: song_id, title, artist_id, year, duration</li>
        <li>artist_table: artist_id, name, location, lattitude, longitude</li>
        <li>time_table: start_time, hour, day, week, month, year, weekday</li>
    </ol>
</p>


## Project Files
<ul>
    <li>create_table.py contains the code to create the fact and dimension tables for the star schema in Redshift.</li>
    <li>etl.py is where data is loaded from S3 into staging tables on Redshift and then process that data into the analytic tables on Redshift.</li>
    <li>sql_queries.py contains the define SQL statements, which will be imported into the two other files above.</li>
</ul>
