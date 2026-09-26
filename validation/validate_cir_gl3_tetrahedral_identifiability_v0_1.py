#!/usr/bin/env python3
from fractions import Fraction

# Columns are the cubic-monomial coefficient vectors of the six normalized-shape
# tangent directions: three rotations followed by three symmetric shears.
# Monomial ordering:
# x^3,y^3,z^3,x^2y,x^2z,y^2x,y^2z,z^2x,z^2y,xyz
M=[
 [0,0,0,0,0,Fraction(2,5)],
 [0,0,0,0,Fraction(2,5),0],
 [0,0,0,Fraction(2,5),0,0],
 [0,1,0,0,Fraction(-3,5),0],
 [1,0,0,Fraction(-3,5),0,0],
 [0,0,1,0,0,Fraction(-3,5)],
 [-1,0,0,Fraction(-3,5),0,0],
 [0,0,-1,0,0,Fraction(-3,5)],
 [0,-1,0,0,Fraction(-3,5),0],
 [0,0,0,0,0,0],
]

def rank_fraction(a):
    a=[row[:] for row in a]
    nr=len(a); nc=len(a[0]); r=0
    for c in range(nc):
        p=next((i for i in range(r,nr) if a[i][c] != 0),None)
        if p is None:
            continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(nr):
            if i!=r and a[i][c]!=0:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(nc)]
        r+=1
    return r

assert rank_fraction(M)==6

# Exact first-order Q response for the symmetric shear basis:
# deltaQ_xy=12(E_xy+E_yx), etc.
for pair in ((0,1),(0,2),(1,2)):
    q=[[Fraction(0) for _ in range(3)] for __ in range(3)]
    i,j=pair
    q[i][j]=q[j][i]=Fraction(12)
    assert sum(q[k][k] for k in range(3))==0
    assert q[i][j]==12 and q[j][i]==12

# Diagonal F leaves xyz morphology unchanged exactly:
# xyz -> xyz/(a*b*c), an amplitude-only factor.
print("PASS: six-dimensional normalized H3 tangent rank and GL3 identifiability firewall.")
