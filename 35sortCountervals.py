#sort Counter by value
from collections import Counter
init_list = {'Math':81, 'Physics':83, 'Chemistry':87}
cnt = Counter(init_list)
print(cnt.most_common())
