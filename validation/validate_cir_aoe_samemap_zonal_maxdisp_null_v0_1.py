#!/usr/bin/env python3
"""
Reproduce the exact same-map maximum-dispersion geometry and a deterministic
isotropic Monte Carlo null for the zonal/max-dispersion relation.

Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.special import sph_harm_y
from scipy.optimize import minimize

SEED = 20260926
NSIM = 100000
NGRID = 4096

OBS = {
    2: np.array([8.361e-6+0j,
                 -3.638e-6+8.0101e-6j,
                 -1.265e-5-1.493e-5j]),
    3: np.array([-6.261e-6+0j,
                 -8.912e-6+8.715e-7j,
                 2.172e-5+1.196e-6j,
                 -1.401e-5+3.048e-5j]),
}

def full_state(a_pos,l):
    out=[]
    for m in range(-l,l+1):
        if m<0:
            k=-m
            out.append(((-1)**k)*np.conj(a_pos[k]))
        else:
            out.append(a_pos[m])
    return np.asarray(out,complex)

def L_mats(l):
    ms=np.arange(-l,l+1)
    n=2*l+1
    Lz=np.diag(ms.astype(float))
    Lp=np.zeros((n,n),complex)
    for j,m in enumerate(ms[:-1]):
        Lp[j+1,j]=math.sqrt(l*(l+1)-m*(m+1))
    Lm=Lp.T.conj()
    return [(Lp+Lm)/2, (Lp-Lm)/(2j), Lz]

OPS={}
for l in (2,3):
    L=L_mats(l)
    OPS[l]=[[(L[i]@L[j]+L[j]@L[i])/2 for j in range(3)] for i in range(3)]

def Qmat(a_pos,l):
    a=full_state(a_pos,l)
    P=np.vdot(a,a).real
    Q=np.zeros((3,3))
    for i in range(3):
        for j in range(i,3):
            q=np.vdot(a,OPS[l][i][j]@a).real/(P*l*(l+1))
            Q[i,j]=Q[j,i]=q
    return Q

def top_axis(a2,a3):
    Q=Qmat(a2,2)+Qmat(a3,3)
    w,V=np.linalg.eigh(Q)
    return V[:,-1],w

def fib_sphere(n):
    i=np.arange(n)
    z=1-2*(i+0.5)/n
    phi=(np.pi*(3-math.sqrt(5))*i)%(2*np.pi)
    r=np.sqrt(1-z*z)
    xyz=np.column_stack([r*np.cos(phi),r*np.sin(phi),z])
    theta=np.arccos(z)
    return theta,phi,xyz

def real_basis(l,theta,phi):
    cols=[sph_harm_y(l,0,theta,phi).real]
    for m in range(1,l+1):
        Y=sph_harm_y(l,m,theta,phi)
        cols += [2*Y.real,-2*Y.imag]
    return np.column_stack(cols)

def rv(a):
    out=[a[0].real]
    for m in range(1,len(a)):
        out += [a[m].real,a[m].imag]
    return np.asarray(out)

def pwr(v,l):
    p=v[...,0]**2
    for k in range(l):
        p += 2*(v[...,1+2*k]**2+v[...,2+2*k]**2)
    return p

theta,phi,XYZ=fib_sphere(NGRID)
B2=real_basis(2,theta,phi)
B3=real_basis(3,theta,phi)

def zonal_grid(a2,a3):
    v2,v3=rv(a2),rv(a3)
    z=(4*np.pi/5)*(B2@v2)**2/pwr(v2,2) + (4*np.pi/7)*(B3@v3)**2/pwr(v3,3)
    k=int(np.argmax(z))
    return XYZ[k],float(z[k])

aobs,eig=top_axis(OBS[2],OBS[3])
zobs,zscore=zonal_grid(OBS[2],OBS[3])
delta_obs=90-math.degrees(math.acos(min(1,abs(float(aobs@zobs)))))

rng=np.random.default_rng(SEED)
count_delta=count_z=count_joint=0
for _ in range(NSIM):
    samp={}
    for l in (2,3):
        a=np.empty(l+1,complex)
        a[0]=rng.normal()
        for m in range(1,l+1):
            a[m]=(rng.normal()+1j*rng.normal())/math.sqrt(2)
        samp[l]=a
    aa,_=top_axis(samp[2],samp[3])
    zz,zv=zonal_grid(samp[2],samp[3])
    delta=90-math.degrees(math.acos(min(1,abs(float(aa@zz)))))
    A=delta<=delta_obs
    B=zv>=zscore
    count_delta += A
    count_z += B
    count_joint += A and B

print({
    "delta_obs_grid_deg":delta_obs,
    "Z23_obs_grid":zscore,
    "p_delta":(count_delta+1)/(NSIM+1),
    "p_Z23":(count_z+1)/(NSIM+1),
    "p_joint":(count_joint+1)/(NSIM+1),
})
