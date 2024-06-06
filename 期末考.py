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

import matplotlib.pyplot as plt
import numpy as np

# 設置 x 範圍
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# 創建子圖
fig, axes = plt.subplots(3, 3, figsize=(12, 12))

# 定義一些函數
functions = [np.sin, np.cos, np.tan, np.exp, np.log, np.arctan, np.sqrt, np.square, lambda x: np.abs(x)]

# 繪製函數圖
for i in range(3):
    for j in range(3):
        ax = axes[i, j]
        if i*3 + j < len(functions):
            ax.plot(x, functions[i*3 + j](x))
            ax.set_title(functions[i*3 + j].__name__)
        ax.axis('off')

# 刪除最後一張圖
axes[2, 2].remove()

# 調整子圖間距
plt.tight_layout()

# 顯示圖形
plt.show()
