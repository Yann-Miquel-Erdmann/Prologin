nombre = int(input())
redirections = list(map(int, input().split(" ")))
import sys
# import random
# nombre  = 20000
# redirections = list(range(2,nombre+1))  # suivi
# redirections.append(1)
# print(len(redirections))
# redirections = [random.choice(list(range(1,n)) + list(range(n+1, nombre+1))) for n in range(1,nombre+1)]  # random

resultats = [0 for i in range(nombre)]

# print(redirections)

def func(initial,red,visites,setvisites):
    for _ in range(nombre):
        # print(initial , _)
        if resultats[red-1]!=0:
            for i,elem in enumerate(resultats[red-1]):
                if elem in setvisites:
                    visites = visites+resultats[red-1][:i]
                    resultats[initial]= visites


                    # print("get visites",initial ,red, visites, setvisites)

                    if resultats[visites[1]-1] == 0:
                        any(setvisites.add(x) for x in resultats[red-1][:i])
                        setvisites.remove(visites[0])
                        return [True, visites[1:], setvisites]
                    else:
                        return [False]
            else:
                visites = visites+resultats[red-1]
                any(setvisites.add(x) for x in resultats[red-1])
                red = redirections[visites[-1]-1] 


        if red in setvisites:
            resultats[initial] = visites
            # print("loop visites",initial ,red, visites, setvisites)
            if resultats[visites[1]-1] == 0:
                setvisites.remove(visites[0])
                return [True, visites[1:], setvisites]
            else:
                return [False]
        else:
            visites.append(red)
            setvisites.add(red)
            red = redirections[red-1]


import time
t = time.time()
for initial, red in enumerate(redirections):
    if resultats[initial] != 0:
        continue
    else:
        visites = [initial+1]
        setvisites = {initial+1}

        res = func(initial,red,visites,setvisites)
        for i in range(nombre):
            if res[0] == True:
                res = func(res[1][0]-1, redirections[res[1][-1]-1], res[1], res[2])
            else:
                continue



# t1 = time.time()-t
# # print(resultats)
# sys.stdout.write(" ".join(map(str , map(len, resultats)))+"\n") 
# print(t1)
# print(time.time()-t)



