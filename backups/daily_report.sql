SELECT dolcegusto_dolcegusto_table.line,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.a_ok) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.combined_side_a_ng) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng + dolcegusto_dolcegusto_table.combined_side_a_re + dolcegusto_dolcegusto_table.a_ok) * 100::numeric, 1)
           ELSE 0::numeric
       END AS combined_side_a_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.b_ok) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.combined_side_b_ng) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng + dolcegusto_dolcegusto_table.combined_side_b_re + dolcegusto_dolcegusto_table.b_ok) * 100::numeric, 1)
           ELSE 0::numeric
       END AS combined_side_b_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.a_ok) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.combined_side_a_re) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng + dolcegusto_dolcegusto_table.combined_side_a_re + dolcegusto_dolcegusto_table.a_ok) * 100::numeric, 1)
           ELSE 0::numeric
       END AS combined_side_a_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.b_ok) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.combined_side_b_re) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng + dolcegusto_dolcegusto_table.combined_side_b_re + dolcegusto_dolcegusto_table.b_ok) * 100::numeric, 1)
           ELSE 0::numeric
       END AS combined_side_b_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_top_ng) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_top_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_top_ng) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_top_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_bottom_ng) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_bottom_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_bottom_ng) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_bottom_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_side_ng) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_side_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_side_ng) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_side_ng,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_top_re) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_top_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_top_re) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_top_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_bottom_re) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_bottom_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_bottom_re) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_bottom_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_a_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.a_side_re) / avg(dolcegusto_dolcegusto_table.combined_side_a_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS a_side_re,
       CASE
           WHEN avg(dolcegusto_dolcegusto_table.combined_side_b_ng) > 0::numeric THEN round(avg(dolcegusto_dolcegusto_table.b_side_re) / avg(dolcegusto_dolcegusto_table.combined_side_b_ng) * 100::numeric, 1)
           ELSE 0::numeric
       END AS b_side_re,
   date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime) AS day
  FROM dolcegusto_dolcegusto_table
 GROUP BY dolcegusto_dolcegusto_table.line, (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime))
 ORDER BY (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime)) DESC LIMIT 7;
