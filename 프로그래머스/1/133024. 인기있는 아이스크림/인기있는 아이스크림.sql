-- first_half(shipment_id(출하번호), flavor(아스크림 맛), total_order(주문량))

-- 아이스크림의 맛을 총주문량을 기준으로 내림차순 정렬
-- 총주문량이 같은 경우 출하번호 기준 오름차순
SELECT flavor
from first_half
group by flavor
order by total_order desc, shipment_id