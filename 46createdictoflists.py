#create a dict of lists
init_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
init_dict = {}
for item in init_list:
    temp_list = []
    for item2 in init_list:
        if item[0] == item2[0]:
            temp_list.append(item2[1])
    init_dict[item[0]]=temp_list
print(init_dict)
