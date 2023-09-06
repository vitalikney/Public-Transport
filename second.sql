WITH route_info AS ( 
	SELECT rt.next_stop, c.tyme_interval
	FROM routes AS rt, communications AS c
	WHERE rt.start_stop = 'Большой Строченовский переулок' AND rt.finish_stop = 'Улица Достоевского' 
	AND c.communication_id = rt.communication_id
	GROUP BY rt.route_part, rt.next_stop, c.tyme_interval
)
SELECT * FROM route_info