import polars as pl

df = pl.read_csv('files/weather.csv')

temp_mean = df['temperature'].mean()
humidity_mean = df['humidity'].mean()

df = df.with_columns([pl.col('temperature').fill_null(temp_mean),
                      pl.col('humidity').fill_null(humidity_mean)])

df = df.with_columns((pl.col('temperature') - temp_mean).alias('temp-diff'))
df = df.with_columns(pl.col('date').str.slice(5, 2).cast(pl.Int32).alias('month'))

print(df)

pivot_df = df.group_by('month').agg(pl.mean('temperature').alias('average_temperature'))
print(pivot_df)

pivot_df.write_csv('files/pivot_table.csv')
