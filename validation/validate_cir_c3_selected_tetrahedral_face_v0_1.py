#!/usr/bin/env python3
import sympy as sp

x,y,z=sp.symbols("x y z", real=True)
rt3=sp.sqrt(3)
s=sp.Matrix([1,1,1])/rt3
U=[
    sp.Matrix([1,-1,-1])/rt3,
    sp.Matrix([-1,1,-1])/rt3,
    sp.Matrix([-1,-1,1])/rt3
]

for i in range(3):
    for j in range(3):
        assert sp.simplify(U[i].dot(U[j])-(1 if i==j else sp.Rational(-1,3)))==0
assert sp.simplify(U[0]+U[1]+U[2]+s)==sp.zeros(3,1)

X=sp.Matrix([x,y,z])
P=sp.expand(sp.prod([u.dot(X) for u in U]))
r2=x*x+y*y+z*z
lap=sp.diff(P,x,2)+sp.diff(P,y,2)+sp.diff(P,z,2)
H=sp.expand(P-r2*lap/10)
assert sp.simplify(sp.diff(H,x,2)+sp.diff(H,y,2)+sp.diff(H,z,2))==0

def dfact(n):
    if n<=0:return sp.Integer(1)
    o=sp.Integer(1)
    for k in range(n,0,-2):o*=k
    return o
def moment(exps):
    if any(e%2 for e in exps):return sp.Integer(0)
    a=[e//2 for e in exps]
    return sp.prod(dfact(2*q-1) for q in a)/dfact(2*sum(a)+1)
def avg(poly):
    pp=sp.Poly(sp.expand(poly),x,y,z)
    return sp.simplify(sum(c*moment(m) for m,c in pp.terms()))
def D(i,f):
    if i==0:return y*sp.diff(f,z)-z*sp.diff(f,y)
    if i==1:return z*sp.diff(f,x)-x*sp.diff(f,z)
    return x*sp.diff(f,y)-y*sp.diff(f,x)

norm=avg(H**2)
Q=sp.Matrix(3,3,lambda i,j:sp.simplify(avg(D(i,H)*D(j,H))/norm))
assert Q==sp.Matrix([[4,sp.Rational(78,41),sp.Rational(78,41)],
                    [sp.Rational(78,41),4,sp.Rational(78,41)],
                    [sp.Rational(78,41),sp.Rational(78,41),4]])
assert sp.simplify(Q*s-sp.Rational(320,41)*s)==sp.zeros(3,1)

Ds=sp.simplify((sp.diff(H,x)+sp.diff(H,y)+sp.diff(H,z))/rt3)
assert sp.simplify(sp.diff(Ds,x,2)+sp.diff(Ds,y,2)+sp.diff(Ds,z,2))==0
ratio=sp.simplify(avg(Ds**2)/avg(H**2))
assert ratio==sp.Rational(343,205)

# Joint C6 conditional power-ratio prediction.
pred=sp.simplify((sp.Rational(49,1)/(5*sp.sqrt(82))*sp.Rational(1,6))**2)
assert pred==sp.Rational(2401,73800)

print("PASS: C3-selected tetrahedral-face Gram, MAMD axis, translation coefficient, and conditional C6 power ratio.")
