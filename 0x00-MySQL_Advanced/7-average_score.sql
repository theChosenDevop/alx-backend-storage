-- SQL script that creates a stored procedure ComputerAverageScoreForUser that computes and
-- store the average score for a student. The average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN p_user_id INT)
BEGIN
	DECLARE p_score FLOAT;

	SET p_score = 0;

	SELECT AVG(score) INTO p_score FROM corrections WHERE user_id = p_user_id;

	UPDATE users SET average_score = p_score WHERE id = p_user_id;
END $$

DELIMITER ;
