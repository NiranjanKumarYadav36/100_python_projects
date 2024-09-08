import polars as pl

df = pl.read_csv('files/iris.csv')
print(df)

print(df.head())

print(df.describe())

setosa_species_df = df.filter(pl.col('species') == 'setosa')
print(setosa_species_df)

mean_sepal_length = df.group_by('species').agg(pl.col('sepal_length').mean())
print(mean_sepal_length)

mean_sepal_length.write_csv('files/mean_sepal_length.csv')