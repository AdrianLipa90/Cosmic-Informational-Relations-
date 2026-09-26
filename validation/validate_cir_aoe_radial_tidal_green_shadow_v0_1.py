#!/usr/bin/env python3
import math

def P(l,x):
    if l==0:return 1.0
    if l==1:return x
    p0,p1=1.0,x
    for n in range(1,l):
        p2=((2*n+1)*x*p1-n*p0)/(n+1)
        p0,p1=p1,p2
    return p1

def integrate(f,n=80000):
    h=2.0/n
    return h*sum(f(-1+(i+0.5)*h) for i in range(n))

def G(R,d,mu):
    return 1.0/math.sqrt(R*R+d*d-2*R*d*mu)

def d2R_numeric(R,d,mu,h=1e-4):
    return (G(R+h,d,mu)-2*G(R,d,mu)+G(R-h,d,mu))/(h*h)

def coeffs(R,d,L=5):
    out=[]
    for l in range(L+1):
        out.append((2*l+1)/2*integrate(lambda mu,l=l:d2R_numeric(R,d,mu)*P(l,mu),n=12000))
    return out

for R,d in [(2.0,0.6),(2.0,1.5)]:
    x=d/R
    cs=coeffs(R,d)
    assert abs(abs(cs[3]/cs[2])-(5/3)*x)<2e-4
    assert abs(abs(cs[4]/cs[3])-(3/2)*x)<2e-4
    assert abs(abs(cs[5]/cs[4])-(7/5)*x)<3e-4

for R,d in [(1.0,2.0),(1.0,4.0)]:
    q=R/d
    cs=coeffs(R,d)
    assert abs(abs(cs[3]/cs[2])-3*q)<3e-4
    assert abs(abs(cs[4]/cs[3])-(5/2)*q)<4e-4
    assert abs(abs(cs[5]/cs[4])-2*q)<7e-4

print("PASS: radial-tidal Green-shadow coefficient ratios.")
