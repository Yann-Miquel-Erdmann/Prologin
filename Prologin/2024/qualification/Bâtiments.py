
from typing import List


def batiments2(n: int, r: int, k: int, villes: List[int]) -> None:
    """
    :param n: le nombre de villes
    :param r: le nombre de mouvements du serpent
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville
    """
    # TODO Afficher le nombre de bâtiments cassés à chaque ville après les $R$
    # mouvements sous la forme d'une suite d'entiers séparés par des espaces.

    villes_final = villes.copy()
    big = max(villes)
    for i in range(n):
        
        if 1+((r-i-1)//n+1) * (k-1) > n:
            villes_final[i] = big
            continue

        villes_final[i] = max(villes[i:i+1+((r-i-1)//n+1) * (k-1)])
        if i+1+((r-i-1)//n+1) * (k-1) > n:
            if 1+((r-i-1)//n+2) * (k-1) > n:
                villes_final[i] = big
                continue

            m_2=  max(villes[0:(i+1+((r-i-1)//n+2) * (k-1))%n])
    
            if m_2 > villes_final[i]:
                villes_final[i] = m_2
    
    # print(" ".join(list(map(str, villes_final))))

    return villes_final
    

def batiment3(n: int, r: int, k: int, villes: List[int]) -> None:
    """
    :param n: le nombre de villes
    :param r: le nombre de mouvements du serpent
    :param k: le nombre de villes impliquées dans chaque mouvement
    :param villes: le nombre de bâtiments cassés dans chaque ville
    """
    # TODO Afficher le nombre de bâtiments cassés à chaque ville après les $R$
    # mouvements sous la forme d'une suite d'entiers séparés par des espaces.


    for i in range(r):
        # if i%n == 0:
        #     print(" ".join(list(map(str, villes))))


        indice = i%n
        villes[indice] = max(villes[i%n:i%n+k])
        if i%n+k > n:
            m=  max(villes[0:(i%n+k)%n])
    
            if m > villes[indice]:
                villes[indice] = m
        
        
    
    # print(" ".join(list(map(str, villes))))
    return villes
       


if __name__ == "__main__":
    import time
    import random


    # n = int(input())
    # r = int(input())
    # k = int(input())
    # villes = list(map(int, input().split()))

    res = True
    i =0
    while res:

        n = 100_000
        r = 10_000_000
        k = 100
        villes = [random.randint (0, n) for i in range(n)]
        villes_1 = batiments(n, r, k, villes)
        # villes_2 = batiments2(n, r, k, villes)

        # res = villes_1 == villes_2
        i +=1

        print(i)


