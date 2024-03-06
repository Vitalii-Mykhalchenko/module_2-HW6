SELECT s.student_id,s.first_name || ' '|| s.last_name as full_name, s2.subject_name 
FROM grades g 
join students s  on s.student_id = g.student_id 
JOIN  subjects s2 on s2.subject_id = g.subject_id ;