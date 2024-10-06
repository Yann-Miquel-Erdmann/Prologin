P = int(input())
D = int(input())

mn = (int(input()))

lst = input().replace(" ", "").split("1")

count = 0

for elem in lst:
    if len(elem) >= mn:
        count+=len(elem)

if count >= D:
    print(1)
else:
    print(0)