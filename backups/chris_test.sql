SELECT dolcegusto_dolcegusto_table.line,
    avg(dolcegusto_dolcegusto_table.combined_side_a_ng) AS sidea_ng,
    avg(dolcegusto_dolcegusto_table.combined_side_b_ng) AS sideb_ng,
    date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime) AS hour
   FROM dolcegusto_dolcegusto_table
  GROUP BY dolcegusto_dolcegusto_table.line, (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime))
  ORDER BY (date_trunc('day'::text, dolcegusto_dolcegusto_table.csv_datetime)) DESC;
