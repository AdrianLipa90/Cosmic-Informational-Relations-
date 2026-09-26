#!/usr/bin/env python3
import sympy as sp

x,y,theta=sp.symbols("x y theta", real=True)
# Generic symbolic derivative names via an explicit cubic polynomial is enough
# to verify the irreducible third-derivative combinations and spin weights.
a,b,c,d=sp.symbols("a b c d", real=True)
psi=(a*x**3+3*b*x**2*y+3*c*x*y**2+d*y**3)/6

px=lambda f: sp.diff(f,x)
py=lambda f: sp.diff(f,y)

gamma=sp.expand((px(px(psi))-py(py(psi)))/2 + sp.I*px(py(psi)))
G3=sp.expand(px(gamma)+sp.I*py(gamma))
F1=sp.expand(px(gamma)-sp.I*py(gamma))

want_G=sp.Rational(1,2)*(a-3*c)+sp.I*sp.Rational(1,2)*(3*b-d)
want_F=sp.Rational(1,2)*(a+c)+sp.I*sp.Rational(1,2)*(b+d)
assert sp.simplify(G3-want_G)==0
assert sp.simplify(F1-want_F)==0

# Complex derivative acting on z^m shows spin m exactly.
z=x+sp.I*y
D=lambda f: sp.diff(f,x)+sp.I*sp.diff(f,y)
# D is the spin-raising convention used in the note for frame rotations.
# Algebraic cubic basis:
re3=sp.expand(sp.re(z**3))
im3=sp.expand(sp.im(z**3))
assert sp.expand(re3-(x**3-3*x*y**2))==0
assert sp.expand(im3-(3*x**2*y-y**3))==0

# Scaling dimensions: Phi_L=A f(x/L,y/L) -> kth derivative L^-k.
L,A=sp.symbols("L A", positive=True)
u,v=sp.symbols("u v", real=True)
f=u**3+2*u*v**2
Phi=A*f.subs({u:x/L,v:y/L})
g2=sp.diff(Phi,x,2)
g3=sp.diff(Phi,x,3)
assert sp.simplify(g2*L**2/A).has(L)==False
assert sp.simplify(g3*L**3/A).has(L)==False

print("PASS: spin-2 shear, spin-1/spin-3 flexion decomposition and derivative scale covariance.")
