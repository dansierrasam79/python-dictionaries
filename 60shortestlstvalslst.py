#shortest list of values in list
init_dict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
init_list = []
final_list = []
for key,value in init_dict.items():
    init_list.append(len(value))

for key, value in init_dict.items():
    if len(value) == min(init_list):
        final_list.append([key,value])
print(final_list)


