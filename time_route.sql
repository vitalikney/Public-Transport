/* Время между Трубной и Парк культуры 1 */
WITH time_route AS ( 
	SELECT SUM(c.tyme_interval)
	FROM routes AS rt, communications AS c
	WHERE rt.start_stop = 'Трубная' AND rt.finish_stop = 'Парк культуры 1' 
	AND c.communication_id = rt.communication_id
)
SELECT * FROM time_route