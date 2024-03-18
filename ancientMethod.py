from math import sqrt
intCos = 0.5 #yay!


def getCos(n : int):
    if n == 0: return(intCos)
    return( sqrt( (1+getCos(n-1))/2 ) )

def getSin(cos):
    sin = sqrt(1-(cos**2))
    return(sin)

def pi_(n):
    if type(n) != int or n < 0: return(False)
    s = 6*(2**n)
    cos = getCos(n)
    sin= getSin(cos)
    lp = sqrt( (1-cos)/2 )
    li = ((1-cos)/sin)
    dp = s * lp ; di = s * li
    return( (dp+di)/2 )

print(pi_(2))
