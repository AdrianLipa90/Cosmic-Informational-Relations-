#!/usr/bin/env python3
import math
import numpy as np

def vec(l,b):
    l=math.radians(l); b=math.radians(b)
    return np.array([
        math.cos(b)*math.cos(l),
        math.cos(b)*math.sin(l),
        math.sin(b)
    ],dtype=float)

def lb(v):
    v=v/np.linalg.norm(v)
    return (
        math.degrees(math.atan2(v[1],v[0]))%360.0,
        math.degrees(math.asin(v[2]))
    )

a2=vec(235.9,58.1)
a3=vec(237.7,62.9)
dot=float(np.clip(abs(a2@a3),-1.0,1.0))
gamma=math.acos(dot)
assert abs(math.degrees(gamma)-4.88065785521028)<1e-12

s=np.cross(a2,a3)
s=s/np.linalg.norm(s)
assert abs(float(a2@s))<1e-14
assert abs(float(a3@s))<1e-14

l,b=lb(s)
assert abs(l-137.65831979352447)<1e-12
assert abs(b-5.098818745494779)<1e-12

cond=1.0/math.sin(gamma)
assert abs(cond-11.753565170812795)<1e-12

# Exact aligned limit is singular.
assert np.linalg.norm(np.cross(a2,a2))<1e-15

print("PASS: two-tangent cross-product inversion and WMAP9 conditioning reproduced.")
