-- ecoli_data(id, parent_id, size_of_colony, differentiation_date(분화날짜), genotype(형질))

-- id, count(child), if doesnt have child print0, asc
select p.id, count(c.id) child_count
from ecoli_data p left join ecoli_data c on p.id = c.parent_id
group by p.id
order by p.id
