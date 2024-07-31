#find 3 largest values
init_dict = {'a':1, 'e':5, 'c':3, 'd':4, 'b':2, 'f':6}
sorted_list = list(init_dict.values())
sorted_list.sort()
final_dict = {}
for item in sorted_list[-3:]:
    for k,v in init_dict.items():
        if item == v:
            final_dict[k] = v
print(final_dict)
