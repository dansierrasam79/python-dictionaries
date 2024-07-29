#sum items in dictionary
init_dict = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
total = 0
for key in init_dict.keys():
    total += key
print(total)
