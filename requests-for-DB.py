# Татьяна Шумилова, 11 когорта - дипломный проект, 2 часть

# Запрос 1
#
# Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
# Для этого: выведи список логинов курьеров с количеством их заказов
# в статусе «В доставке» (поле inDelivery = true)

SELECT "c"."login",
	COUNT("o"."id") AS "Orders in work"
FROM "Couriers" AS "c"
INNER JOIN "Orders" AS "o" ON "c"."id" = "o"."courierId"
WHERE "o"."inDelivery"=TRUE
GROUP BY "c"."login";


# Запрос 2
#
# Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
# Для этого: выведи все трекеры заказов и их статусы.
# Статусы определяются по следующему правилу:
# Если поле finished == true, то вывести статус 2.
# Если поле canсelled == true, то вывести статус -1.
# Если поле inDelivery == true, то вывести статус 1.
# Для остальных случаев вывести 0.

SELECT "track",
	CASE
		WHEN "finished"=TRUE THEN '2'
		WHEN "cancelled"=TRUE THEN '-1'
		WHEN "inDelivery"=TRUE THEN '1'
		ELSE '0'
END AS "Status"
FROM "Orders";
