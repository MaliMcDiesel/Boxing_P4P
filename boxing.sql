--Combined canelo fights
DROP VIEW IF EXISTS combined_canelo;
CREATE VIEW combined_canelo AS
SELECT * FROM rename_caneloB 
UNION ALL 
SELECT * FROM rename_caneloG ;

--Combined usyk fights
DROP VIEW IF EXISTS combined_usyk;
CREATE VIEW combined_usyk AS
SELECT * FROM rename_usyk1 
UNION ALL 
SELECT * FROM rename_usyk2;

--Combined Canelo and Usyk fights
DROP VIEW IF EXISTS combined_fighters;
CREATE VIEW combined_fighters AS
SELECT * FROM rename_caneloB 
UNION ALL 
SELECT * FROM rename_caneloG 
UNION ALL 
SELECT * FROM rename_usyk1 
UNION ALL 
SELECT * FROM rename_usyk2;

--Ananlysis for punches landed 
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

--Analysis for punches missed
SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'missed' THEN 1 ELSE 0 END) AS 'Total Punches Missed'
FROM combined_fighters
WHERE fighter IN ('Canelo','Usyk')
GROUP BY fighter;

-- Punches missed vs punches landed
SELECT fighter AS Fighter, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Total Punches Landed', 
SUM(CASE WHEN landed = 'missed' THEN 1 ELSE 0 END) AS 'Total Punches Missed'
FROM combined_fighters
WHERE fighter IN ('Canelo','Usyk')
GROUP BY fighter;

--Percentage of power punches thrown vs jabs
SELECT 
  fighter AS Fighter,
  COUNT(CASE WHEN punch_type = 'powerpunch' THEN 1 END) * 100.0 / COUNT(punch_type != 'hold') AS 'Percentage Powerpunch', 
  COUNT(CASE WHEN punch_type = 'jab' THEN 1 END) * 100.0 / COUNT(punch_type != 'hold') AS 'Percentage Jab' 
FROM combined_fighters
WHERE fighter IN ('Canelo','Usyk')
GROUP BY fighter;

--Number of Power Punches Thrown
SELECT fighter AS Fighter,
	SUM(CASE WHEN punch_type = 'powerpunch' THEN 1 ELSE 0 END) AS 'Power Punches',
	SUM(CASE WHEN punch_type = 'jab' THEN 1 ELSE 0 END) AS 'Jabs'
FROM combined_fighters
WHERE fighter IN ('Canelo','Usyk')
GROUP BY fighter;

--Power Punch Type Thrown, Canelo
SELECT power_punch AS 'Punch Type', COUNT(*) AS 'Thrown', 
	COUNT(CASE WHEN landed = 'landed'THEN 1 END) AS 'Landed'
FROM combined_canelo
WHERE fighter = 'Canelo' AND power_punch IN ('cross','hook','uppercut')
GROUP BY power_punch;

--Power Punch Type Thrown, Usyk
SELECT power_punch AS 'Punch Type', COUNT(*) AS 'Thrown', 
	COUNT(CASE WHEN landed = 'landed'THEN 1 END) AS 'Landed'
FROM combined_usyk
WHERE fighter = 'Usyk' AND power_punch IN ('cross','hook','uppercut')
GROUP BY power_punch;

--Canelo number of punches landed per round
SELECT fighter AS Fighter, round, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Landed Punches'
FROM combined_fighters 
WHERE fighter IN ('Canelo') 
GROUP BY round 
ORDER BY round;

--Usyk number of punches landed per round
SELECT fighter AS Fighter, round, SUM(CASE WHEN landed = 'landed' THEN 1 ELSE 0 END) AS 'Landed Punches'
FROM combined_fighters 
WHERE fighter IN ('Usyk') 
GROUP BY round 
ORDER BY round;

--Count of combo vs single punches thrown
SELECT fighter AS Fighter, SUM(CASE WHEN combo = 'Combo' THEN 1 ELSE 0 END) AS 'Combo Punches Landed', 
SUM(CASE WHEN combo = 'Single' THEN 1 ELSE 0 END) AS 'Single Punches Landed'
FROM combined_fighters 
WHERE fighter IN ('Usyk','Canelo')
GROUP BY fighter;

--Number or Counters landed
SELECT fighter AS Fighter, SUM(CASE WHEN counter_punch = 'counterpunch' THEN 1 END) 
	AS 'Counter Punches Landed' 
FROM combined_fighters
WHERE fighter IN ('Usyk','Canelo')
GROUP BY fighter;

--Landed Punches by Placement, Canelo
SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
FROM combined_canelo
WHERE landed = 'landed' 
GROUP BY Placement;

--Landed Punches by Placement, Usyk
SELECT placement AS Placement, COUNT(*) AS 'Landed Punches' 
FROM combined_usyk
WHERE landed = 'landed' 
GROUP BY Placement;

--Number of Each Type of Punch Thrown, Canelo
SELECT punch_type AS 'Punch Type' , COUNT(*) AS Count 
FROM combined_canelo 
WHERE fighter = 'Canelo'
GROUP BY punch_type; 

--Number of Each Type of Punch Thrown, Usyk
SELECT punch_type AS 'Punch Type', COUNT(*) AS Count 
FROM combined_usyk
WHERE punch_type IN ('hold','jab','powerpunch')
	AND fighter = 'Usyk'
GROUP BY punch_type;

--Punches Thrown/Landed Per Round, Usyk
SELECT round AS Round, 
	COUNT(CASE WHEN punch_type != 'hold'THEN 1 END) AS 'Punches Thrown',
	COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Punches Landed'
FROM combined_usyk
WHERE fighter = 'Usyk'
GROUP BY round;

--Punches Thrown/Landed Per Round, Canelo
SELECT round AS Round, 
	COUNT(punch_type != 'hold') AS 'Punches Thrown',
	COUNT(CASE WHEN landed = 'landed' THEN 1 END) AS 'Punches Landed'
FROM combined_canelo
WHERE fighter = 'Canelo'
GROUP BY round;
 
 --Canelo Landed Vs Opponents Landed
SELECT SUM(CASE WHEN fighter = 'Canelo' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Canelo', 
	SUM(CASE WHEN fighter != 'Canelo' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Opponents'
FROM combined_canelo;
 
 --Usyk Landed VS Opponents Landed
SELECT SUM(CASE WHEN fighter = 'Usyk' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Usyk', 
	SUM(CASE WHEN fighter != 'Usyk' AND landed = 'landed' THEN 1 ELSE 0 END) AS 'Opponents'
FROM combined_usyk;