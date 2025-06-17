def prime_factor_decomposition(x):
    if x < 2:
        return None
    # part 1 - pre compute primes for efficiency (I believe that this is still the most time consuming part of the algorithm.)
    precomputedprimes = [2]
    for i in list(range(3, (x+1)//2 +1)) + [x]:
        dv = False
        for p in precomputedprimes:
            if i % p == 0:
                dv = True
                break
        if not dv:
            precomputedprimes.append(i)
    if precomputedprimes[-1] == x:
        return f"{x}"
    #part 2 - decomposing time
    primes = []
    other = x
    non_prime_present = True
    while non_prime_present:
        fpf = None
        for p in precomputedprimes:
            if other % p == 0:
                fpf = p

        other = int(other/fpf)
        primes.append(fpf)
        non_prime_present = not other in precomputedprimes
        if not non_prime_present: 
            primes.append(other)
        
    
    # part 3 - making them look good
    counts = {}
    result_strings = []
    for i in sorted(primes):
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

print("PRIME FACTORISATION PROGRAM")
x = int(input("x?: "))
print(f"{prime_factor_decomposition(x)}")
