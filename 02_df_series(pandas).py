import pandas as pd

vector = [1, 2, 3]
print(vector * 2)
# Створюється список, оператор * не множить числа, а повторює весь список.

series = pd.Series([1, 2, 3])
# Створюється Series (одновимірний масив pandas) з трьома елементами:
print(series * 10)
# Кожен елемент Series множиться на 10, результатом буде новий Series з елементами [10, 20, 30].
series_str = pd.Series(["a", "b", "c"])
print(series_str[0])

months = ['jan', 'feb', 'mar', 'apr']
sales = [100, 200, 300, 400]
data = pd.Series(data=sales, index=months)
print(data)
print(data["feb"])
# pd.Series() створює одновимірний масив (Series) з pandas.
# data=sales → дані (числа)
# index=months → індекси (назви рядків), тепер рядки можна звертатися за ім’ям місяця.

months = ['jan', 'feb', 'mar', 'apr']
sales = {
    'revenue': [100, 200, 300, 400],
    'items_sold': [23, 43, 54, 65],
    'new_clients': [10, 20, 30, 40]
}
df = pd.DataFrame(data=sales, index=months)
print(df)
# Створюємо список, який буде використовуватися як індекси рядків (назви місяців)
# Ключі словника → назви стовпців DataFrame.
# Значення (списки) → дані для кожного стовпця.
# Кількість елементів у списках має відповідати кількості місяців
# DataFrame — це основна таблиця в бібліотеці pandas у Python.
# Простіше кажучи, DataFrame = таблиця, як у Excel, тільки в програмі.
# 📌 Що таке DataFrame:
# ✔️ ДВОВИМІРНА СТРУКТУРА (рядки × колонки)
# DataFrame складається з:
# рядків (index)
# стовпців (columns)
# даних (values)

print(df.head(2))  # З початку рядки
print(df.tail(1))  # з кінця рядки
print(df.revenue)
print(df.info())
# df.info() — метод pandas, який виводить коротку інформацію про DataFrame.
# Виводить:
# Кількість рядків і стовпців
# Імена стовпців
# Кількість непустих значень у кожному стовпці
# Тип даних кожного стовпця (int64, float64, object тощо)
# Обсяг пам’яті, який займає DataFrame

print(df.shape)  # (row, column)
print(df.columns)
print(df.describe())
# Обчислює основні статистики для числових стовпців (за замовчуванням):
# count — кількість непустих значень
# mean — середнє значення
# std — стандартне відхилення
# min — мінімум
# 25%, 50%, 75% — перцентили (квартилі)
# max — максимум

print(df.dtypes)
# dtypes
# Для DataFrame: повертає тип даних кожного стовпця
# Для Series: повертає тип даних самого Series
# Типи даних можуть бути, наприклад:
# int64 — ціле число
# float64 — число з плаваючою комою
# object — рядки / текст
# bool — логічне значення
# datetime64[ns] — дата/час

print(df.loc[['feb', 'apr']])
# У pandas .loc — це дуже потужний індексатор для вибору даних за мітками (label-based indexing) у DataFrame або Series.
# Використовується для доступу до рядків та/або стовпців за їхніми іменами

# обробка помилок 
# df.revenue = ['100a', '200', '300', '400']
# # print(df)
# # print(df.revenue.dtypes)
# df.revenue = pd.to_numeric(df.revenue, errors='coerce')
# # print(df)
# # print(df.describe())
# # print(df.revenue.dtypes)


# movies_df = pd.read_csv('data/movies_metadata.csv')
# # print(movies_df.to_string())

# pd.options.display.max_rows = 10
# print(pd.options.display.max_rows)