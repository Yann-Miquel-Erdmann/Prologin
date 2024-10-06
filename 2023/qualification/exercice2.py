nombre_de_restes = int(input())

restes = list(map(int, input().split(" ")))
boites = list(map(int, input().split(" ")))


restes.sort()
boites.sort()

count = 0
decalage = 0
i = 0
while i <=nombre_de_restes-1:
    if restes[i-decalage] <= boites[i]:
        count+=1
    else:
        decalage+=1
    i+=1
print(count)
