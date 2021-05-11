import time
#from reader import feed

tic = time.perf_counter()

def is_prime(num):
    flag = False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if not flag:
        print(num, "is  a prime number")

for n in range(2, 29):
    is_prime(n)

toc = time.perf_counter()

print(f"time: {toc - tic:0.04f} seconds")




