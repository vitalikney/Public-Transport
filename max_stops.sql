/* Отчёт о количествах остановок у каждого транспорта */
CREATE VIEW bus_stops AS (
	SELECT tr.transport_number AS "Номер транспорта", COUNT(p.transport_id) AS "Количество остановок"
	FROM stop_transports AS p, transports AS tr
	WHERE tr.transport_id = p.transport_id
	GROUP BY p.transport_id, tr.transport_number
	ORDER BY "Количество остановок"
	DESC
	)
