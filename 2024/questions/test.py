dico = {1: None}
for i in dico:
    print i
    del dico[i]
    dico[i + 1] = None