import time


t = time.time()
R = range(1000000)
count=0
for i in range(10000000):
    if i//2+i**2 in R:
        count+=1
print(count)
print(time.time()-t)


t = time.time()
R = range(1000000)
count=0
for i in range(10000000):
    if i//2+i**2>=0 and i//2+i**2<1000000:
        count+=1
print(count)
print(time.time()-t)
