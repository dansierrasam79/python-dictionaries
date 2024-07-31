# count vals in dict
init_dict = [{'a':1, 'b':2}, {'c':3, 'd':4}, {'e':5, 'f':6}, {'a':3, 'e':3}]
final_list = []
final_dict = {}
for ind_dict in init_dict:
    for key, value in ind_dict.items():
        final_list.append([key,value])
print(final_list)
for lst in final_list:
    total = 0
    for lst2 in final_list:
        if lst[0] == lst2[0]:
            total += lst2[1]
    final_dict[lst[0]] = total
print(final_dict)
