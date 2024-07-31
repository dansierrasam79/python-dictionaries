# find length of dict of values
init_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
final_dict = {}
for key,value in init_dict.items():
    final_dict[key] = len(value)
print(final_dict)
    
