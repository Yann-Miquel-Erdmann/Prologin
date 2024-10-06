nb_accroches = int(input())
stabilisateurs = int(input())
stabilite_parfaite = int(input())
accroches = list(map(int, input().split(" ")))

accroches.sort()

desequilibres = []
for i in range(nb_accroches-3):
    desequilibres.append(stabilite_parfaite-(accroches[i]-accroches[i+3])**2)


zone = len(desequilibres)// stabilisateurs
if len(desequilibres)%stabilisateurs != 0:
    zone+=1
if zone < 4:
    zone = 4



def getbest(id, n):
    if n > stabilisateurs:
        return 0
    if len(desequilibres) - (id+(zone-1))>0:
        liste = []
        ajout = len(desequilibres)-((stabilisateurs-n)*4)
        if ajout < id+4:
            ajout = id+4
        for i in range(id, ajout):
            b = getbest(i+4, n+1)
            if b< 0:
                b = 0
            if desequilibres[i] < 0:
                liste.append(0+b)
            else:
                liste.append(desequilibres[i]+b)
        m  = max(liste)
        if m<0:
            return 0
        else:
            return m
    else:
        if id <= len(desequilibres)-1:
            m =  max(desequilibres[id:])
            if m< 0:
                return 0
            else: return m
        else:
            return 0    

print(getbest(0,1))