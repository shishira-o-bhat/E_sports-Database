-- Trigger

DELIMITER $$
CREATE TRIGGER age_checks_397
BEFORE INSERT
ON player_397 FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(50);
DECLARE age INT;
SET error_msg = "Not eligible to play as a professional.";
SELECT DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),new.DOB)), '%Y') 
 + 0 INTO age;

IF age < 18 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$
DELIMITER ;

-- Cursor

DELIMITER $$

CREATE FUNCTION Player_Finder ( In_Team_ID VARCHAR(50) )
RETURNS VARCHAR(50) READS SQL DATA

BEGIN

   DECLARE done INT DEFAULT FALSE;
   DECLARE PlayerName VARCHAR(50);

   DECLARE cursor_player CURSOR FOR
     SELECT Player_Name
     FROM player_397
     WHERE Team_ID = In_Team_ID;

   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

   OPEN cursor_player;
   FETCH cursor_player INTO PlayerName;

   CLOSE cursor_player;

   RETURN PlayerName;

END; $$

DELIMITER ;