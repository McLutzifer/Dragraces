def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return false
        else:
            print(i)

is_prime(20)