SELECT g.subject_id, s.subject_name,  AVG(g.grade) as avg_grade 
from grades g 
join subjects s on g.subject_id =s.subject_id 
GROUP BY g.subject_id, s.subject_name;
