nb_points = int(input())
nb_tuyaux = int(input())
refroidissement = int(input())
depart = int(input())
arrivee = int(input())

boucles = []
points = {i:[] for i in range(1,nb_points+1)}
res = []

func = lambda elem: points[elem[0]].append((elem[1],elem[2]))

for _ in range(nb_tuyaux):
   func(list(map(int, input().split(" "))))



def explore(point, explores,setexplores, chaleur,count, fin=False):
    
    if tuyau in setexplores:
        boucle = explores.index(point)
        return (False, )
    elif len(points[point]) == 0:
        if tuyau == arrivee:
            return (True,)
    
    else:
        setexplores.add(tuyau[0])
        explores.append(tuyau[0])
        chaleur.append[tuyau[2]]
        count+=1

        explore(tuyau, explores,setexplores, chaleur,count)
    



