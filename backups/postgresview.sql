SELECT ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime >= '2018-10-23 00:00:00'::timestamp without time zone) AS combined_side_a_ng_avg_1,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime >= '2018-10-23 00:00:00'::timestamp without time zone) AS combined_side_b_ng_avg_1,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime >= '2018-10-23 00:00:00'::timestamp without time zone) AS combined_side_a_re_avg_1,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime >= '2018-10-23 00:00:00'::timestamp without time zone) AS combined_side_b_re_avg_1,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '1 day'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '00:00:00'::interval)) AS combined_side_a_ng_avg_2,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '1 day'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '00:00:00'::interval)) AS combined_side_b_ng_avg_2,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '1 day'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '00:00:00'::interval)) AS combined_side_a_re_avg_2,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '1 day'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '00:00:00'::interval)) AS combined_side_b_re_avg_2,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '2 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '1 day'::interval)) AS combined_side_a_ng_avg_3,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '2 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '1 day'::interval)) AS combined_side_b_ng_avg_3,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '2 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '1 day'::interval)) AS combined_side_a_re_avg_3,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '2 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '1 day'::interval)) AS combined_side_b_re_avg_3,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '3 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '2 days'::interval)) AS combined_side_a_ng_avg_4,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '3 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '2 days'::interval)) AS combined_side_b_ng_avg_4,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '3 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '2 days'::interval)) AS combined_side_a_re_avg_4,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '3 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '2 days'::interval)) AS combined_side_b_re_avg_4,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '4 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '3 days'::interval)) AS combined_side_a_ng_avg_5,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '4 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '3 days'::interval)) AS combined_side_b_ng_avg_5,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '4 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '3 days'::interval)) AS combined_side_a_re_avg_5,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '4 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '3 days'::interval)) AS combined_side_b_re_avg_5,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '5 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '4 days'::interval)) AS combined_side_a_ng_avg_6,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '5 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '4 days'::interval)) AS combined_side_b_ng_avg_6,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '5 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '4 days'::interval)) AS combined_side_a_re_avg_6,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '5 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '4 days'::interval)) AS combined_side_b_re_avg_6,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '6 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '5 days'::interval)) AS combined_side_a_ng_avg_7,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '6 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '5 days'::interval)) AS combined_side_b_ng_avg_7,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '6 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '5 days'::interval)) AS combined_side_a_re_avg_7,
   ( SELECT avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS avg
          FROM dolcegusto_dolcegusto_table
         WHERE dolcegusto_dolcegusto_table.csv_datetime > (CURRENT_DATE - '6 days'::interval) AND dolcegusto_dolcegusto_table.csv_datetime < (CURRENT_DATE - '5 days'::interval)) AS combined_side_b_re_avg_7;
