
from typing import List
# from bisect import insort

def test_prog(prog):
    global max_len, po, pf, liens
    to_visit = [([], 0)]
    if len(prog) == 0:
        print("VALIDE")
        return
    while len(to_visit):
        pile, index = to_visit.pop()
        for i in range(min(max_len, len(prog)-index)):
            if prog[index:index+i+1] in po:
                p2 = pile.copy()
                p2.append(prog[index:index+i+1])
                to_visit.append((p2, index+i+1))

            elif prog[index:index+i+1] in pf:
                if len(pile) == 0:
                    # print("break len")
                    break
                # print("check",liens[prog[index:index+i+1]], pile[-1])
                if liens[prog[index:index+i+1]] == pile[-1]:
                    p2 = pile.copy()
                    p2.pop()
                    if len(p2) == 0 and index+i+1 == len(prog):
                        print("VALIDE")
                        return
                    else:
                        to_visit.append((p2, index+i+1))
                        

      
    else:
        print("INVALIDE")
        return

def phrases_valides(
    n: int,
    parentheses_ouvrantes: List[str],
    parentheses_fermantes: List[str],
    q: int,
    programmes: List[str],
) -> None:
    global max_len, po, pf, liens

    liens = {parentheses_fermantes[i]:parentheses_ouvrantes[i] for i in range(n)}
    pf = set(parentheses_fermantes)
    po = set(parentheses_ouvrantes)
    max_len = max(max(list(map(len,parentheses_ouvrantes))),max(list(map(len,parentheses_fermantes))))

    for prog in programmes:
        test_prog(prog)




if __name__ == "__main__":
    n = int(input())
    parentheses_ouvrantes = [input() for _ in range(n)]
    parentheses_fermantes = [input() for _ in range(n)]
    q = int(input())
    programmes = [input() for _ in range(q)]
    phrases_valides(n, parentheses_ouvrantes,
                    parentheses_fermantes, q, programmes)
