-- Lists all records of the table second_table having a name value.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `sceond_table`
WHERE `name` != ""
ORDER BY `score` DESC
