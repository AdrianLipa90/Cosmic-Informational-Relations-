#!/usr/bin/env python3
import math
import numpy as np

def exterior_polar_root(chi):
    roots=np.roots([1.0,-3.0,chi*chi,chi*chi])
    rp=1.0+math.sqrt(1.0-chi*chi)
    cand=[float(z.real) for z in roots if abs(z.imag)<1e-10 and z.real>rp+1e-10]
    if len(cand)!=1:
        raise AssertionError((chi,roots,rp,cand))
    return cand[0]

def C_of_lambda(lam):
    l2=lam*lam
    return math.sqrt(
        63.0*(3.0*l2+2.0)**2
        /
        (5.0*(20.0*l2**3+9.0*l2**2+12.0*l2+4.0))
    )

def delta_n(chi):
    return chi/(12.0*math.sqrt(1.0-chi*chi))

# Endpoints.
assert abs(exterior_polar_root(0.0)-3.0)<1e-12
for chi in np.linspace(0.0,0.999999,200):
    x=exterior_polar_root(float(chi))
    # photon cubic
    assert abs(x**3-3*x*x+chi*chi*(x+1))<2e-10
    # eliminated chi identity
    assert abs(chi*chi-x*x*(3-x)/(x+1))<2e-10
    D=x*x-2*x+chi*chi
    lam=x/math.sqrt(D)
    lam2_alt=x*(x+1)/(2*(x-1))
    assert abs(lam*lam-lam2_alt)<2e-10
    assert 1.70<lam<1.74
    assert 1.50<C_of_lambda(lam)<1.56

x_ext=exterior_polar_root(0.999999999)
assert abs(x_ext-(1+math.sqrt(2)))<2e-4

C0=C_of_lambda(math.sqrt(3))
assert abs(C0-1.5187183066676861)<1e-14

for n in (1,2,3,4):
    R0=C0*(2.0**(-n))
    assert R0>0
    # high-spin branch is suppressed by divergent delta_n
    R_hi=C_of_lambda(
        exterior_polar_root(0.999999)/
        math.sqrt(exterior_polar_root(0.999999)**2
                  -2*exterior_polar_root(0.999999)
                  +0.999999**2)
    ) * 2.0**(-n-delta_n(0.999999))
    assert R_hi<R0

print("PASS: polar Kerr photon radius, source lambda, and two-parameter forward family.")
