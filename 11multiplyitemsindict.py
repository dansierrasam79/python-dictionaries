#multiply all items in a dict
init_dict = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}

prod_keys, prod_values = 0,0

for key,value in init_dict.items():
    prod_keys += key
    prod_values += value

print(prod_keys, prod_values)
