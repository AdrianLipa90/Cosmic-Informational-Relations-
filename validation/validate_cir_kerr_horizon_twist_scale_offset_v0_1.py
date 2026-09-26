#!/usr/bin/env python3
import math

def delta_from_chi(chi):
    if not (0.0 <= chi < 1.0):
        raise ValueError("chi must lie in [0,1)")
    return chi/(12.0*math.sqrt(1.0-chi*chi))

def chi_from_delta(delta):
    if delta < 0.0:
        raise ValueError("delta must be nonnegative")
    u=12.0*delta
    return u/math.sqrt(1.0+u*u)

for chi in (0.0,0.1,0.5,0.9,0.99,0.999):
    back=chi_from_delta(delta_from_chi(chi))
    assert abs(back-chi)<2e-14,(chi,back)

# Kerr algebra check in dimensionless form.
for chi in (0.0,0.2,0.7,0.95):
    M=1.0
    a=chi*M
    root=math.sqrt(M*M-a*a)
    rp=M+root
    rm=M-root
    denom=rp*rp+a*a
    Omega=a/denom
    kappa=(rp-rm)/(2.0*denom)
    if chi==0.0:
        assert Omega==0.0
    else:
        want=chi/math.sqrt(1.0-chi*chi)
        assert abs(Omega/kappa-want)<1e-13

n_cont=2.561074230987091
delta=n_cont-2.0
chi=chi_from_delta(delta)
assert abs(chi-0.989149412559955)<1e-15

print("PASS: Kerr horizon twist ratio, spin-offset map and inverse.")
