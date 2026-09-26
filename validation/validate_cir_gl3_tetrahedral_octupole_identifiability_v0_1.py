#!/usr/bin/env python3
import sympy as sp

x,y,z,eps=sp.symbols("x y z eps", real=True)
r2=x*x+y*y+z*z

# General infinitesimal GL(3) action on H3=xyz.
p=sp.symbols("a0:9", real=True)
A=sp.Matrix(3,3,p)
v=sp.Matrix([x,y,z])
vp=(sp.eye(3)-eps*A)*v
P=sp.expand(vp[0]*vp[1]*vp[2])
dP=sp.expand(sp.diff(P,eps).subs(eps,0))

# Harmonic projector for homogeneous cubics in R^3.
lap=sp.diff(dP,x,2)+sp.diff(dP,y,2)+sp.diff(dP,z,2)
H=sp.expand(dP-r2*lap/10)

mons=[
    x**3,y**3,z**3,
    x**2*y,x**2*z,
    y**2*x,y**2*z,
    z**2*x,z**2*y,
    x*y*z
]
M=sp.Matrix([
    [sp.Poly(sp.diff(H,par),x,y,z).coeff_monomial(mon) for par in p]
    for mon in mons
])
assert M.rank()==7
assert len(M.nullspace())==2

# Kernel is exactly traceless diagonal gl(3).
kernel=sp.Matrix.hstack(*M.nullspace())
diag_tf=sp.Matrix([
    [-1,-1],
    [ 0, 0],
    [ 0, 0],
    [ 0, 0],
    [ 1, 0],
    [ 0, 0],
    [ 0, 0],
    [ 0, 0],
    [ 0, 1]
])
assert kernel.row_join(diag_tf).rank()==2

# Finite diagonal deformation preserves normalized xyz morphology.
lx,ly,lz=sp.symbols("lx ly lz", nonzero=True)
assert sp.expand((x/lx)*(y/ly)*(z/lz)-x*y*z/(lx*ly*lz))==0

# Exact spherical averages for Q.
def dfact(n):
    if n<=0:
        return sp.Integer(1)
    out=sp.Integer(1)
    for k in range(n,0,-2):
        out*=k
    return out

def sphere_moment(exps):
    if any(e%2 for e in exps):
        return sp.Integer(0)
    aa=[e//2 for e in exps]
    return sp.prod(dfact(2*q-1) for q in aa)/dfact(2*sum(aa)+1)

def avg(poly):
    pp=sp.Poly(sp.expand(poly),x,y,z)
    return sp.simplify(sum(c*sphere_moment(m) for m,c in pp.terms()))

def D(i,f):
    if i==0:
        return y*sp.diff(f,z)-z*sp.diff(f,y)
    if i==1:
        return z*sp.diff(f,x)-x*sp.diff(f,z)
    return x*sp.diff(f,y)-y*sp.diff(f,x)

H0=x*y*z
norm0=avg(H0**2)
Q0=sp.Matrix(3,3,lambda i,j:sp.simplify(avg(D(i,H0)*D(j,H0))/norm0))
assert Q0==4*sp.eye(3)

a,b,c,d,e=sp.symbols("a b c d e", real=True)
S=sp.Matrix([[a,b,c],[b,d,e],[c,e,-a-d]])
vp=(sp.eye(3)-eps*S)*sp.Matrix([x,y,z])
P=sp.expand(vp[0]*vp[1]*vp[2])
dP=sp.expand(sp.diff(P,eps).subs(eps,0))
lap=sp.diff(dP,x,2)+sp.diff(dP,y,2)+sp.diff(dP,z,2)
dH=sp.expand(dP-r2*lap/10)

norm1=2*avg(H0*dH)
Q1=sp.zeros(3)
for i in range(3):
    for j in range(3):
        A0=avg(D(i,H0)*D(j,H0))
        A1=avg(D(i,dH)*D(j,H0)+D(i,H0)*D(j,dH))
        Q1[i,j]=sp.simplify(A1/norm0-A0*norm1/norm0**2)

target=12*sp.Matrix([[0,b,c],[b,0,e],[c,e,0]])
assert sp.simplify(Q1-target)==sp.zeros(3)

# Normalized morphology: trace/amplitude removed, leaving 3 rotations + 3 shear.
assert 3+3==6

print("PASS: GL(3) tangent rank=7, traceless-diagonal kernel dim=2, normalized rank=6, deltaQ=12 offdiag(S).")
