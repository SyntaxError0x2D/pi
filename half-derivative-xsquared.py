h = 0.000001
def f(x): return(x**2)
s = 0
ak = 1
for k in range(0, int(1/h)):
    s += (-1)**k * ak * f(1-k*h)
    ak *= (1/2 - k)/(k+1)
HD = s*h**(-1/2)
pi = 64/9 * HD**(-2)
print(pi)
