import polars as pl

df = pl.read_csv("files/sales.csv")
print(df.head())

avg_sales = df['sales'].mean()
avg_profit = df['profit'].mean()

df = df.with_columns([pl.col('sales').fill_null(avg_sales), pl.col('profit').fill_null(avg_profit)])

df = df.with_columns((pl.col('sales') - avg_sales).alias('sales_diff'))

df = df.with_columns(pl.col('order_date').str.slice(5, 2).cast(pl.Int32).alias('month'))

print(df)

pivot_df = df.group_by('month').agg(pl.mean('sales').alias('avg_sales'))
print(pivot_df)

pivot_df.write_csv('files/pivot_car_sales_table.csv')