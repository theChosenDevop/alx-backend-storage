-- SQL ranks coutry origins of bands
-- Ordered by the number of Fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
