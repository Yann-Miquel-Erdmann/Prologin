
from typing import List


def compteur_de_fleurs(champ: List[str]) -> None:
    """
    :param champ: la liste des fleurs dans le champ
    """
    count = 0
    for i in range(len(champ)-2):
        if champ[i:i+3] == "BJR":
            count+=1
    
    print(count)


if __name__ == "__main__":
    champ = input()
    compteur_de_fleurs(champ)
