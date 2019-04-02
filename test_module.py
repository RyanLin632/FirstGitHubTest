# from moduleLib import m_first
# import moduleLib.m_first as lib
# import moduleLib.m_second
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# from sklearn import datasets

# moduleLib.m_second.m2()
# m_first.m1()
# lib.m1()

# X, y = datasets.make_regression(
#     n_samples=200, n_features=1, n_targets=1, noise=10)
# model = LinearRegression()
# model.fit(X, y)
# predict = model.predict(X[:200, :])
# plt.plot(X, predict, c="red")
# plt.scatter(X, y)
# plt.show()


# import time
# import threading


# def decrement(n):
#     while n > 0:
#         n -= 1


# start = time.time()
# decrement(100000000)
# cost = time.time() - start
# print("one thread : ", cost)

# start2 = time.time()

# t1 = threading.Thread(target=decrement, args=[50000000])
# t2 = threading.Thread(target=decrement, args=[50000000])
# t1.start()  # 啟動執行緒，執行任務
# t2.start()  # 同上

# t1.join()  # 主執行緒阻塞，直到t1執行完成，主執行緒繼續往後執行
# t2.join()  # 同上

# cost2 = time.time() - start2
# print("two thread", cost2)

# start3 = time.time()
# t1 = threading.Thread(target=decrement, args=[25000000])
# t2 = threading.Thread(target=decrement, args=[25000000])
# t3 = threading.Thread(target=decrement, args=[25000000])
# t4 = threading.Thread(target=decrement, args=[25000000])

# t1.start()
# t2.start()
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()

# cost3 = time.time() - start3

# print(cost3)

# from testName import testFun

# testFun()

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="123456", db="gocrud")

db.query("select * from employee")
# r=db.store_result()  取出整個resultset，如結果太大會有問題
# ...or...
# r=db.use_result() 一次取指定數量的row
r = db.use_result()
print(r.fetch_row(10))
