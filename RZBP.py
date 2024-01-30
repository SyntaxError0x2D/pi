def sqrt(n, lim = 500) -> float:
    sqrt2 = 1.4142135623730950488 # precomputed const
    pw2 = int(n).bit_length()
    a = 2 << (pw2 >> 2)
    if pw2 & 1: a *= sqrt2
    for _ in range(lim): a -= a/2 - n/(2*a) 
    return(a)

def sieve(l) -> list:
    # returns the list of all prime numbers til l
    nums = [True for i in range(l-1)]
    trgt = int(l**(1/2))+1
    for indx in range(trgt):
        n = indx +2 ; r = 1
        if nums[indx] == False: continue
        while indx + n * r < len(nums):
            nums[indx + n*r] = False
            r+=1
    primes = []
    for i in range(l-1):
        if nums[i]: primes.append(i+2)
    return(primes)

def pi_(acc = 500):
    pL = sieve(acc) # list of primes
    pi = 1 # initialized
    for p in pL: pi *= (1 - (1/(p*p)) ) # the fun part
    pi = sqrt(6/pi)
    return(pi)
    