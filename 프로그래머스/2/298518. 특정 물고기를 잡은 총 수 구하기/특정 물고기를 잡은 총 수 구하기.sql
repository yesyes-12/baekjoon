-- fish_info(id, fish_type, length, time)
-- fish_name_info(fish_type, fish_name)

-- count bass and snapper
select count(i.id) as 'FISH_COUNT'
from fish_info i join fish_name_info n on i.fish_type = n.fish_type
where n.fish_name in ("BASS","SNAPPER")