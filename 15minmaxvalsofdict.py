# return keys of min and max values in dict
init_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
all_values = [value for value in init_dict.values()]
max_key = [key for key,value in init_dict.items() if value == max(all_values)]
min_key = [key for key,value in init_dict.items() if value == min(all_values)]
print(max_key[0],min_key[0])
#Outputs f and a

