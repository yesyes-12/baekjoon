-- first_half(shipment_id, flavor(pk), total_order)
-- icecream_info(flavor(pk,fk), ingredient_type(주성분))

-- 총주문량>=3000 and 주성분 =과일
-- 총주문량 내림차순
SELECT h.flavor
from first_half h left join icecream_info i on h.flavor = i.flavor
where h.total_order >= 3000 and i.ingredient_type = 'fruit_based'
order by total_order desc