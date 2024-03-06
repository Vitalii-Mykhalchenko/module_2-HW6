SELECT t.first_name || ' ' || t.last_name as full_name, s.subject_name
FROM teachers t  
JOIN subjects_teachers st ON st.teacher_id = t.teacher_id 
JOIN subjects s ON s.subject_id = st.subject_id
GROUP BY full_name, s.subject_name;
