SELECT s.id, ROUND(AVG(g.grade), 1) as sgr, s.name, sb.name
FROM grades as g
LEFT JOIN students as s ON s.id = g.id_stud
LEFT JOIN subjects as sb ON sb.id =g.id_sub
WHERE g.id_sub=? GROUP BY g.id_stud, g.id_sub  ORDER BY  sgr