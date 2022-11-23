-- Function

DELIMITER $$
CREATE FUNCTION tax_397(Income VARCHAR(10))
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
	DECLARE tax VARCHAR(100);
	IF  Income <= 10000 THEN
		SET tax = 'A tax of 10% needs to be payed.';
	ELSEIF Income > 10000 AND income <= 50000 THEN
		SET tax = 'A tax of 15% needs to be payed.';
	ELSE
		SET tax = 'A tax of 25% needs to be payed.';
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