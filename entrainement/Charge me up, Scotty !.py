cote = int(input())
R = range(cote)
matrix = [input() for i in range(cote)]


def search(x,y):
    tosearch = [(x,y)]
    visited = set()
    count = 0
    while len(tosearch) != 0:
        s = tosearch.pop(0)
        m = matrix[s[1]][s[0]]

        if m == ".":
            continue

        if m == "C":
            count+=6
            continue
    
        if s in visited:
            continue

        visited.add(s)

        if m == "P" or m == "+":
            for i in [-1,1]:
                m = (s[0]+i,s[1])
                if m[0] in R and m[1] in R:
                    if m not in visited:
                        tosearch.append(m)
            for j in [-1,1]:
                m = (s[0],s[1]+j)
                if m[0] in R and m[1] in R:
                    if m not in visited:
                        tosearch.append(m)
    
    return count

mx = 0
for x in R:
    for y in R:
        if matrix[y][x] == "P":
            res = search(x, y)
            if res>mx:
                mx = res


print(mx)

        

                
        