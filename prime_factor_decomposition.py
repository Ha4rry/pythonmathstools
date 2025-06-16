def is_prime(x):
    primelist = [2]
    if x < 2:
        return False
    if x == 2:
        return True
    for n in range(3,x+1):
        divisible = False
        for prime in primelist:
            if n % prime == 0:
                divisible = True
                break
        if n != x:
            if not divisible:
                primelist.append(n)
        elif n == x:
            return not divisible
        
def first_prime_factor(x):
    for i in [o for o in list(range(2,x+1)) if is_prime(o)]:
        if x % i == 0:
            return i


def prime_factor_decomposition(x):
    # part 1 - finding them
    if is_prime(x):
        return f"{x}"
    if x <= 1:
        return None
    primes = []
    non_prime = x
    non_prime_present = True
    while non_prime_present:
        fpf=first_prime_factor(non_prime)
        primes.append(fpf)
        non_prime_present = not is_prime(int(non_prime/fpf))
        if not non_prime_present:
            
            primes.append(int(non_prime/fpf))
        non_prime = int(non_prime/fpf)
        
    # part 2 - making them look good
    counts = {}
    result_strings = []
    for i in primes:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for key, val in counts.items():
        if val != 1:
            result_strings.append(f"{key}^{val}")
        else:
            result_strings.append(f"{key}")
    return " × ".join(result_strings)

for i in range(0,10000):
    print(f"{i} --- {prime_factor_decomposition(i)}")
