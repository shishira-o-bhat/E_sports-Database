-- Function

DELIMITER $$
CREATE FUNCTION tax_397(Income INT)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE tax INT;
	IF  Income <= 10000 THEN
		SET tax = 0.1*Income;
	ELSEIF Income > 10000 AND income <= 50000 THEN
		SET tax = 0.15*Income;
	ELSE
		SET tax = 0.25*Income;
	END IF;
	RETURN tax;
END; $$
DELIMITER ;

-- Procedure
DELIMITER $$

CREATE procedure age()

BEGIN

UPDATE player_397 SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),player_397.dob)), '%Y') + 0;

END; $$

DELIMITER ;