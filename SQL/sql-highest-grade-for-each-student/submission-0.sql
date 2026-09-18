select student_id, exam_id, score
from (
    select e.*,
    row_number() over(
        partition by student_id
        order by score desc, 
        exam_id asc ) as rn
    from exam_results e
    ) as x
    where x.rn = 1

