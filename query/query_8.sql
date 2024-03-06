SELECT  t.first_name || ' '|| t.last_name as full_name, s.subject_name , AVG(g.grade) as average_grade
FROM subjects_teachers st 
JOIN teachers t ON st.teacher_id = t.teacher_id 
JOIN subjects s ON st.subject_id = s.subject_id
JOIN grades g  on s.subject_id = g.grade_id 
GROUP BY t.teacher_id, full_name;
