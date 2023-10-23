# %%
# import psycopg2
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
sns.set(color_codes=True)


# %%
# conn = psycopg2.connect(
#     dbname="analiz",
#     user="postgres",
#     password="123123",
#     host="127.0.0.1"
# )


# %%
# query = "SELECT * FROM mtcars;"
# df = pd.read_sql_query(query, conn)

df = pd.read_csv('mtcars.csv', sep=',')

# %%
print(len(df))
print(df.head())
#print(len(df)) - Это выводит количество строк в вашем фрейме данных df.
#print(df.head()) - Это выводит первые 5 строк вашего фрейма данных df для предварительного просмотра данных.
# %%

max_cars = df[df['qsec'] == df['qsec'].min()]
print('Самая медленный машина:')
print(min_cars)
#Найдет медленную машину в списке
# %%
max_cars = df[df['disp'] == df['disp'].min()]
print('Объем')
print(max_cars)
#Найдет обьем медленную машину в списке

# %%
df.shape
#df.shape - Эта строка кода используется для получения размерности (количества строк и столбцов) фрейма данных 
# %%
df.dtypes
#Эта строка кода возвращает типы данных (dtype) для каждого столбца во фрейме данных df. 
# %%
df.shape
duplicate_rows_df = df[df.duplicated()]
print(f"Количество дубликатов: {duplicate_rows_df.shape}")
#Этот код позволяет вам найти и вывести количество дубликатов во фрейме данных df и его размерность.

# %%
df.count()
#df.count() - Эта строка кода возвращает количество непустых (непропущенных) значений в каждом столбце фрейма данных df

# %%
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)
#Выводит сообщение о количестве дубликатов и их размерности в новом фрейме данных 


# %%
df = df.drop(['model'], axis=1)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
#Выводит значения межквартильных диапазонов для всех числовых столбцов во фрейме данных df.

# %%
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape
#Код выполняет фильтрацию данных во фрейме данных df на основе межквартильного диапазона (IQR) и выводит размерность (количество строк и столбцов) результата. 
# %%
plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c
#Код создает тепловую карту корреляции для числовых столбцов во фрейме данных df с использованием библиотеки для визуализации данных
# %%

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['hp'], df['qsec'])
ax.set_xlabel('HP')
ax.set_ylabel('Qsec')
plt.show()
#Код создает график рассеяния для столбцов 'hp' и 'qsec' из фрейма данных df
# %%
conn.close()
# %%