#!/usr/bin/env python3
import math

def P0(x): return 1.0
def P1(x): return x
def P2(x): return 0.5*(3*x*x-1)
def P3(x): return 0.5*(5*x*x*x-3*x)

# Verify the truncated coefficients of the exact generating function by
# numerical Legendre projection for several epsilon values.
def kernel(mu,e):
    return 1.0/math.sqrt(1.0-2.0*e*mu+e*e)

def integrate(f,n=200000):
    # midpoint rule on [-1,1], deterministic
    h=2.0/n
    s=0.0
    for i in range(n):
        x=-1.0+(i+0.5)*h
        s+=f(x)
    return s*h

Ps=[P0,P1,P2,P3]
for e in (0.05,0.2,0.5,0.8):
    for ell,P in enumerate(Ps):
        g=(2*ell+1)/2.0*integrate(lambda x: kernel(x,e)*P(x),n=20000)
        target=e**ell
        if abs(g-target) > 2e-7:
            raise SystemExit(f'FAIL epsilon={e} ell={ell} got={g} target={target}')

print('PASS: Green-shadow Legendre coefficients g_l = epsilon^l for l=0..3.')
