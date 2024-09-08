import polars as pl

df = pl.read_csv("files/cars.csv")
print(df)

print(df.head())

print(df.describe())

cyl_4_df = df.filter(pl.col("cylinders") == 4)
print(cyl_4_df)

mean_horsepower = df.group_by('cylinders').agg(pl.col('horsepower').mean())
print(mean_horsepower)


cyl_4_df.write_csv('files/cly_4_cars.csv')
