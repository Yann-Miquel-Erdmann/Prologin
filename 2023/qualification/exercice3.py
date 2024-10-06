def pas_malindrome(mot:str):
    chiffres = [char for char in mot if char.isnumeric()]
    majuscules = [char for char in mot if char.isupper()]
    minuscules = [char for char in mot if char.islower()]

    if chiffres[:len(chiffres)//2] != chiffres[len(chiffres) - len(chiffres)//2:][::-1]:
        return False
    
    if majuscules[:len(majuscules)//2] != majuscules[len(majuscules) - len(majuscules)//2:][::-1]:
        return False

    if minuscules[:len(minuscules)//2] != minuscules[len(minuscules) - len(minuscules)//2:][::-1]:
        return False
    
    return True


count = 0
for i in range(int(input())):
    if pas_malindrome(input()):
        count+=1


print(count)
