
from typing import List


def le_plus_grand_saut(n: int, differences: List[int]) -> None:
    height = 0
    max_up = 0
    max_up_lock = 0
    max_height = 0

    for i in range(n):
        height += differences[i]
        
        if differences[i] > max_up:
            max_up = differences[i]
        
        if height > max_height:
            max_up_lock = max_up
            max_height= height
    
    print(max_up_lock)



if __name__ == "__main__":
    n = int(input())
    differences = list(map(int, input().split()))
    le_plus_grand_saut(n, differences)
