#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact tetrahedral vectors scaled by sqrt(3); dot products are checked
# using integer numerators divided by 3.
V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]

# Sum zero.
assert all(sum(v[j] for v in V)==0 for j in range(3))

# Gram: diagonal 1, off-diagonal -1/3.
for i,a in enumerate(V):
    for j,b in enumerate(V):
        dot=Fraction(sum(a[k]*b[k] for k in range(3)),3)
        assert dot==(Fraction(1,1) if i==j else Fraction(-1,3))

# Second moment sum v v^T = 4/3 I.
for i in range(3):
    for j in range(3):
        x=Fraction(sum(v[i]*v[j] for v in V),3)
        assert x==(Fraction(4,3) if i==j else Fraction(0,1))

# Uniform S^2 even monomial moments.
def odd_df(n):
    if n<=0: return 1
    p=1
    for k in range(n,0,-2): p*=k
    return p

def sphere_moment(a,b,c):
    # E[x^(2a)y^(2b)z^(2c)].
    num=odd_df(2*a-1)*odd_df(2*b-1)*odd_df(2*c-1)
    den=odd_df(2*(a+b+c)+1)
    return Fraction(num,den)

# H3=xyz.
H2=sphere_moment(1,1,1)
assert H2==Fraction(1,105)

# D_s H3=(xy+xz+yz)/sqrt(3).
# Cross terms integrate to zero by parity.
D2=Fraction(1,3)*(sphere_moment(1,1,0)+sphere_moment(1,0,1)+sphere_moment(0,1,1))
assert D2==Fraction(1,15)
assert D2/H2==7

# Translation descendants:
# D_s^2 H3 = 2/3 (x+y+z), D_s^3 H3=2/sqrt(3).
# D_s H3 = (3 z_s^2-r^2)/(2 sqrt(3)) follows from
# 3 z_s^2-r^2=2(xy+xz+yz).
# Numerical shell inversion sanity.
for n in range(1,20):
    q=2.0**(-n)
    # choose arbitrary parent amplitude and R
    R=3.7
    A3=2.5*R**3*math.sqrt(float(H2))
    A2=2.5*(q*R)*R**2*math.sqrt(float(D2))
    q_back=A2/(math.sqrt(7.0)*A3)
    assert abs(q_back-q)<1e-14
    n_back=-math.log2(q_back)
    assert abs(n_back-n)<1e-12

print("PASS: tetrahedral moments, sqrt(7) translation scale bridge, and dyadic inversion.")
