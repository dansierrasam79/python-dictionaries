#remove duplicates from dict
init_dict = {'a':1, 'b':2, 'c':1, 'd':4, 'e':1, 'f':1}
final_dict = {}
for k,v in init_dict.items():
    if v not in final_dict.values():
        final_dict[k] = v
print(final_dict)
