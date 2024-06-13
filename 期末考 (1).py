# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#第一題

from datetime import datetime, timedelta

# 取得今日 timestamp
today_timestamp = datetime.now().timestamp()
print("今日 timestamp:", today_timestamp)

# timestamp轉換為時間格式
today_time = datetime.fromtimestamp(today_timestamp)
print("今日時間:", today_time)

# 顯示今日
print("今日:", today_time.strftime("%Y-%m-%d"))

# 顯示昨日
yesterday = today_time - timedelta(days=1)
print("昨日:", yesterday.strftime("%Y-%m-%d"))

# 顯示昨日timestamp
yesterday_timestamp = yesterday.timestamp()
print("昨日 timestamp:", yesterday_timestamp)

# 字串轉換為時間格式
date_str = "2024-06-05"
date_time = datetime.strptime(date_str, "%Y-%m-%d")
print("字串轉換為時間格式:", date_time)

# 時間格式轉換為字串
time_str = today_time.strftime("%Y-%m-%d %H:%M:%S")
print("時間格式轉換為字串:", time_str)

# 將今天顯示 YYMMDD的日期
YYMMDD = today_time.strftime("%y%m%d")
print("今天顯示 YYMMDD的日期:", YYMMDD)

# 計算明年你的生日是星期幾
next_birthday = datetime(2005 + 1, 5, 12)
print("明年你的生日是星期幾:", next_birthday.strftime("%A"))

# 將你的生日顯示為西元年與中華民國年
birth_date = datetime(2005, 5, 12)
print("你的生日(西元年):", birth_date.strftime("%Y-%m-%d"))
print("你的生日(中華民國年):", birth_date.strftime("%Y-%m-%d").replace(str(2005), str(2005 - 1911)))


#___________________________________________________________________________________________________________________
#第二題
#a
import matplotlib.pyplot as plt
import numpy as np

# 定義一個函數來繪製不同的函數圖形
def plot_function(ax, func, x_range, title):
    x = np.linspace(*x_range, 400)
    y = func(x)
    ax.plot(x, y)
    ax.set_title(title)
    ax.grid(True)

# 創建子圖
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

# 定義函數
functions = [
    (np.sin, (-2 * np.pi, 2 * np.pi), "y = sin(x)"),
    (np.cos, (-2 * np.pi, 2 * np.pi), "y = cos(x)"),
    (np.tan, (-2 * np.pi, 2 * np.pi), "y = tan(x)"),
    (np.exp, (-2, 2), "y = exp(x)"),
    (np.log, (0.1, 10), "y = log(x)"),
    (np.sqrt, (0, 10), "y = sqrt(x)"),
    (np.square, (-3, 3), "y = x^2"),
    (lambda x: x**3, (-3, 3), "y = x^3"),
    (np.abs, (-10, 10), "y = |x|")
]

# 繪製每個函數的圖形
for ax, (func, x_range, title) in zip(axs.flat, functions):
    plot_function(ax, func, x_range, title)

# 調整子圖之間的間距
plt.tight_layout()

# 顯示圖像
plt.show()



#b
import matplotlib.pyplot as plt
import numpy as np

# 定義一個函數來繪製不同的函數圖形
def plot_function(ax, func, x_range, title):
    x = np.linspace(*x_range, 400)
    y = func(x)
    ax.plot(x, y)
    ax.set_title(title)
    ax.grid(True)

# 創建一個 2x5 的子圖
fig, axs = plt.subplots(5, 2, figsize=(12, 15))

# 定義不同的函數
functions = [
    (np.sin, (-2 * np.pi, 2 * np.pi), "y = sin(x)"),
    (np.cos, (-2 * np.pi, 2 * np.pi), "y = cos(x)"),
    (np.tan, (-2 * np.pi, 2 * np.pi), "y = tan(x)"),
    (np.exp, (-2, 2), "y = exp(x)"),
    (np.log, (0.1, 10), "y = log(x)"),
    (np.sqrt, (0, 10), "y = sqrt(x)"),
    (np.square, (-3, 3), "y = x^2"),
    (lambda x: x**3, (-3, 3), "y = x^3"),
    (np.abs, (-10, 10), "y = |x|"),
    (np.sinh, (-2 * np.pi, 2 * np.pi), "y = sinh(x)")
]

# 繪製每個函數的圖形
for ax, (func, x_range, title) in zip(axs.flat, functions):
    plot_function(ax, func, x_range, title)

# 調整子圖之間的間距
plt.tight_layout()

# 顯示圖像
plt.show()


#___________________________________________
#第三題


import numpy as np

# 函數
def f(x):
    return np.sin(x)

# 積分區間
a = 0
b = 1

# 生成隨機點
N = 1000000  # 生成數量
x_random = np.random.uniform(a, b, N)

# 計算平均
f_values = f(x_random)
f_mean = np.mean(f_values)

# 估計
integral_estimate = (b - a) * f_mean

print(f"估計的積分值為：{integral_estimate}")


#______________________________
#第四題
S = 12240036
#a
print(S)
#b
octal_number = oct(S)

print(octal_number)
#c
binary_number = bin(S)

print(binary_number)
#d
hexadecimal_number = hex(S)

print(hexadecimal_number)
#e
hex_str = format(S, 'x').upper()

print(hex_str)
#f
formatted_string = f"{S:>20}"

print(formatted_string)
#g
import math

pi = math.pi
pi_value = "{:.6f}".format(pi)
print(pi_value)
#h
import math

e_value = math.e

formatted_string_1 = f"{'0'*5}{e_value:.6f}"

print(formatted_string_1)
#i
import math

e_to_pi = math.exp(math.pi)

formatted_string_2 = f"{'0'*3}{e_to_pi:.3f}"

print(formatted_string_2)

#j
import pandas as pd

# 创建DataFrame
df = pd.DataFrame({
    'Description': ["學號10進位", "學號8進位", "學號2進位","學號16進位-數字","學號16進位-字串","學號右側填空","pi小數點後6位"
                    ,"e","e**pi"],
    'Result': [S, octal_number, binary_number,hexadecimal_number,hex_str,formatted_string,pi_value,formatted_string_1,formatted_string_2]
})

# 将DataFrame保存为Excel文件
df.to_excel('results.xlsx', index=False)
