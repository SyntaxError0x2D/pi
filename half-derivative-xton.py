from math import factorial
from tqdm import tqdm
h = 0.0000001
N = 12
def f(x): return(x**N)
s = 0
ak = 1
acc = 10**(-15)
for k in tqdm(range(0, int(1/h))):
    rs = (-1)**k * ak * f(1-k*h)
    #print(rs)
    if abs(rs) < acc: break
    s += rs
    ak *= (1/2 - k)/(k+1)
HD = s*h**(-1/2)
pi = (4**N * factorial(N)**2 / (factorial(2*N) * HD))**2
print(pi)
