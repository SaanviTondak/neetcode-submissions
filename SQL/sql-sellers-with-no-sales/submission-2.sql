SELECT s.seller_name
FROM seller s
LEFT JOIN orders o 
    ON s.seller_id = o.seller_id
GROUP BY s.seller_id, s.seller_name
HAVING SUM(
    CASE 
        WHEN o.sale_date >= DATE '2020-01-01'
         AND o.sale_date <  DATE '2021-01-01'
        THEN 1
        ELSE 0
    END
) = 0
order by seller_name