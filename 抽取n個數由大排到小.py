# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:36:36 2024

@author: kkjj1
"""

import random

def main():
    n = int(input("請輸入 n 的值: "))
    a = int(input("請輸入 a 的值: "))
    b = int(input("請輸入 b 的值: "))
    
    random_numbers = [random.randint(a, b) for _ in range(n)]
    
    # 刪除重複數字並排序
    unique_sorted_numbers = sorted(list(set(random_numbers)), reverse=True)
    
    print("隨機抽取且刪除重複的數字並由大到小排序後的結果:")
    print(unique_sorted_numbers)

if __name__ == "__main__":
    main()
