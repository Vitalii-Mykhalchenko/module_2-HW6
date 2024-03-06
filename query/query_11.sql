SELECT DISTINCT s.subject_name  AS course_name, stu.student_id, stu.first_name || ' ' || stu.last_name AS full_name,
s.subject_name, t.teacher_id, t.first_name || ' ' || t.last_name as full_name_teacher, AVG( g.grade ) as average_grade
FROM grades g
JOIN subjects_teachers st ON g.subject_id = st.subject_id
JOIN subjects s ON g.subject_id = s.subject_id
JOIN teachers t ON st.teacher_id = t.teacher_id
JOIN students stu ON g.student_id = stu.student_id
WHERE stu.first_name = 'Ірина' AND stu.last_name = 'Слюсар'
AND t.first_name = 'Болеслав' AND t.last_name = 'Шаповал';
