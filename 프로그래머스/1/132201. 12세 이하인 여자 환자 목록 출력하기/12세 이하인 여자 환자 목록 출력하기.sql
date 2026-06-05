-- patient(pt_no, pt_name, gend_cd(성별), age, tlno(전화번호))

-- under 12, female, 
SELECT pt_name,pt_no, gend_cd, age, ifnull(tlno, 'NONE') as tlno
from patient
where age<=12 and gend_cd='W'
order by age desc, pt_name asc