import pandas as pd

df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

df = pd.concat([df0, df1, df2], ignore_index=True)

df = df[df['product'] == 'pink morsel']

df['price'] = df['price'].str.slice(1).astype(float)

df['sales'] = df['quantity'].mul( df['price'])

df.drop(['product', 'price', 'quantity'], axis=1, inplace = True)

df.to_csv('data/output_file.csv', index=False)