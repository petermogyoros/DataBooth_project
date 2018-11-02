SELECT dolcegusto_dolcegusto_table.line,
    avg(dolcegusto_dolcegusto_table.batch) AS batch,
    avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS combined_side_a_ng,
    avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS combined_side_b_ng,
    avg(dolcegusto_dolcegusto_table.combined_side_a_re) AS combined_side_a_re,
    avg(dolcegusto_dolcegusto_table.combined_side_b_re) AS combined_side_b_re,

    date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime) AS day
   FROM dolcegusto_dolcegusto_table
  GROUP BY dolcegusto_dolcegusto_table.line, (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime))
  ORDER BY (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime)) DESC;
