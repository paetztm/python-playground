import pandas


df = pandas.DataFrame({
    'A': [-137, 22, -3, 4, 5],
    'B': [10, 11, 121, 13, 14],
    'C': [3, 6, 91, 12, 15],
})

print(df)

positive_a = df[df.A > 0]

print(positive_a)