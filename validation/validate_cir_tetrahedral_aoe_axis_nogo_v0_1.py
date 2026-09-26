#!/usr/bin/env python3
import numpy as np, math

def L_matrices(l):
    ms=np.arange(-l,l+1,dtype=float)
    n=2*l+1
    Lz=np.diag(ms)
    Lp=np.zeros((n,n),dtype=complex)
    for j,m in enumerate(ms[:-1]):
        Lp[j+1,j]=math.sqrt(l*(l+1)-m*(m+1))
    Lm=Lp.T.conj()
    return (Lp+Lm)/2,(Lp-Lm)/(2j),Lz

# Tetrahedral H3=xyz in a vertex-axis frame contains m=0 and m=±3.
# Relative normalized power fractions are zonal 5/9 and planar 4/9.
# Choose phases arbitrarily; Q must be 4 I.
l=3
Lx,Ly,Lz=L_matrices(l)
psi=np.zeros(7,dtype=complex)
# ordering m=-3..3. real tetrahedral state with ±3 antisymmetric pair
psi[0]=math.sqrt(2/9)       # |-3>
psi[3]=math.sqrt(5/9)       # |0>
psi[6]=-math.sqrt(2/9)      # |+3>
psi/=np.linalg.norm(psi)
Ls=[Lx,Ly,Lz]
Q=np.zeros((3,3),float)
for i,A in enumerate(Ls):
    for j,B in enumerate(Ls):
        Q[i,j]=np.real(np.vdot(psi,(A@B+B@A)@psi))/2
assert np.max(np.abs(Q-4*np.eye(3)))<1e-12, Q

# l=2,m=0 descendant: M(beta)=3 sin^2 beta.
l=2
Lx,Ly,Lz=L_matrices(l)
q2=np.zeros(5,dtype=complex); q2[2]=1
for beta in np.linspace(0,math.pi,17):
    Ln=math.sin(beta)*Lx+math.cos(beta)*Lz
    M=float(np.real(np.vdot(q2,Ln@Ln@q2)))
    assert abs(M-3*math.sin(beta)**2)<1e-11

print("PASS: tetrahedral l=3 dispersion is isotropic and joint AoE maximum is a great-circle degeneracy.")
