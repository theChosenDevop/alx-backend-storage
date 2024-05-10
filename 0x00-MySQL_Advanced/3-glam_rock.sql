-- SQL script that lists all bands with Glamrock as their main style
-- Ranked by their longetivity
SELECT band_name, (COALESCE(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
