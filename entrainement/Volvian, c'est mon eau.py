prix = int(input())
paye = int(input())
montant = paye - prix
count = 0
liste = [200,100,50,20,10,5,2,1]

for elem in liste:
    count+=montant//elem
    montant = montant%elem

print(count)