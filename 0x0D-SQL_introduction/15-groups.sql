-- number of records with the same score

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
Having name1.score == name2.score
ORDER BY score DESC;
