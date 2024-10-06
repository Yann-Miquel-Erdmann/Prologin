nom = input()


liste = []
for i in range(int(input())):
    n = input()
    if len(n) == len(nom):
        score = 0
        for i in range(len(n)):
            if n[i] == nom[i]:
                score+=1
        
        liste.append((score,n))

print(max(liste,key=lambda x: x[0])[1])