-- rest_info(rest_id, rest_name, food_type, views, favorites, parking_lot,address, tel)
-- rest_review(review_id, rest_id, member_id, review_score, review_text, review_date)
SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score),2) score
from rest_info i join rest_review r on i.rest_id = r.rest_id
where address like '서울%'
group by rest_name
order by score desc, favorites desc