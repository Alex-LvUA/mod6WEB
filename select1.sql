SELECT s.id, ROUND(AVG(g.grade), 1) as sgr, s.name
FROM grades as g
LEFT JOIN students as s ON s.id = g.id_stud
GROUP BY g.id_stud ORDER BY sgr DESC LIMIT 5