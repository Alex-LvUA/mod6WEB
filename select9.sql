SELECT st.name, sb.name
FROM grades as g
LEFT JOIN students as st ON st.id = g.id_stud
LEFT JOIN subjects as sb ON sb.id =g.id_sub
WHERE g.id_stud IN (SELECT id FROM students WHERE name LIKE ? ) GROUP BY g.id_stud, g.id_sub
