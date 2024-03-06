SELECT  AVG( g.grade) as average_grade, s.subject_name 
FROM grades g 
join subjects s on s.subject_id = g.subject_id 
WHERE s.subject_name = 'Механіка'
GROUP BY  s.subject_name;