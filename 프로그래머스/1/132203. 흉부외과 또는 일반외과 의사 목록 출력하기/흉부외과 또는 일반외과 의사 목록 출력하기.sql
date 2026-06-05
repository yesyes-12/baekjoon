-- doctor(dr_name, dr_id, lcns_no, hire_ymd, mcdp_cd(진료과코드), tlno(전번))

-- cs or gs
SELECT dr_name, dr_id, mcdp_cd, hire_ymd
from doctor
where mcdp_cd in ('CS', 'GS')
order by hire_ymd desc, dr_name