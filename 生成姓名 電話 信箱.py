# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

last_name = ['李', '王', '張', '劉', '陳', '楊', '黃', '趙', '周', '吳', \
              '徐', '孫', '朱', '馬', '胡', '郭', '林', '何', '高', '梁', \
              '鄭', '羅', '宋', '謝', '唐', '韓', '曹', '許', '鄧', '蕭', \
              '馮', '曾', '程', '蔡', '彭', '潘', '袁', '於', '董', '餘', \
              '蘇', '葉', '呂', '魏', '蔣', '田', '杜', '丁', '沈', '姜', \
              '範', '江', '傅', '鐘', '盧', '汪', '戴', '崔', '任', '陸', \
              '廖', '姚', '方', '金', '邱', '夏', '譚', '韋', '賈', '鄒', \
              '石', '熊', '孟', '秦', '閻', '薛', '侯', '雷', '白', '龍', \
              '段', '郝', '孔', '邵', '史', '毛', '常', '萬', '顧', '賴', \
              '武', '康', '賀', '嚴', '尹', '錢', '施', '牛', '洪', '龔']

first_name = ['家豪', '志明', '建宏', '俊傑', '俊宏', '志豪', '志偉', '承翰', '冠字', '志強',
             '淑芬', '淑惠', '美玲', '麗華', '美惠', '淑貞', '雅婷', '秀英', '淑娟', '秀琴']

for _ in range(10):
    result_first_name = random.choice(first_name)
    result_last_name = random.choice(last_name)
    result_name = result_last_name + result_first_name
    print(result_name)
    print()
    
#_________________________________________________________

import random

for _ in range(10):
    number = random.randint(10000000,99999999)
    print(f"09{number}")
    print()
    
#_________________________________________________________

import random
import string

min_length = 6
max_length = 30

allowed_characters = string.ascii_lowercase + string.digits

for _ in range(10):

    length = random.randint(min_length, max_length)
    mailbox_name = ''.join(random.choices(allowed_characters, k=length))
    print(f"{mailbox_name}@gmail.com")
    print()

