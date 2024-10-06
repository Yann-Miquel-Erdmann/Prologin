from typing import List

def trier_une_file(n: int, m: int, file: List[int]) -> None:
    count = 0
    for a in range(n-1):
        for i in range(n-1-a):
            if file[i] > file[i+1]:
                count+=1
                file[i],file[i+1] = file[i+1],file[i]
    print(count)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    file = list(map(int, input().split()))

    trier_une_file(n, m, file)