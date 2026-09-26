#!/usr/bin/env python3
import math

def N(l):
    return math.sqrt(math.factorial(l+2)/math.factorial(l-2))

for l in range(2,20):
    lhs=(N(l+1)/N(l))**2
    rhs=(l+3)/(l-1)
    assert abs(lhs-rhs) < 1e-12

expected={
    2:25/7,
    3:7/3,
    4:21/11,
}
for l,val in expected.items():
    ratio=((l+3)/(l-1))*((2*l+1)/(2*l+3))
    assert abs(ratio-val)<1e-14,(l,ratio,val)

for n in range(1,20):
    q=2.0**(-n)
    p32=(25/7)*q*q
    qback=math.sqrt((7/25)*p32)
    nback=-math.log2(qback)
    assert abs(qback-q)<1e-15
    assert abs(nback-n)<1e-13

print("PASS: spin-2 tidal harmonic normalization and dyadic power ladder.")
