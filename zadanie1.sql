SELECT 
    "Couriers".login AS "Логин курьера",
    COUNT("Orders".id) AS "Количество заказов"
FROM "Orders"
JOIN "Couriers" ON "Orders"."courierId" = "Couriers".id
WHERE "Orders"."inDelivery" = TRUE
GROUP BY "Couriers".login;