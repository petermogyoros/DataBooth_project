# SQL View query backup:
CREATE OR REPLACE VIEW past_week (
	combined_side_a_ng_avg_1, combined_side_b_ng_avg_1, combined_side_a_re_avg_1, combined_side_b_re_avg_1,
	combined_side_a_ng_avg_2, combined_side_b_ng_avg_2, combined_side_a_re_avg_2, combined_side_b_re_avg_2,
	combined_side_a_ng_avg_3, combined_side_b_ng_avg_3, combined_side_a_re_avg_3, combined_side_b_re_avg_3,
	combined_side_a_ng_avg_4, combined_side_b_ng_avg_4, combined_side_a_re_avg_4, combined_side_b_re_avg_4,
	combined_side_a_ng_avg_5, combined_side_b_ng_avg_5, combined_side_a_re_avg_5, combined_side_b_re_avg_5,
	combined_side_a_ng_avg_6, combined_side_b_ng_avg_6, combined_side_a_re_avg_6, combined_side_b_re_avg_6,
	combined_side_a_ng_avg_7, combined_side_b_ng_avg_7, combined_side_a_re_avg_7, combined_side_b_re_avg_7
)

AS SELECT
line = 5, line = 8,
-- query for today
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),

-- query for one day ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),

-- query for two days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),

-- query for three days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),

-- query for four days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),

-- query for five days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),

-- query for six days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day')

;
