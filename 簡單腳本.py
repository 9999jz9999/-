# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:46:41 2024

@author: kkjj1
"""

def collect_user_data():
    # 讓用戶輸入個人資料
    name = input("請輸入您的姓名: ")
    age = int(input("請輸入您的年齡: "))
    height = float(input("請輸入您的身高（米）: "))
    favorite_color = input("請輸入您喜愛的顏色: ")
    
    # 將個人資料存儲在字典中
    user_data = {
        "姓名": name,
        "年齡": age,
        "身高": height,
        "喜愛的顏色": favorite_color
    }
    
    return user_data

def format_user_summary(user_data):
    # 格式化個人資料摘要
    summary = (
        f"{user_data['姓名']}, "
        f"{user_data['年齡']}歲, "
        f"身高{user_data['身高']}米, "
        f"喜愛的顏色是{user_data['喜愛的顏色']}。"
    )
    
    return summary

def main():
    # 收集用戶資料
    user_data = collect_user_data()
    
    # 格式化並輸出個人資料摘要
    summary = format_user_summary(user_data)
    print(summary)

if __name__ == "__main__":
    main()
