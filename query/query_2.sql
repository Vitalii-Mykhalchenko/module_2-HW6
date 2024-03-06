SELECT s.student_id, s.first_name, s.last_name, g.subject_id, sub.subject_name, AVG(g.grade ) as avarage_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id 
JOIN subjects sub ON g.subject_id = sub.subject_id
GROUP BY s.student_id
ORDER BY avarage_grade DESC
LIMIT 1;