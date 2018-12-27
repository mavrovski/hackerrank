from collections import OrderedDict

ord_dict = OrderedDict()

for _ in range(int(input())):
    item,space,quantity = input().rpartition(' ')
    ord_dict[item]=ord_dict.get(item,0)+int(quantity)
for item,quantity in ord_dict.items():
    print(item,quantity)