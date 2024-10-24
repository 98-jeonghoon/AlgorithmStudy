WITH RECURSIVE price_groups AS (
    -- 시작 구간 (0원)
    SELECT 0 AS PRICE_GROUP
    UNION ALL
    -- 10000원씩 증가하는 구간을 재귀적으로 생성
    SELECT PRICE_GROUP + 10000
    FROM price_groups
    WHERE PRICE_GROUP < (SELECT MAX(PRICE) FROM PRODUCT)
)
SELECT 
    pg.PRICE_GROUP, 
    COUNT(p.PRODUCT_ID) AS PRODUCTS
FROM 
    price_groups pg
LEFT JOIN 
    PRODUCT p ON p.PRICE >= pg.PRICE_GROUP AND p.PRICE < pg.PRICE_GROUP + 10000
GROUP BY 
    pg.PRICE_GROUP
HAVING 
    COUNT(p.PRODUCT_ID) > 0  -- 0인 구간을 제외
ORDER BY 
    pg.PRICE_GROUP;
