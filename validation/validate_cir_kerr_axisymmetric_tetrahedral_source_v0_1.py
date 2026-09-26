#!/usr/bin/env python3
import sympy as sp

x,y,z,lam=sp.symbols("x y z lam", positive=True)
s=sp.Matrix([1,1,1])/sp.sqrt(3)
I=sp.eye(3)
Finv=I+(1/lam-1)*(s*s.T)
v=sp.Matrix([x,y,z])
u=sp.simplify(Finv*v)
P=sp.expand(u[0]*u[1]*u[2])
r2=x*x+y*y+z*z
lap=sp.diff(P,x,2)+sp.diff(P,y,2)+sp.diff(P,z,2)
H=sp.expand(P-r2*lap/10)
Ds=sp.simplify((sp.diff(H,x)+sp.diff(H,y)+sp.diff(H,z))/sp.sqrt(3))

def dfact(n):
    if n<=0: return sp.Integer(1)
    out=sp.Integer(1)
    for k in range(n,0,-2): out*=k
    return out

def moment(exps):
    if any(e%2 for e in exps): return sp.Integer(0)
    aa=[e//2 for e in exps]
    return sp.prod(dfact(2*q-1) for q in aa)/dfact(2*sum(aa)+1)

def avg(poly):
    pp=sp.Poly(sp.expand(poly),x,y,z)
    return sp.simplify(sum(c*moment(m) for m,c in pp.terms()))

NH=sp.factor(avg(H**2))
ND=sp.factor(avg(Ds**2))
want_H=(20*lam**6+9*lam**4+12*lam**2+4)/(4725*lam**6)
want_D=(3*lam**2+2)**2/(375*lam**6)
assert sp.simplify(NH-want_H)==0
assert sp.simplify(ND-want_D)==0

C2=sp.factor(ND/NH)
want_C2=63*(3*lam**2+2)**2/(5*(20*lam**6+9*lam**4+12*lam**2+4))
assert sp.simplify(C2-want_C2)==0
assert sp.simplify(C2.subs(lam,1)-7)==0
assert sp.limit(C2,lam,sp.oo)==0
assert sp.limit(C2,lam,0,dir="+")==sp.Rational(63,5)

# Kerr ADM algebra.
M,a,r,th=sp.symbols("M a r th", positive=True)
Sigma=r**2+a**2*sp.cos(th)**2
Delta=r**2-2*M*r+a**2
A=(r**2+a**2)**2-a**2*Delta*sp.sin(th)**2
g_tphi=-2*M*a*r*sp.sin(th)**2/Sigma
g_phiphi=A*sp.sin(th)**2/Sigma
beta=sp.simplify(g_tphi/g_phiphi)
assert sp.simplify(beta + 2*M*a*r/A)==0
alpha2=sp.simplify(Delta*Sigma/A)

# Polar local relative triad anisotropy.
lambda_polar=sp.simplify(
    sp.sqrt(Sigma.subs(th,0)/Delta)
    /
    (sp.sqrt(Sigma.subs(th,0))/r)
)
assert sp.simplify(lambda_polar-r/sp.sqrt(Delta))==0

print("PASS: axisymmetric tetrahedral C(lambda) and Kerr ADM source formulas.")
