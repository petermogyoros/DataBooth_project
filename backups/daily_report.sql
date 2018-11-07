SELECT dolcegusto_dolcegusto_table.line,
    round(avg(dolcegusto_dolcegusto_table.combined_side_a_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS combined_side_a_ng,
    round(avg(dolcegusto_dolcegusto_table.combined_side_b_ng) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS combined_side_b_ng,
    round(avg(dolcegusto_dolcegusto_table.combined_side_a_re) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS combined_side_a_re,
    round(avg(dolcegusto_dolcegusto_table.combined_side_b_re) / avg(dolcegusto_dolcegusto_table.batch) * 100, 2) AS combined_side_b_re,

    date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime) AS day
   FROM dolcegusto_dolcegusto_table
  GROUP BY dolcegusto_dolcegusto_table.line, (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime))
  ORDER BY (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime)) DESC;
