SELECT 
    "Orders".track AS "Трекер",
    CASE
        WHEN "Orders".finished = TRUE THEN 2
        WHEN "Orders".cancelled = TRUE THEN -1
        WHEN "Orders"."inDelivery" = TRUE THEN 1
        ELSE 0
    END AS "Статус"
FROM "Orders";