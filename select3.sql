SELECT gr.name, ROUND(AVG(g.grade), 1), sb.name
FROM grades as g
LEFT JOIN students as s ON s.id = g.id_stud
LEFT JOIN subjects as sb ON sb.id =g.id_sub
LEFT JOIN groups as gr ON s.id_groups =gr.id
WHERE g.id_sub=? GROUP BY gr.id ORDER BY  gr.id
