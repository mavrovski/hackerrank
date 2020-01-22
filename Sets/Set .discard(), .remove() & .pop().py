set_length = int(input())
main_set = set(map(int,input().split()))
commands_count = int(input())
command = ""
number = ""
for i in range(commands_count):
    args = list(input().split())
    if len(args)==1:
        command  = args[0]
    else:
        command=args[0]
        number=int(args[1])
    if command == "pop":
        main_set.pop()
    if command == "remove":
        main_set.remove(number)
    if command == "discard":
        main_set.discard(number)

print(sum(list(main_set)))
