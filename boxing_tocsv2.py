import sqlite3
import pandas as pd

# Function to execute a query and save the result to a CSV file
def query_to_csv(db_path, query, output_path):
    # Connect to the SQLite database
    with sqlite3.connect(db_path) as conn:
        # Execute the query and load the result into a DataFrame
        df = pd.read_sql_query(query, conn)
        # Save the DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Exported results to {output_path}")

# Define your database path
db_path = 'boxing.db'

# Define your queries and corresponding output CSV file names
queries = {"total_punches_landed": """
        SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Total Punches Landed'
        FROM(
            SELECT fighter, landed FROM rename_caneloB
            UNION ALL
            SELECT fighter, landed FROM rename_caneloG
            UNION ALL
            SELECT fighter, landed FROM rename_usyk1
            UNION ALL
            SELECT fighter, landed FROM rename_usyk2
        ) AS Combined
        WHERE fighter IN ('Canelo','Usyk')
        GROUP BY fighter;
    """,
    "total_punches_missed": """
        SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'missed' THEN 1 ELSE 0 END) AS 'Total Punches Missed'
        FROM combined_fighters
        WHERE fighter IN ('Canelo','Usyk')
        GROUP BY fighter;
    """,
    "total_missed_landed": """
        SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Total Punches Landed', 
        SUM(CASE WHEN landed = 'missed' THEN 1 ELSE 0 END) AS 'Total Punches Missed'
        FROM combined_fighters
        WHERE fighter IN ('Canelo','Usyk')
        GROUP BY fighter;
    """,
    "percentage_jab_PowerPunch": """
        SELECT 
        fighter AS Fighter,
        COUNT(CASE WHEN punch_type = 'powerpunch' THEN 1 END) * 100.0 / COUNT(punch_type != 'hold') AS 'Percentage Powerpunch', 
        COUNT(CASE WHEN punch_type = 'jab' THEN 1 END) * 100.0 / COUNT(punch_type != 'hold') AS 'Percentage Jab' 
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
    "Canelo_PowerType_thrown": """
        SELECT power_punch AS 'Punch Type', COUNT(*) AS 'Thrown', 
            COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Landed'
        FROM combined_canelo
        WHERE fighter = 'Canelo' AND power_punch IN ('cross','hook','uppercut')
        GROUP BY power_punch;
    """,
    "Usyk_PowerType_thrown": """
        SELECT power_punch AS 'Punch Type', COUNT(*) AS 'Thrown', 
            COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Landed'
        FROM combined_usyk
        WHERE fighter = 'Usyk' AND power_punch IN ('cross','hook','uppercut')
        GROUP BY power_punch;
    """,
    "Canelo_punches_PerRound": """
        SELECT fighter AS Fighter, round, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Landed Punches'
        FROM combined_fighters 
        WHERE fighter IN ('Canelo') 
        GROUP BY round 
        ORDER BY round;
    """,
    "Usyk_punches_PerRound": """
        SELECT fighter AS Fighter, round, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Landed Punches'
        FROM combined_fighters 
        WHERE fighter IN ('Usyk') 
        GROUP BY round 
        ORDER BY round;
    """,
    "combo_v_single": """
        SELECT fighter AS Fighter, SUM(CASE WHEN combo = 'Combo' THEN 1 ELSE 0 END) AS 'Combo Punches Landed', 
        SUM(CASE WHEN combo = 'Single' THEN 1 ELSE 0 END) AS 'Single Punches Landed'
        FROM combined_fighters 
        WHERE fighter IN ('Usyk','Canelo')
        GROUP BY fighter;
    """,
    "total_counters_landed": """
        SELECT fighter AS Fighter, SUM(CASE WHEN counter_punch = 'counterpunch' THEN 1 END) 
            AS 'Counter Punches Landed' 
        FROM combined_fighters
        WHERE fighter IN ('Usyk','Canelo')
        GROUP BY fighter;
    """,
    "Canelo_landed_ByPlacement": """
        SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
        FROM combined_canelo
        WHERE landed = 'landed' 
        GROUP BY Placement;
    """,
    "Usyk_landed_ByPlacement": """
        SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
        FROM combined_usyk
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
        SELECT punch_type AS 'Punch Type' , COUNT(*) AS Count 
        FROM combined_usyk 
        WHERE fighter = 'Usyk'
        GROUP BY punch_type;
    """,
    "Usyk_landed/missed_round": """
        SELECT round AS Round, 
            COUNT(CASE WHEN punch_type != 'hold' THEN 1 END) AS 'Punches Thrown',
            COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Punches Landed'
        FROM combined_usyk
        WHERE fighter = 'Usyk'
        GROUP BY round;
    """,
    "Canelo_landed/missed_round": """
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

# Loop through the queries and export each result to a CSV file
for query_name, query in queries.items():
    output_path = f"{query_name}.csv"
    query_to_csv(db_path, query, output_path)
