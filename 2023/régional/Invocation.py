debuts = [input() for _ in range(int(input()))]
vocabulaire = [input() for _ in range(int(input()))]


# import time

# t = time.perf_counter()


sorts =set()
for voc in vocabulaire:
    for voc2 in vocabulaire:
        if len(voc)*2 + len(voc2) <= 60:
            sorts.add(voc+voc2+voc)

for debut in debuts:
    ct = 0
    for sort in sorts:
        if sort.startswith(debut):
            ct+=1
    print(ct)


# print(time.perf_counter()-t)




# t = time.perf_counter()

# for debut in debuts:
#     ct = 0
#     for voc in vocabulaire:
#         if voc.startswith(debut):
#             ct+=len(vocabulaire)
#         else:
#             for voc2 in vocabulaire:
#                 if (voc+voc2+voc).startswith(debut):
#                     ct+=1
    
#     print(ct)

# print(time.perf_counter()-t)
