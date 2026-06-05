-- member_profile(member_id, member_name, tlno, gender, date_of_birth)

-- birth march, female

select member_id, member_name, gender, date_of_birth
from member_profile
where month(date_of_birth) = '03' and gender = 'W' and tlno is not null
order by member_id