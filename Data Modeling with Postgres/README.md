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

| *artists* |Column Type 
| :---      | :----      
| artist_id | text       
| name      | text       
| location  | text       
| latitude  | float      
| longitude | float      

| *users*   |Column type 
| :----     | :---       
| user_id   | int        
| first_name| text       
| last_name | text       
| gender    | text       
| level     | text       


| *time*    | Column Type 
| :---      | :----             
| start_time| timestamp   
| hour      | int         
| day       | int         
| week      | int         
| month     | int         
| year      | int         
| weekday   | int         

| *songs*  | Column type
|  :----    | :--- 
|  song_id  | text
|  title    | text
|  artist_id| text
|  year     | int
| duration | float


## File Structure

- **sql_queries.py** contains all sql queries.
- **create_tables.py** creates tables. Run this file to reset tables, each time, before running ETL scripts.
- **test.ipynb** displays the first few rows of each table to let you check your database.
- **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- **etl.py** reads and processes files from song_data and log_data and loads them into the tables.
- **test.ipynb** displays the first few rows of each table to let you check your database.
