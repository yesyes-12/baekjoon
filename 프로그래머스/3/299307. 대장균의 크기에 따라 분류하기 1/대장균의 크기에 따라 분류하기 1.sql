-- ecoil_data(id, parent_id, size_of_colony, differentitaion_date, genotype)

-- size <= 100 'low', size > 100 medium, size > 1000 high
select id, if(SIZE_OF_COLONY>1000, 'HIGH', if(SIZE_OF_COLONY>100, 'MEDIUM', if(SIZE_OF_COLONY<=100,'LOW',''))) as SIZE
from ecoli_data