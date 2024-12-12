import sqlite3
import pandas as pd
import os

# Connect to SQLite database
db_path = 'boxing.db'
conn = sqlite3.connect(db_path)

# Loading the .sql file
sql_file_path = 'boxing.sql'
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script to set up views and other commands
conn.executescript(sql_script)

# Defining the queries for data extraction
queries = {

    "total_missed_landed": """
        SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Total Punches Landed', 
        SUM(CASE WHEN landed = 'missed' THEN 1 ELSE 0 END) AS 'Total Punches Missed'
        FROM combined_fighters
        WHERE fighter IN ('Canelo','Usyk')
        GROUP BY fighter;
    """,
    "PowerPunches_thrown": """
        SELECT fighter AS Fighter,
            SUM(CASE WHEN punch_type = 'powerpunch' THEN 1 ELSE 0 END) AS 'Power Punches',
            SUM(CASE WHEN punch_type = 'jab' THEN 1 ELSE 0 END) AS 'Jabs'
        FROM combined_fighters
        WHERE fighter IN ('Canelo','Usyk')
        GROUP BY fighter;
    """,
    "combo_v_single": """
        SELECT fighter AS Fighter, SUM(CASE WHEN combo = 'Combo' THEN 1 ELSE 0 END) AS 'Combo Punches Landed', 
        SUM(CASE WHEN combo = 'Single' THEN 1 ELSE 0 END) AS 'Single Punches Landed'
        FROM combined_fighters 
        WHERE fighter IN ('Usyk','Canelo')
        GROUP BY fighter;
    """,
    "Usyk_landed_ByPlacement": """
        SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
        FROM combined_usyk
        WHERE landed = 'landed' 
        GROUP BY Placement;
    """,
    "Canelo_landed_ByPlacement": """
        SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
        FROM combined_canelo
        WHERE landed = 'landed' 
        GROUP BY Placement;
    """,
    "Canelo_PunchType_total": """
        SELECT punch_type AS 'Punch Type' , COUNT(*) AS Count 
        FROM combined_canelo 
        WHERE fighter = 'Canelo'
        GROUP BY punch_type;
    """,
    "Usyk_PunchType_total": """
        SELECT punch_type AS 'Punch Type', COUNT(*) AS Count 
        FROM combined_usyk
        WHERE punch_type IN ('hold','jab','powerpunch')
            AND fighter = 'Usyk'
        GROUP BY punch_type;
    """,
    "Usyk_landed_missed_round": """
        SELECT round AS Round, 
            COUNT(CASE WHEN punch_type != 'hold' THEN 1 END) AS 'Punches Thrown',
            COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Punches Landed'
        FROM combined_usyk
        WHERE fighter = 'Usyk'
        GROUP BY round;
    """,
    "Canelo_landed_missed_round": """
        SELECT round AS Round, 
            COUNT(punch_type != 'hold') AS 'Punches Thrown',
            COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Punches Landed'
        FROM combined_canelo
        WHERE fighter = 'Canelo'
        GROUP BY round;
    """,
    "Canelo_opponents": """
        SELECT SUM(CASE WHEN fighter = 'Canelo' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Canelo', 
            SUM(CASE WHEN fighter != 'Canelo' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Opponents'
        FROM combined_canelo;
    """,
    "Usyk_opponents": """
        SELECT SUM(CASE WHEN fighter = 'Usyk' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Usyk', 
            SUM(CASE WHEN fighter != 'Usyk' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Opponents'
        FROM combined_usyk;
    """
}
#Create a visualization_data folder
output_folder = 'visualization_data'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for query_name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    output_path = os.path.join(output_folder, f"{query_name}.csv")
    df.to_csv(output_path, index=False)
    print(f"Exported results to {output_path}")

# Close the connection
conn.close()