SELECT dolcegusto_dolcegusto_table.line,
    round((avg(dolcegusto_dolcegusto_table.combined_side_a_ng) / (avg(dolcegusto_dolcegusto_table.combined_side_a_ng)+avg(dolcegusto_dolcegusto_table.combined_side_a_re)+avg(dolcegusto_dolcegusto_table.a_ok))) * 100::numeric, 2) AS combined_side_a_ng,
    round((sum(dolcegusto_dolcegusto_table.combined_side_a_ng) / (sum(dolcegusto_dolcegusto_table.combined_side_a_ng+dolcegusto_dolcegusto_table.combined_side_a_re+dolcegusto_dolcegusto_table.a_ok))) * 100::numeric, 2) AS combined_side_a_ng,

    round((avg(dolcegusto_dolcegusto_table.combined_side_b_ng) / (avg(dolcegusto_dolcegusto_table.combined_side_b_ng)+avg(dolcegusto_dolcegusto_table.combined_side_b_re)+avg(dolcegusto_dolcegusto_table.b_ok))) * 100::numeric, 2) AS combined_side_b_ng,

    round((avg(dolcegusto_dolcegusto_table.combined_side_a_re) / (avg(dolcegusto_dolcegusto_table.combined_side_a_re)+avg(dolcegusto_dolcegusto_table.combined_side_a_re)+avg(dolcegusto_dolcegusto_table.a_ok))) * 100::numeric, 2) AS combined_side_a_re,
    round((avg(dolcegusto_dolcegusto_table.combined_side_b_re) / (avg(dolcegusto_dolcegusto_table.combined_side_b_re)+avg(dolcegusto_dolcegusto_table.combined_side_b_re)+avg(dolcegusto_dolcegusto_table.b_ok))) * 100::numeric, 2) AS combined_side_b_re,

    round((avg(dolcegusto_dolcegusto_table.a_top_ng) / (avg(dolcegusto_dolcegusto_table.a_top_ng)+avg(dolcegusto_dolcegusto_table.a_tbottom_ng)+avg(dolcegusto_dolcegusto_table.a_side_ng))) * 100, 2) AS a_top_ng,
    round(avg(dolcegusto_dolcegusto_table.b_top_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS b_top_ng,
    round(avg(dolcegusto_dolcegusto_table.a_bottom_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS a_bottom_ng,
    round(avg(dolcegusto_dolcegusto_table.b_bottom_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS b_bottom_ng,
    round(avg(dolcegusto_dolcegusto_table.a_side_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS a_side_ng,
    round(avg(dolcegusto_dolcegusto_table.b_side_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS b_side_ng,



    date_trunc('hour'::text, dolcegusto_dolcegusto_table.csv_datetime) AS hour
   FROM dolcegusto_dolcegusto_table
  GROUP BY dolcegusto_dolcegusto_table.line, (date_trunc('hour'::text, dolcegusto_dolcegusto_table.csv_datetime))
  ORDER BY (date_trunc('hour'::text, dolcegusto_dolcegusto_table.csv_datetime)) DESC;
