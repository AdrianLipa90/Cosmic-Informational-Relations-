#!/usr/bin/env python3
import numpy as np
import math

V=np.array([
 [ 1, 1, 1],
 [ 1,-1,-1],
 [-1, 1,-1],
 [-1,-1, 1],
],dtype=float)/math.sqrt(3.0)

s=V[0]
P=[]
for v in V[1:]:
    p=v-np.dot(s,v)*s
    p=p/np.linalg.norm(p)
    P.append(p)
P=np.array(P)

# Tangent and 120-degree separation.
assert np.max(np.abs(P@s))<1e-14
for i in range(3):
    for j in range(3):
        want=1.0 if i==j else -0.5
        assert abs(float(P[i]@P[j])-want)<1e-14

# Construct the 120-degree rotation around s using Rodrigues.
theta=2*math.pi/3
K=np.array([
 [0,-s[2],s[1]],
 [s[2],0,-s[0]],
 [-s[1],s[0],0]
])
R=np.eye(3)*math.cos(theta)+(1-math.cos(theta))*np.outer(s,s)+math.sin(theta)*K

# It permutes the three tangent directions.
perm=[]
for p in P:
    rp=R@p
    dots=P@rp
    perm.append(int(np.argmax(dots)))
    assert np.max(dots)>1-1e-12
assert sorted(perm)==[0,1,2]

# No nonzero tangent fixed vector: kernel of (R-I) restricted to tangent plane is zero.
# Full R has one fixed axis, exactly span{s}.
w,vec=np.linalg.eig(R)
fixed=np.where(np.abs(w-1)<1e-10)[0]
assert len(fixed)==1
u=np.real(vec[:,fixed[0]])
u/=np.linalg.norm(u)
assert abs(abs(float(u@s))-1.0)<1e-12

print("PASS: C3 has no nonzero tangent invariant and the D3/tetrahedral tangent candidates form one threefold orbit.")
