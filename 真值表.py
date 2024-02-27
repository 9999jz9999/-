# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:17:29 2024

@author: kkjj1
"""

import pandas as pd

# 生成真值表
truth_table = pd.DataFrame({
    'P': ['F','F', 'T', 'T'],
    'Q': ['F','T', 'F', 'T']
})

# 定义逻辑运算函数
def logical_and(p, q): #∧
    return 'T' if p == 'T' and q == 'T' else 'F'

def logical_or(p, q): #∨
    return 'T' if p == 'T' or q == 'T' else 'F'

def logical_xor(p, q): #⊕
    return 'T' if (p == 'T' and q == 'F') or (p == 'F' and q == 'T') else 'F'

def logical_xnor(p, q): #≡
    return 'T' if (p == 'T' and q == 'T') or (p == 'F' and q == 'F') else 'F'

def logical_if(p, q): #→
    return 'T' if p == 'F' or q == 'T' else 'F'

def logical_iff(p, q): #↔
    return 'T' if p == q else 'F'

# 应用逻辑运算并生成结果表
result_table = pd.DataFrame()
result_table['P'] = truth_table['P']
result_table['Q'] = truth_table['Q']
result_table['P ∧ Q'] = [logical_and(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]
result_table['P ∨ Q'] = [logical_or(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]
result_table['P ⊕ Q'] = [logical_xor(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]
result_table['P ≡ Q'] = [logical_xnor(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]
result_table['P → Q'] = [logical_if(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]
result_table['P ↔ Q'] = [logical_iff(p, q) for p, q in zip(truth_table['P'], truth_table['Q'])]

# 删除重复行
result_table.drop_duplicates(inplace=True)

# 格式化输出结果表
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
print(result_table)

