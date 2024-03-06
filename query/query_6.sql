SELECT  s.student_id, s.first_name || ' '|| s.last_name AS full_name , g.group_name 
from students s 
join groups g on s.group_id = g.group_id 
ORDER BY g.group_id  DESC;