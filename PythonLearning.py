# %%
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import random
# import twstock
import pandas as pd
import io
import datetime
# import xmath
# import xmath as math
import traceback
import sys
import requests


# def helloPython(inputStr):
#     output = "Hello "+inputStr+" !"
#     print(output)
#     x = [1, 2, 3]
#     y = [4, 5, 6]
#     zipped = zip(x, y)
#     print(list(zipped))
#     x2, y2 = zip(*zip(x, y))
#     print(x2+y2)
#     # import func--------
#     max = xmath.max(10, 5)
#     min = xmath.min(4, 10)
#     sum = xmath.sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
#     print(max)
#     print(min)
#     print(sum)
#     print(math.e)

# traceback---------
# try:
#     inputNum = int(input("input number :"))
#     print("{0} is {1}".format(inputNum, "one" if inputNum % 2 else "two"))
# except ValueError:
#     print("pls input the numbers")
# except (EOFError, KeyboardInterrupt):
#     print("out of system!")
# except:
#     print("system error")


# def gcd(m, n):
#     if n == 0:
#         return m
#     else:
#         return gcd(n, m % n)

# use lambda like java switch


# def lambdaFunc(errorMsg):
#     def max(m, n): return m if m > n else n
#     print(max(10, 3))
#     score = int(input('Pls input the score：'))
#     level = score
#     {
#         10: lambda: print("Perfect"),
#         9: lambda: print('A'),
#         8: lambda: print('B'),
#         7: lambda: print('C'),
#         6: lambda: print('D')
#     }.get(level, lambda: print(errorMsg))()


# helloPython("Ryan")

# print(gcd(20, 30))         # show 10
# print(type(gcd))           # show <class 'function'>

# gcd2 = gcd
# print(gcd2(20, 30))        # show 10
# print(id(gcd), id(gcd2))   # show two same number

# lambdaFunc("The exam has not pass")


# def stockSearchById(stockId):
#     now = int(datetime.datetime.now().timestamp())+86400
#     url = "https://query1.finance.yahoo.com/v7/finance/download/" + stockId + \
#         "?period1=0&period2=" + \
#         str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
#     response = requests.post(url)

#     f = io.StringIO(response.text)
#     df = pd.read_csv(f, index_col='Date', parse_dates=['Date'])

#     return df


# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# plt.close('all')
# f, ax = plt.subplots()
# ax.plot(x, y)

# stock = twstock.Stock("2330")
# print(stock.price[-5:])
# print(stock.high[-5:])
# stockRealTime = twstock.realtime.get("2330")
# print(stockRealTime)
# stocks = twstock.realtime.get(['2330', '2337', '2409'])
# stocks['success']
# print(stocks)

# df = stockSearchById("2376.TW")
# df.Close.plot()


# list1 = ['cat', 'dog', 'bird']
# list1.remove('dog')
# print(list1)

# ansNum = random.randint(1, 10)
# print("guess a number between 1 and 10 in 5 times")
# for guessTime in range(1, 6):
#     guess = int(input("input the number : "))
#     if guess < ansNum:
#         print("too low")
#     elif guess > ansNum:
#         print("too high")
#     else:
#         print("got it!")
#         break
# print("times over")

ser = pd.Series([1, 2, 3, 4, "zz"])
# print(ser.values)
# print(ser.index)
# # 判斷有沒
# print(1 in ser)

# dictionary = {"name": "Kirito", "sex": "man", "skill": "C8763"}
# print(dictionary["name"], "_", dictionary["skill"], "\n")
# obj = pd.Series(dictionary)
# print(obj)

data = {'name': ['Bob', 'Nancy', 'Amy', 'Elsa', 'Jack'],
        'year': [1998, 1995, 1994, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day': [11, 23, 8, 3, 11]}
# 沒有years欄位會自動補NaN
myframe = pd.DataFrame(data, columns=["name", "day", "month", "year"])
# luckynumber = ['3', '2', '1', '7', '8', '100']
# luckynumber = pd.Series(luckynumber)
# # 用key的方式給值
# myframe["years"] = luckynumber
# print(myframe)

# dataFrame操作
# df = pd.DataFrame(np.random.randn(4, 2))
# print(df)
# selectFm = myframe["name"] != "Amy"
# selectFm2 = myframe["name"].isin(["Amy"])
# print(myframe[selectFm])
# print(myframe[selectFm2])
# isnull = myframe["name"].isnull()
# print(isnull)
# notnull = myframe["name"].notnull()
# print(notnull)
# betweenApi = myframe["year"].between(1995, 1997)
# print(myframe[betweenApi])

# inplace=True屬性，直接修改原本物件，False -> 創建一個新的物件，預設為False
newFrame = myframe.set_index("name", inplace=True)
# print(myframe)
# print(newFrame)
# 將index回覆為原本的
# myframe.reset_index(inplace=True)
# print(myframe)
# loc 拿index的key
# print(myframe.loc["Bob"])
# 取得單一欄位的值
# print(myframe.loc["Bob", "year"])
# iloc 拿原本index的值 int
# print(myframe.iloc[0])
# myframe.reset_index(inplace=True)
# print(myframe.loc[0])

fortune1 = pd.read_csv(r"C:\PythonSpace\file1.csv")
sectors = fortune1.groupby('col2').sum()

# print(sectors)


pd.core.common.is_list_like = pd.api.types.is_list_like

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)
data = web.DataReader('F', 'iex', start, end)
print(data)
# data.plot(y="Close")
data[["close", "high", "low"]].plot()
