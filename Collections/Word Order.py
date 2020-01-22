from collections import OrderedDict

words_count = int(input())

words_dict = OrderedDict()

for i in range(0,words_count):
    word = input()
    if(words_dict.__contains__(word)):
        words_dict[word] +=1
    else:
        words_dict.update({word:1})


print(len(words_dict))
for k,v in words_dict.items():
    print(v,end=' ')