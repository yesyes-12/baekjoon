-- used_goods_board(board_id, writer_id, title, contents, price, created_date, status, views)
-- used_goods_reply(reply_id, board_id, writer_id, contents, created_date)

-- created 2022-10
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, r.created_date
from used_goods_board b, used_goods_reply r
where b.created_date between '2022-10-01' and '2022-10-31'
and b.board_id = r.board_id
order by r.created_date, b.title