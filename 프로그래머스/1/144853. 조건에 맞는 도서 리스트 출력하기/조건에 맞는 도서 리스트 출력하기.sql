-- book(book_id, category, author_id, price, published_date)

-- 2021 published, '인문'
SELECT book_id, published_date
from book
where published_date between '2021-01-01' and '2021-12-31' and category='인문'