#map values of given list to dict
def square_function(val):
    return val * val

init_list = [1,2,3,4,5]
final_dict = {}
for item in init_list:
    result = square_function(item)
    final_dict[item] = result
print(final_dict)
