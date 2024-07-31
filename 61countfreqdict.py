#freq of dict
from collections import Counter as cnt
init_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
init_list = []
for key,value in init_dict.items():
    init_list.append(value)
cnt = cnt(init_list)
print(cnt)
