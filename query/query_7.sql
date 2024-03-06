SELECT g.student_id ,s.first_name || ' '||  s.last_name  as full_name , g2.group_name, g.grade , s2.subject_name 
FROM grades g 
join students s on g.student_id = s.student_id 
JOIN  groups g2  on g2.group_id = s.group_id 
JOIN subjects s2  on s2.subject_id = g.subject_id  