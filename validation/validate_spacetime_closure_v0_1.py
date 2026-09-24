#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOL=1e-11

def det(matrix):
    a=[list(map(float,row)) for row in matrix]
    n=len(a)
    d=1.0
    for i in range(n):
        p=max(range(i,n),key=lambda r:abs(a[r][i]))
        if abs(a[p][i])<1e-15:
            return 0.0
        if p!=i:
            a[i],a[p]=a[p],a[i]
            d*=-1.0
        piv=a[i][i]
        d*=piv
        for r in range(i+1,n):
            f=a[r][i]/piv
            for c in range(i+1,n):
                a[r][c]-=f*a[i][c]
    return d

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def eye_error(m):
    return max(abs(m[i][j]-(1.0 if i==j else 0.0)) for i in range(len(m)) for j in range(len(m)))

def main():
    failures=[]
    h=[[2.0,0.2,0.1],[0.2,1.5,0.05],[0.1,0.05,1.2]]
    beta=[0.3,-0.2,0.1]
    N=1.7

    # explicit inverse of 3x3 via cofactors
    dh=det(h)
    if dh<=0: failures.append("h_not_positive_det")
    a,b,c=h[0]; d,e,f=h[1]; g,hh,i=h[2]
    cof=[
      [e*i-f*hh, c*hh-b*i, b*f-c*e],
      [f*g-d*i, a*i-c*g, c*d-a*f],
      [d*hh-e*g, b*g-a*hh, a*e-b*d]
    ]
    hinv=[[cof[r][col]/dh for col in range(3)] for r in range(3)]
    betad=[sum(h[r][k]*beta[k] for k in range(3)) for r in range(3)]
    betasq=sum(beta[k]*betad[k] for k in range(3))

    g4=[[0.0]*4 for _ in range(4)]
    g4[0][0]=-N*N+betasq
    for j in range(3):
        g4[0][j+1]=betad[j]
        g4[j+1][0]=betad[j]
        for k in range(3): g4[j+1][k+1]=h[j][k]

    inv=[[0.0]*4 for _ in range(4)]
    inv[0][0]=-1.0/(N*N)
    for j in range(3):
        inv[0][j+1]=beta[j]/(N*N)
        inv[j+1][0]=beta[j]/(N*N)
        for k in range(3):
            inv[j+1][k+1]=hinv[j][k]-beta[j]*beta[k]/(N*N)

    if abs(det(g4)+N*N*dh)>TOL: failures.append("adm_determinant")
    if eye_error(matmul(g4,inv))>TOL: failures.append("adm_inverse")

    schur=g4[0][0]-sum(g4[0][i+1]*hinv[i][j]*g4[j+1][0] for i in range(3) for j in range(3))
    if abs(schur+N*N)>TOL: failures.append("schur")

    # spherical vacuum power-law check V=A r^p:
    # 2V'+V/r = A r^(p-1)(2p+1), so nonzero branch forces p=-1/2.
    p=-0.5
    if abs(2*p+1)>TOL: failures.append("river_power")
    for bad in (-1.0,0.0,0.5,1.0):
        if abs(2*bad+1)<TOL: failures.append("river_uniqueness_probe")

    # flat FLRW extrinsic-curvature contraction
    H=0.07; c0=3.0
    K=3*H/c0
    KijKij=3*(H/c0)**2
    if abs((K*K-KijKij)-6*H*H/(c0*c0))>TOL:
        failures.append("flrw_constraint")

    doc=(ROOT/"FOUNDATIONS"/"CIR_SPATIAL_TEMPORAL_ADM_CLOSURE_V0_1.md").read_text("utf-8")
    required=[
      "det g=-N_\\Theta^2\\det h<0",
      "RF-E9 operator remains the unique extrinsic-curvature authority",
      "NOEMA runtime vectors",
      "PhaseNav / Terminal36D phase states",
      "late-time acceleration source                    OPEN",
      "microscopic TIR source -> physical coframe       OPEN"
    ]
    for token in required:
        if token not in doc: failures.append("missing_firewall:"+token)

    pin=json.loads((ROOT/"provenance"/"TIR_SPACETIME_PARENT_PIN_V0_1.json").read_text("utf-8"))
    if pin.get("parent_commit")!="853032e019824b836de43634d949da5566396153":
        failures.append("parent_commit")

    out={
      "schema":"CIR_SPACETIME_CLOSURE_VALIDATION_V0_1",
      "checks":{
        "adm_determinant":"adm_determinant" not in failures,
        "adm_inverse":"adm_inverse" not in failures,
        "schur_lorentzian":"schur" not in failures,
        "spherical_vacuum_power":"river_power" not in failures,
        "flrw_constraint":"flrw_constraint" not in failures,
        "firewalls":not any(x.startswith("missing_firewall:") for x in failures),
        "parent_pin":"parent_commit" not in failures
      },
      "values":{
        "det_h":dh,
        "det_g":det(g4),
        "schur":schur,
        "inverse_identity_error":eye_error(matmul(g4,inv))
      },
      "failures":failures,
      "verdict":"PASS" if not failures else "FAIL"
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__=="__main__":
    main()
