/* Отчёт о самом длинном по количеству остановок оптимальном маршруте */
CREATE VIEW bid_route AS ( 
	WITH biggest_route AS (
		SELECT rt.start_stop AS start, rt.finish_stop AS finish, MAX(rt.route_part) AS stops, SUM(c.tyme_interval) AS times
		FROM routes AS rt, communications AS c
		WHERE c.communication_id = rt.communication_id
		GROUP BY rt.start_stop, rt.finish_stop
		ORDER BY stops
		DESC
		LIMIT 1
		)

	SELECT rt.start_stop AS "Откуда", rt.finish_stop AS "Куда", bg.times AS "Время пути", bg.stops AS "Количество остановок",
	rt.next_stop AS "Следующая остановка", tr.transport_number AS "Транспорт, который останавливется"
	FROM routes AS rt, biggest_route AS bg, transports AS tr, stops AS st, stop_transports AS str
	WHERE rt.start_stop = bg.start AND rt.finish_stop = bg.finish AND rt.next_stop = st.stop_name AND st.stop_id = str.stop_id 
	AND str.transport_id = tr.transport_id
	GROUP BY rt.next_stop, rt.start_stop, rt.finish_stop, bg.times, tr.transport_number, rt.route_part, bg.stops
	ORDER BY rt.route_part
	)
