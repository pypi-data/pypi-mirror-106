def prime_number(n):
    primes = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(f"El número {i} es primo")
            primes += 1

    return primes
