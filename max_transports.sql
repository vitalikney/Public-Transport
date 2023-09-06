/* Три остановки с самым нагруженным транспортным трафиком */
WITH Max_Transports AS (
	SELECT COUNT(p.stop_id) AS "Max", p.stop_id
	FROM stop_transports AS p
	GROUP BY p.stop_id
	ORDER BY "Max"
	DESC
	LIMIT 3
	)

SELECT st.stop_name AS "Остановка", tr.transport_number AS "Транспорт"
FROM Max_Transports AS MA, stop_transports AS p, stops AS st, transports AS tr
WHERE MA.stop_id = p.stop_id AND p.stop_id = st.stop_id AND p.transport_id = tr.transport_id
ORDER BY "Остановка"