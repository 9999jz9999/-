# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from datetime import datetime

# 讀取數據文件
data = pd.read_csv("data.csv")

# 將birthday轉換為日期時間對象
data['birthday'] = pd.to_datetime(data['birthday'])

# 獲取當前日期
current_date = datetime.now()

# 計算年齡
data['years-old'] = current_date.year - data['birthday'].dt.year

# 輸出結果
print(data)

#___________________________________________________
import pandas as pd

# 定義函數來確定星座
def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return '白羊座'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return '金牛座'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return '雙子座'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return '巨蟹座'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return '獅子座'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return '處女座'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return '天秤座'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return '天蠍座'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return '射手座'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return '摩羯座'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '水瓶座'
    else:
        return '雙魚座'

# 讀取數據文件
data = pd.read_csv("data.csv")

# 將birthday轉換為日期時間對象
data['birthday'] = pd.to_datetime(data['birthday'])

# 從生日中提取月份和日期
data['month'] = data['birthday'].dt.month
data['day'] = data['birthday'].dt.day

# 計算星座
data['zodiac_sign'] = data.apply(lambda x: get_zodiac_sign(x['month'], x['day']), axis=1)

# 刪除中間生成的月份和日期列
data = data.drop(columns=['month', 'day'])

# 輸出結果
print(data)
