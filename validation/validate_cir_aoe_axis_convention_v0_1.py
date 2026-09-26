#!/usr/bin/env python3
import math
import numpy as np

# Angular momentum matrices in |l,m> basis, hbar=1.
def matrices(l):
    ms=np.arange(-l,l+1,dtype=float)
    n=2*l+1
    Lz=np.diag(ms)
    Lp=np.zeros((n,n),dtype=complex)
    for j,m in enumerate(ms[:-1]):
        # column j=|m>, row j+1=|m+1>
        Lp[j+1,j]=math.sqrt(l*(l+1)-m*(m+1))
    Lm=Lp.T.conj()
    Lx=(Lp+Lm)/2
    Ly=(Lp-Lm)/(2j)
    return ms,Lx,Ly,Lz

checks={}
for l in (2,3,4,7):
    ms,Lx,Ly,Lz=matrices(l)
    psi=np.zeros(2*l+1,dtype=complex)
    psi[l]=1.0 # m=0
    def ex(A):
        return float(np.real(np.vdot(psi,A@A@psi)))
    checks[f'l{l}_Lz2_zero']=abs(ex(Lz))<1e-12
    checks[f'l{l}_Lx2']=abs(ex(Lx)-l*(l+1)/2)<1e-12
    checks[f'l{l}_Ly2']=abs(ex(Ly)-l*(l+1)/2)<1e-12
    # General axis in x-z plane.
    for beta in (0.0,0.2,0.7,math.pi/2):
        Ln=math.sin(beta)*Lx+math.cos(beta)*Lz
        got=ex(Ln)
        want=l*(l+1)/2*(math.sin(beta)**2)
        if abs(got-want)>1e-11:
            raise SystemExit((l,beta,got,want))

status='PASS' if all(checks.values()) else 'FAIL'
print(status)
for k,v in checks.items(): print(k,v)
if status!='PASS': raise SystemExit(1)
