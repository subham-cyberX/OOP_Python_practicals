
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def primes_upto(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


def first_n_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


n = int(input("Enter a number n: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

print("Prime numbers up to", n, ":", primes_upto(n))
print("First", n, "prime numbers:", first_n_primes(n))
