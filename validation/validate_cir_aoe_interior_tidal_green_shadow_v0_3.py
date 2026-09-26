#!/usr/bin/env python3
import math

def P(l,x):
    if l == 0: return 1.0
    if l == 1: return x
    p0,p1=1.0,x
    for n in range(1,l):
        p2=((2*n+1)*x*p1-n*p0)/(n+1)
        p0,p1=p1,p2
    return p1

def G(R,d,mu):
    return 1.0/math.sqrt(R*R+d*d-2*R*d*mu)

def d2_numeric(R,d,mu,h=1e-5):
    return (G(R,d+h,mu)-2*G(R,d,mu)+G(R,d-h,mu))/(h*h)

def integrate(f,n=50000):
    h=2.0/n
    return h*sum(f(-1+(i+0.5)*h) for i in range(n))

for q in (0.1,0.25,0.5,0.75):
    R=2.3
    d=q*R
    coeff=[]
    for ell in range(0,6):
        c=(2*ell+1)/2*integrate(lambda mu,ell=ell:d2_numeric(R,d,mu)*P(ell,mu),n=12000)
        coeff.append(c)
    # l=0,1 vanish; finite differencing leaves small numerical noise
    if abs(coeff[0]) > 2e-5 or abs(coeff[1]) > 2e-5:
        raise SystemExit(("FAIL annihilation",q,coeff[:2]))
    for ell in range(2,6):
        target=(ell*(ell-1)*(q**(ell-2)))/(R**3)
        if abs(coeff[ell]-target) > 8e-5:
            raise SystemExit(("FAIL coefficient",q,ell,coeff[ell],target))
    r23=abs(coeff[3]/coeff[2])
    r34=abs(coeff[4]/coeff[3])
    r45=abs(coeff[5]/coeff[4])
    if abs(r23-3*q)>2e-4: raise SystemExit("FAIL r23")
    if abs(r34-2*q)>2e-4: raise SystemExit("FAIL r34")
    if abs(r45-(5/3)*q)>2e-4: raise SystemExit("FAIL r45")

for n in range(1,12):
    q=2.0**(-n)
    r23=3*q
    n_back=math.log2(3/r23)
    if abs(n_back-n)>1e-14:
        raise SystemExit("FAIL dyadic inverse")

print("PASS: interior tidal Green multipole law and dyadic inverse.")
