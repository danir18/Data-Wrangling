CREATE VIEW rural AS
SELECT * FROM census
WHERE locality LIKE '%Rural%';


-- .headers on
--.mode csv
--.output rural.csv
-- SELECT * FROM rural