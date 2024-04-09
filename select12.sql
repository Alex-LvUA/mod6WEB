SELECT st.name, g.grade, g.date
FROM grades as g
LEFT JOIN students as st ON st.id=g.id_stud
WHERE  g.id_sub=(SELECT id FROM subjects WHERE name=?) AND st.id_groups= ?  AND g.date=(SELECT MAX(date) FROM grades)

