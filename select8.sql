SELECT t.name, ROUND(AVG(g.grade), 1)
FROM grades as g
LEFT JOIN subjects as sb ON sb.id =g.id_sub
LEFT JOIN teachers as t ON t.id = sb.id_teacher
WHERE t.name LIKE ? GROUP BY t.id
