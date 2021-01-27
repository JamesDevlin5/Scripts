#!/usr/bin/env python3


def Sieve(n):
    # A value prime[i] will be false if i is not a prime, and true otherwise
    prime = [True for _ in range(n+1)]
    p = 2
    while (p*p <= n):
        if (prime[p]):
            # Update all multiples
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    # Print primes
    for p in range(2, n+1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    n = 200
    print(f"Primes smaller than {n}:")
    Sieve(n)
