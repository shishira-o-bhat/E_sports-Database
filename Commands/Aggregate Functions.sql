-- Count

SELECT COUNT(*) FROM revenue_397 WHERE revenue_397.Income>100000;

-- Average

SELECT AVG(revenue_397.Income) FROM revenue_397;

-- Minimum

SELECT MIN(player_397.Salary) FROM player_397;

-- Maximum

SELECT MAX(competition_397.Prize_pool) FROM competition_397;

-- Sum

SELECT SUM(player_397.Salary) FROM player_397;
