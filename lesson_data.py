import pandas as pd
month_data = ["january", "february", "march", "april", "may", "june",]
sales = {
    "revenue" : [1500, 2000, 2500, 3000, 3500, 4000],
    "items_sold" : [500, 700, 800, 900, 1000, 1100],
    "new_customers" : [50, 80, 90, 100, 120, 150]
}
df = pd.DataFrame(sales, index=month_data)
print(df)

