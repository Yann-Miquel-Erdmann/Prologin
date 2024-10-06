carburant = int(input())
mini = int(input())
nb = int(input())
liste = list(map(int,input().split(" ")))


total = 0
for elem in liste:
    ajout = elem*mini
    if elem <=20 and ajout>40:
        ajout = 40
    elif elem >=80 and ajout > 120:
        ajout = 120
    
    total+=ajout

if total <= carburant:

    print(total)
else:
    print(-1)