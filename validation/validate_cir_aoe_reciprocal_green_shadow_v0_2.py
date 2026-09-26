#!/usr/bin/env python3
import math

def P(l,x):
    if l==0: return 1.0
    if l==1: return x
    p0,p1=1.0,x
    for n in range(1,l):
        p2=((2*n+1)*x*p1-n*p0)/(n+1)
        p0,p1=p1,p2
    return p1

def integrate(f,n=60000):
    h=2.0/n
    return h*sum(f(-1.0+(i+0.5)*h) for i in range(n))

def coeffs(R,d,L=5):
    def G(mu):
        return 1.0/math.sqrt(R*R+d*d-2*R*d*mu)
    out=[]
    for l in range(L+1):
        out.append((2*l+1)/2*integrate(lambda x,l=l:G(x)*P(l,x)))
    return out

for R,d in [(1.0,0.2),(1.0,0.6),(1.0,2.0),(1.0,5.0),(3.0,1.0),(2.0,7.0)]:
    cs=coeffs(R,d)
    q=min(d/R,R/d)
    for l in range(0,5):
        ratio=abs(cs[l+1]/cs[l])
        if abs(ratio-q)>3e-6:
            raise SystemExit(f"FAIL R={R} d={d} ell={l} ratio={ratio} q={q}")
    x=d/R
    B=math.log(x)
    if abs(q-math.exp(-abs(B)))>1e-14:
        raise SystemExit("FAIL log reciprocal identity")

for n in range(1,21):
    q=2.0**(-n)
    for x in (q,1.0/q):
        if abs(math.exp(-abs(math.log(x)))-q)>1e-14:
            raise SystemExit("FAIL dyadic reciprocal shell")

print("PASS: reciprocal Green coefficients and dyadic radial branches.")
