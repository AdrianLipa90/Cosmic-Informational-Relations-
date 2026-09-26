#!/usr/bin/env python3
import argparse, hashlib, json, math
from pathlib import Path

AXIS_L_DEG=239.9881633256477
AXIS_B_DEG=68.5117419161366
R_CMB_MPC=13873.0
LMAX=5

def sha256_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('fits')
    ap.add_argument('--expected-sha256')
    ap.add_argument('--out')
    args=ap.parse_args()

    try:
        import healpy as hp
        import numpy as np
        from scipy.special import sph_harm_y
    except Exception as exc:
        raise SystemExit('Required: healpy, numpy, scipy. '+repr(exc))

    p=Path(args.fits)
    digest=sha256_file(p)
    if args.expected_sha256 and digest.lower()!=args.expected_sha256.lower():
        raise SystemExit('SHA256 mismatch; fail closed.')

    T=hp.read_map(str(p),field=0,dtype=float,verbose=False)
    if not np.all(np.isfinite(T)):
        raise SystemExit('Non-finite I_STOKES pixels; v0.1 full-sky pipeline fails closed.')

    alm=hp.map2alm(
        T,lmax=LMAX,iter=3,pol=False,
        use_weights=False,use_pixel_weights=False
    )

    theta=math.radians(90.0-AXIS_B_DEG)
    phi=math.radians(AXIS_L_DEG)

    def gell(ell):
        z=0j
        for m in range(ell+1):
            idx=hp.Alm.getidx(LMAX,ell,m)
            a=alm[idx]
            y=sph_harm_y(ell,m,theta,phi)
            if m==0:
                z += a*y
            else:
                z += 2.0*(a*y).real
        return float(z.real)

    g={ell:gell(ell) for ell in range(2,6)}
    if not all(math.isfinite(v) for v in g.values()) or g[2]==0:
        raise SystemExit('Unidentified/non-finite low-l projection; fail closed.')

    r23=abs(g[3]/g[2])
    r34=abs(g[4]/g[3]) if g[3]!=0 else None
    r45=abs(g[5]/g[4]) if g[4]!=0 else None

    def dyadic_record(radial_ratio, distance_mpc):
        n=-math.log(radial_ratio,2)
        k=round(n)
        return {
            'radial_ratio':radial_ratio,
            'n_cont':n,
            'nearest_integer':k,
            'eta':n-k,
            'distance_Mpc_comoving':distance_mpc
        }

    branches={}
    if 0<r23<5/3:
        x=(3/5)*r23
        pred34=(9/10)*r23
        pred45=(21/25)*r23
        branches['interior']={
            **dyadic_record(x,R_CMB_MPC*x),
            'pred_r34':pred34,
            'pred_r45':pred45,
            'resid_r34': None if r34 is None else r34-pred34,
            'resid_r45': None if r45 is None else r45-pred45,
            'frac_resid_r34': None if r34 is None else (r34/pred34-1),
            'frac_resid_r45': None if r45 is None else (r45/pred45-1)
        }
    if 0<r23<3:
        q=r23/3
        pred34=(5/6)*r23
        pred45=(2/3)*r23
        branches['exterior']={
            **dyadic_record(q,R_CMB_MPC/q),
            'pred_r34':pred34,
            'pred_r45':pred45,
            'resid_r34': None if r34 is None else r34-pred34,
            'resid_r45': None if r45 is None else r45-pred45,
            'frac_resid_r34': None if r34 is None else (r34/pred34-1),
            'frac_resid_r45': None if r45 is None else (r45/pred45-1)
        }

    result={
        'schema':'CIR_AOE_TIDAL_SHADOW_HEALPIX_RESULT_V0_1',
        'input':{
            'file':p.name,
            'sha256':digest,
            'field':0,
            'lmax':LMAX,
            'map2alm_iter':3,
            'use_weights':False,
            'use_pixel_weights':False
        },
        'frozen_axis_galactic_deg':[AXIS_L_DEG,AXIS_B_DEG],
        'R_CMB_Mpc_comoving':R_CMB_MPC,
        'g_uK_or_input_map_unit':{str(k):v for k,v in g.items()},
        'ratios':{'r23':r23,'r34':r34,'r45':r45},
        'branch_domain_verdict': (
            'FAIL_BOTH_TIDAL_POINT_BRANCHES' if r23>=3
            else 'EXTERIOR_ONLY' if r23>=5/3
            else 'INTERIOR_AND_EXTERIOR_ADMISSIBLE'
        ),
        'branches':branches,
        'epistemic_status':'REAL_DATA_RESULT_ONLY; no source-catalog matching performed'
    }
    txt=json.dumps(result,indent=2,sort_keys=True)
    if args.out:
        Path(args.out).write_text(txt+'\n')
    print(txt)

if __name__=='__main__':
    main()
