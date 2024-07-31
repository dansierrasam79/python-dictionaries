#create list of tuples
init_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
final_list = []
for key,value in init_dict.items():
    final_list.append((key,value))
print(final_list)
