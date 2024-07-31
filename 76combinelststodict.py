#combine two list
init_list = ['a', 'b', 'c', 'd', 'e', 'f']
init_list2 = [1, 2, 3, 4, 5]
final_dict = {}
for i in range(len(init_list)):
    try:
        final_dict[init_list[i]] = init_list2[i]
    except:
        print("Extra keys available.Ignore")
print(final_dict)
