# convert lists to dictionary
init_list = ['S001', 'S002', 'S003', 'S004']
init_list2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
init_list3 = [85, 98, 89, 92]
final_dict = {}
final_list = []
final_lst = []
final_dict2 = {}

for i in range(0,len(init_list2)):
    final_dict2[init_list2[i]] = init_list3[i]
    final_list.append(final_dict2)
    final_dict2 = {}

for j in range(0, len(init_list)):
    final_dict[init_list[j]] = final_list[j]
    final_lst.append(final_dict)
    final_dict = {}
print(final_lst)

