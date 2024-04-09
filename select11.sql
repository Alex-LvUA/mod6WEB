SELECT st.name, t.name, ROUND(AVG(g.grade), 1) as sgr
FROM grades as g
LEFT JOIN students as st ON st.id = g.id_stud
LEFT JOIN subjects as sb ON sb.id =g.id_sub
LEFT JOIN teachers as t ON t.id = sb.id_teacher
WHERE g.id_sub IN (SELECT sb.id FROM subjects WHERE sb.id_teacher IN (SELECT id FROM teachers WHERE name LIKE ? ))
AND g.id_stud IN (SELECT id FROM students WHERE name LIKE ?)
GROUP BY g.id_stud, t.id
