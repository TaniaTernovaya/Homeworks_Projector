-- Create next analytic queries: Find a user who had the biggest amount of reservations. Return username and user_id

SELECT guest_id,COUNT(*) as reservation_count
FROM booking
GROUP BY guest_id
ORDER BY COUNT(*) DESC
LIMIT 1

-- Find a host who earned the biggest amount of money for the last month. Return hostname and host_id
SELECT h.host_name, h.host_id, SUM(b.price) AS total_earnings
FROM hosts h
JOIN rooms r ON h.host_id = r.host_id
JOIN booking b ON r.room_id = b.room_id
WHERE b.start_day >= DATE_TRUNC('month', CURRENT_DATE) AND
      b.start_day < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'
GROUP BY h.host_name, h.host_id
ORDER BY total_earnings DESC
LIMIT 1;

-- Find a host with the best average rating. Return hostname and host_id
SELECT h.host_name, h.host_id, AVG(r.ratings) AS avg_rating
FROM hosts h
JOIN rooms rm ON h.host_id = rm.host_id
JOIN reviews r ON rm.room_id = r.room_id
GROUP BY h.host_name, h.host_id
ORDER BY avg_rating DESC
LIMIT 1;