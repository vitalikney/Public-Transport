/* Маршрут от Баррикадная до Курская 3 */
WITH route_info AS ( 
	SELECT rt.next_stop, c.tyme_interval
	FROM routes AS rt, communications AS c
	WHERE rt.start_stop = 'Баррикадная' AND rt.finish_stop = 'Курская 3' 
	AND c.communication_id = rt.communication_id
	GROUP BY rt.route_part, rt.next_stop, c.tyme_interval
)
SELECT * FROM route_info
