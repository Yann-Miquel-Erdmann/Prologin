
from typing import List


def contenu_dechiffre(n: int, contenu: str, occurences: List[int]) -> None:
    """
    :param n: le nombre de caractères gravés sur la stèle
    :param contenu: le texte gravé sur la stèle
    :param occurences: la liste contenant les nombres d'occurrences des lettres de A à Z
    """
    occ = [0  for i in range(26)]
    for e in contenu:
        occ[ord(e)-ord("a")] += 1

    for i in range(26):
        indice = occ.index(occurences[i])
        contenu = contenu.replace(chr(indice+ ord("a")), chr(i+ ord("A")))

    print(contenu)



if __name__ == "__main__":
    n = int(input())
    contenu = input()
    occurences = list(map(int, input().split()))
    contenu_dechiffre(n, contenu, occurences)
