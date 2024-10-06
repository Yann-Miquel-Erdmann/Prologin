from typing import List


def koios(nombre_d_etoiles: int, constellation: List[List[int]]) -> None:
    matrix = np.array(constellation)
    matrix = matrix_power(matrix,3)
    print(np.trace(matrix)//6) 


if __name__ == "__main__":
    nombre_d_etoiles = int(input())
    constellation = [list(map(int, input().split())) for _ in range(nombre_d_etoiles)]
    koios(nombre_d_etoiles, constellation)
