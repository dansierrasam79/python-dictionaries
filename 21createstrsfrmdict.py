#create strings from dict
init_dict = {'1':['a','b'], '2':['c','d']}
init_list = list(init_dict.values())
init_list2 = []
final_list = []
for item in init_list2:
    final_string = ""
    for item2 in init_list2:
        final_string = item + item2
        final_list.append(final_string)
print(final_list)
