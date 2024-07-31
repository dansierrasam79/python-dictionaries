#add values for common keys
init_dict = {'a': 100, 'b': 200, 'c':300}
init_dict2 = {'a': 300, 'b': 200, 'd':400}
final_dict = {}
for k,v in init_dict.items():
    for k2,v2 in init_dict2.items():
        if k == k2:
            final_dict[k] = v+v2
        if k not in final_dict.keys():
            final_dict[k] = v
        if k2 not in final_dict.keys():
            final_dict[k2] = v2
print(final_dict)
