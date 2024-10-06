
from typing import List


def alignement(n: int, rayons: List[int]) -> None:
    mx =0
    res = []
    for idx,rayon in enumerate(rayons):
        if rayon>=mx:
            res.append(0)
            mx = rayon
        else:
            i = idx-1
            if rayons[i] == rayon:
                i = res[i]-1
                
            while i!= 0: 
                if rayons[i] == rayon:
                    i = res[i]-1
                    break 
                elif rayons[i] > rayon:
                    break
                
                else:
                    i = res[i]-1

                

            


            
            res.append(i+1)
    print(" ".join(map(str,res)))


if __name__ == "__main__":
    n = int(input())
    rayons = list(map(int, input().split()))
    # import random
    # n = 10
    # rayons = [random.randint(1,n)for i in range(n,0,-1)]
    # print(rayons)
    alignement(n, rayons)
