/* Все остановки Автобуса М5 */
SELECT st.stop_name AS "Остановка"
FROM stops AS st, transports AS tr, stop_transports AS str
WHERE tr.transport_number = 'Автобус М5'
AND tr.transport_id = str.transport_id AND st.stop_id = str.stop_id
ORDER BY str.stop_transport_id