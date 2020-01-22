from itertools import groupby





input_string = input()

output_string = []

for i,j in groupby(input_string):
    output_string.append((len(list(j)),int(i)))



print(*output_string,sep=' ')