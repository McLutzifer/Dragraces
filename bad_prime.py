"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return false
        else:
            print(i)

is_prime(20)
"""


# Program to check if a number is prime or not

num = 29


flag = False


for i in range(2, num):
    if (num % i) == 0:
        flag = True
        break
if not flag:
    print(num, "is  a prime number")

