#sort list in dict
init_dict = {'a':[3,2,1], 'b':[6,5,4], 'c':[8,7,9]}
final_dict = {}
for key, value in init_dict.items():
    final_dict[key]=sorted(value)
print(final_dict)    
