import re


pattern  =  '[(e|a|i|o|u|y|A|E|I|O|U|Y)]{2,}'

input_str = input()

res = re.findall(pattern,input_str)

print(res)