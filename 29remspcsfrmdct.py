#remove spaces from keys in dict
init_dict = {'a ':1, 'b':2, 'c ':3, 'd':4, ' e':5, 'f':6}
final_dict = {}
for key,value in init_dict.items():
    final_dict[key.strip()] = value
print(init_dict)
print(final_dict)
