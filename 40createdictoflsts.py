#create dict of lists
init_list = ['x','y','z']
init_list2 = [list(range(11,20)),list(range(21,30)),list(range(31,40))]
final_dict = {}
for i in range(0,len(init_list)):
    final_dict[init_list[i]] = init_list2[i]
print(final_dict)
