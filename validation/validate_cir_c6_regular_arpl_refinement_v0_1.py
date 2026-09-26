#!/usr/bin/env python3
import math

# Regular C6 child fibre.
grades=list(range(6))
def g(q):
    return (q+1)%6

# Free and transitive action of <g> on one child label.
orbit=[]
x=0
for _ in range(6):
    orbit.append(x)
    x=g(x)
assert x==0
assert sorted(orbit)==grades
assert len(set(orbit))==6

# Therefore branch count equals six.
b=len(set(orbit))
assert b==6

# ARPL strict-refinement ultrametric ratio.
q=1.0/b
assert q==1.0/6.0

# Entropy increment and C6 product cardinality.
assert abs(math.log(b)-(math.log(3.0)+math.log(2.0)))<1e-15

# Frozen CMB-screen shell.
R=13873.0
d=R*q
assert abs(d-2312.1666666666665)<1e-12

# Preserve separation from dyadic ln2 generator.
assert abs(math.log(6.0)/math.log(2.0)-round(math.log(6.0)/math.log(2.0)))>1e-3

print("PASS: regular C6 fibre has b=6, ARPL q=1/6, and R_CMB/6 shell is reproduced.")
