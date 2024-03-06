SELECT g.student_id , g.subject_id , g.grade ,g.grade_date ,s.first_name || ' '||  s.last_name  as full_name  , s2.subject_name 
from grades g 
join students s on s.student_id  = g.student_id 
JOIN subjects s2  on s2.subject_id = g.subject_id 
WHERE 
 	s.first_name = 'Соломон' 
    AND s.last_name = 'Андріїшин' 
    AND g.grade_date = '2024-03-04 22:27:13'
    AND s2.subject_name = 'Фізика'
;