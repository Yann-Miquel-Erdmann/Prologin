aimes = list(set([input() for i in range(6)]))
detestes = list(set([input() for i in range(6)]))

nombre = len(aimes)
for elem in detestes:
    if elem in aimes:
        nombre-=1

print(nombre)
