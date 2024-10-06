
from typing import List
from bisect import insort


def pions(n: int, valeurs: List[int], m: int, plateau: List[List[int]]) -> None:
    pos = [set() for _ in range(10)]

    couts = [[[[10**16 for _ in range(m)] for _ in range(m)] for _ in range(m)] for _ in range(m)]
    for y in range(m):
        for x in range(m):
            pos[plateau[y][x]-1].add((x,y))
            to_visit = [(0,x,y,set())]
            while len(to_visit) != 0:
                elem_c, elem_x, elem_y, elem_v  = to_visit.pop()
                if elem_c >= couts[y][x][elem_y][elem_x]:
                    continue
                
                couts[y][x][elem_y][elem_x] = elem_c 

                if elem_c == 0:
                    elem_c = 1

                elem_v.add((elem_x,elem_y))
                

                for ox, oy in [(1,0), (0,-1), (-1,0), (0,1)]:
                    if 0<=elem_x+ox<m and 0<=elem_y+oy<m:
                        if (elem_x+ox, elem_y+oy) not in elem_v:
                            insort(
                                to_visit, (elem_c*plateau[elem_y+oy][elem_x+ox], elem_x+ox, elem_y+oy, elem_v.copy()), key=lambda x: -x[0])


    liste_pos = [(0,[(0,0),(0,0),(0,0)],0)]

    if all(map(lambda x: len(pos[x-1]) != 0, valeurs)):
        while len(liste_pos)!= 0:
            pc,pl,pi = liste_pos.pop()
            # print(pc,pl,pi)
            if pi == n:
                print(pc) 
                return

            
            
            for i in range(3):
                # if plateau[pl[i][1]][pl[i][1]] == valeurs[pi]:
                #     insort(liste_pos, (pc,[pl[index] for index in range(3)], pi+1), key=lambda x: -x[0])
                #     break

                if i!= 0 and pl[i] == pl[i-1]:
                    break

                for (ax,ay) in pos[valeurs[pi]-1]:
                    insort(liste_pos, (pc+couts[pl[i][1]][pl[i][0]][ay][ax], 
                                       [pl[index] if index != i else (ax, ay) for index in range(3)]
                           , pi+1),key=lambda x: -x[0])

    else:
        print(-1)


    
    """
    :param n: le nombre de tours
    :param valeurs: la liste des valeurs à visiter
    :param m: la taille de chaque côté du plateau
    :param plateau: le plateau de jeu
    """
    # TODO Afficher le coût minimal pour réaliser cette tâche ou -1 si ce n'est
    # pas possible.
    pass


if __name__ == "__main__":
    n = int(input())
    valeurs = list(map(int, input().split()))
    m = int(input())
    plateau = [list(map(int, input().split())) for _ in range(m)]
    pions(n, valeurs, m, plateau)
