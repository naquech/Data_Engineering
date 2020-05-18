# DATA MODELING WITH POSTGRES

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 

The purpose is to create a Postgres database with tables designed to optimize queries on song play analysis. 

## Star Schema

### FACT TABLE 

|**songplays**| Column Type 
| :---        | :----       
| songplay_id | numeric       
| start_time  | timestamp       
| user_id     | text
| level       | text
| song_id     | text
| artist_id   | text
| session_id  | text
| location    | text
| user_agent  | text

### Dimension Tables

| *artists* |Column Type ||| *users*   |Column type ||| *time*    | Column Type ||| *songs*  | Column type
| :---      | :----      ||| :----     | :---       ||| :----     | :---        ||| :----    | :--- 
| artist_id | text       ||| user_id   | int        ||| start_time| timestamp   ||| song_id  | text
| name      | text       ||| first_name| text       ||| hour      | int         ||| title    | text
| location  | text       ||| last_name | text       ||| day       | int         ||| artist_id| text
| latitude  | float      ||| gender    | text       ||| week      | int         ||| year     | int
| longitude | float      ||| level     | text       ||| month     | int         ||| duration | float
|           |            |||           |            ||| year      | int         |||          |
|           |            |||           |            ||| weekday   | int         |||          |
|           |            |||           |            |||           |             |||          |

## File Structure

- **sql_queries.py** contains all sql queries.
- **create_tables.py** creates tables. Run this file to reset tables, each time, before running ETL scripts.
- **test.ipynb** displays the first few rows of each table to let you check your database.
- **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- **etl.py** reads and processes files from song_data and log_data and loads them into the tables.
- **test.ipynb** displays the first few rows of each table to let you check your database.
