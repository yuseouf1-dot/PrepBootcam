import random
import time

start = time.time()
list_random_integers = []

for i in range(1000000):
    list_random_integers.append(random.randint(1,10000000))

list_random_integers.sort()

print(time.time()-start)