#!/usr/bin/env python3
import cmath, json, math

AXIS_L_DEG = 239.9881633256477
AXIS_B_DEG = 68.5117419161366

DATA = {
  "SMICA_raw": {
    2:[13.089+0j,-1.530+2.497j,-15.503-17.091j],
    3:[-5.959+0j,-12.841+1.671j,22.086+1.670j,-12.465+29.402j]
  },
  "SMICA_deboosted": {
    2:[11.622+0j,-1.830+5.143j,-14.363-16.852j],
    3:[-5.964+0j,-12.857+1.709j,22.139+1.696j,-12.421+29.362j]
  },
  "NILC_raw": {
    2:[13.512+0j,-1.375+1.722j,-13.564-16.325j],
    3:[-6.117+0j,-9.547+1.896j,22.242+1.875j,-12.914+28.340j]
  },
  "NILC_deboosted": {
    2:[12.046+0j,-1.670+4.368j,-12.423-16.086j],
    3:[-6.122+0j,-9.563+1.935j,22.291+1.900j,-12.873+28.301j]
  }
}

EXPECTED = {
  "SMICA_raw": (7.390464410500907,-11.6281044603997,1.5733929310149504),
  "SMICA_deboosted": (5.285160164583028,-11.676965934860016,2.2093873357159213),
  "NILC_raw": (7.82862333359097,-10.602694379050684,1.3543497914322637),
  "NILC_deboosted": (5.72508819924693,-10.651384264891725,1.8604751392813117)
}

def double_factorial_odd(k):
    if k <= 0: return 1.0
    out=1.0
    for j in range(1,k+1,2): out*=j
    return out

def assoc_legendre(l,m,x):
    pmm = ((-1)**m)*double_factorial_odd(2*m-1)*(max(0.0,1-x*x)**(m/2))
    if l==m: return pmm
    pm1m=x*(2*m+1)*pmm
    if l==m+1: return pm1m
    p0,p1=pmm,pm1m
    for L in range(m+2,l+1):
        p2=((2*L-1)*x*p1-(L+m-1)*p0)/(L-m)
        p0,p1=p1,p2
    return p1

def Y(l,m,theta,phi):
    x=math.cos(theta)
    norm=math.sqrt((2*l+1)/(4*math.pi)*math.factorial(l-m)/math.factorial(l+m))
    return norm*assoc_legendre(l,m,x)*cmath.exp(1j*m*phi)

def multipole_at(alms,l,theta,phi):
    s=alms[0]*Y(l,0,theta,phi)
    for m in range(1,l+1):
        s += 2.0*(alms[m]*Y(l,m,theta,phi)).real
    return float(s.real)

theta=math.radians(90.0-AXIS_B_DEG)
phi=math.radians(AXIS_L_DEG)
out={}
for name,d in DATA.items():
    g2=multipole_at(d[2],2,theta,phi)
    g3=multipole_at(d[3],3,theta,phi)
    q=abs(g3/g2)
    e2,e3,eq=EXPECTED[name]
    assert abs(g2-e2)<1e-9,(name,g2,e2)
    assert abs(g3-e3)<1e-9,(name,g3,e3)
    assert abs(q-eq)<1e-9,(name,q,eq)
    assert q>1.0,(name,q)
    out[name]={"g2":g2,"g3":g3,"q23":q,"verdict":"FAIL_q_lt_1"}

print(json.dumps({"status":"PASS_REPRODUCING_MODEL_FAIL","results":out},indent=2,sort_keys=True))
