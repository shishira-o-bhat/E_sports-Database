-- Union

SELECT revenue_397.Team_ID FROM revenue_397 UNION SELECT team_397.Team_ID FROM team_397;

-- Intersection

SELECT revenue_397.Team_ID FROM revenue_397 INTERSECT SELECT team_397.Team_ID FROM team_397;

-- Set difference

SELECT team_397.Team_ID FROM team_397 EXCEPT SELECT player_397.Team_ID FROM player_397;

-- Cross Join

SELECT player_397.player_name,team_397.team_name FROM player_397 CROSS JOIN team_397;