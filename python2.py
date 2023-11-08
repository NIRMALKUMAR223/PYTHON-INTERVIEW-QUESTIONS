def newtonsqrt(n,howmany):
    approx=0.5*n
    for i in range(howmany):
        betterapprox=0.5*(approx+n/approx)
        approx=betterapprox
    return betterapprox
print("Newton sqrt value is",newtonsqrt(10,3))
print("Newton sqrt value is",newtonsqrt(10,5))
print("Newton sqrt value is",newtonsqrt(10,10))
