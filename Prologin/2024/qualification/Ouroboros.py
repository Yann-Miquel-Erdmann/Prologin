from typing import List
from sys import stdout
class new_ville():
    def __init__(self,nom,id, prec):
        self.nom = nom
        self.id= id
        self.prec = prec


def situation_finale(n: int, m: int, villes: List[str], actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr
    """
    # TODO Afficher, sur une ligne par ville, la liste des villes qui seront
    # rencontrées lors du Ragnarök, dans l'ordre, en partant de la queue de
    # Jörmungandr jusqu'à sa tête.
    
    # boucle chainée 
    first = new_ville(villes[0], 0, None)
    ville_itr = first
    for i in range(1,n):
        ville_itr = new_ville(villes[i], i, ville_itr)
        ville_itr.prec.suiv = ville_itr
    
    ville_itr.suiv=first
    first.prec=ville_itr

    sens = True
    ville = first
    pile = []
    for action in actions:

        if action == "A":
            if sens:
                ville = ville.suiv
            else:
                ville = ville.prec
        if action == "R":
            sens = not sens

            if sens:
                ville = ville.suiv
            else:
                ville = ville.prec

        if action == "M":
            pile.append(ville)

            ville.suiv.prec = ville.prec
            ville.prec.suiv = ville.suiv
            
            if sens:
                ville = ville.suiv
            else:
                ville = ville.prec


        if action == "C":
            temp = pile.pop()

            if sens:
                temp.suiv = ville
                temp.prec = ville.prec
                ville.prec.suiv = temp
                ville.prec = temp
            else:
                temp.suiv = ville.suiv
                temp.prec = ville
                ville.suiv.prec = temp
                ville.suiv = temp
            
            ville = temp


    
    # afffichage de la boucle chainée
    id = ville.id
    print(ville.nom)
    if sens:
        ville = ville.suiv
    else:
        ville = ville.prec

    while ville.id != id:
        stdout.write(ville.nom + "\n")
        if sens:
            ville = ville.suiv
        else:
            ville = ville.prec



    

    
    


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
  
    # n = 100000
    # m = 2000000
    # villes = [str(i) for i in range(n)]
    # actions = "".join(["MRAC" for i in range(int(m/4))]) 

    situation_finale(n, m, villes, actions)
