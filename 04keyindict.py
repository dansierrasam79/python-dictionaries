# key exists in dict
final_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
does_exist =  False
key2 = 10
for key, value in final_dict.items():
    if key == key2:
        does_exist = True
        break;
    else:
        does_exist = False
if does_exist:
    print("Key exists in dict")
else:
    print("Key does not exist in dict")
