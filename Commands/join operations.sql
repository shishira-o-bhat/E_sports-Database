-- Natural Join

SELECT * FROM game_397 NATURAL JOIN competition_397;

-- Inner Join

SELECT Game_Name,Creator FROM game_397 INNER JOIN competition_397 WHERE game_397.Game_ID = competition_397.Game_ID;

-- Left Outer Join

SELECT player_397.Player_Name,team_397.Team_Name FROM player_397 LEFT JOIN team_397 ON team_397.Team_ID = player_397.Team_ID;

-- Right Outer Join

 SELECT team_397.Team_Name,revenue_397.Source_name FROM revenue_397 RIGHT JOIN team_397 ON revenue_397.Team_ID = team_397.Team_ID;

-- Nested Join

SELECT player_397.Player_Name,Team_397.Team_Name,Competition_Name FROM participates_397 NATURAL JOIN competition_397 JOIN team_397 ON team_397.Team_ID = participates_397.Team_ID JOIN player_397 ON player_397.Team_ID = team_397.Team_ID;



