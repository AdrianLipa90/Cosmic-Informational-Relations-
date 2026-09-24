#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOL=1e-12

def close(a,b):
    return abs(a-b)<=TOL*max(1.0,abs(a),abs(b))

def main():
    failures=[]

    # Information-scalar formula and exact criterion equivalence.
    kappa=2.3
    alpha=0.7
    for Xi,rate in [(0.5,0.0),(1.2,0.4),(4.0,1.1),(2.0,2.0)]:
        Xip=rate*Xi
        acc=alpha*Xi/3.0-kappa*Xip*Xip/(6.0*Xi)
        criterion=abs(rate)<math.sqrt(2.0*alpha/kappa)
        if (acc>0) != criterion and abs(acc)>TOL:
            failures.append(f"scalar_criterion:{Xi}:{rate}")

    # Full scalar stress and dynamic-Lambda bookkeeping must agree.
    for phip,U in [(0.2,1.0),(1.1,0.7),(2.0,4.0)]:
        K=0.5*phip*phip
        rho=K+U
        p=K-U
        full=-kappa*(rho+3.0*p)/6.0
        split=-kappa*(K+3.0*K)/6.0+(kappa*U)/3.0
        if not close(full,split):
            failures.append("scalar_lambda_bookkeeping")

    # Exact holonomy partition invariance and naive-potential Hessian.
    U=3.2
    for tau in [0.0,0.3,1.0,math.pi,5.7]:
        C=math.cos(tau/2.0)**2
        D=math.sin(tau/2.0)**2
        if not close(C+D,1.0): failures.append("partition_unity")
        if not close(U*C+U*D,U): failures.append("equal_stress_partition")
    hessian_pi=0.5*U*math.cos(math.pi)
    if not hessian_pi<0: failures.append("naive_D_stability")

    # Pure phase kinetic source is stiff and decelerating.
    for K in [0.1,1.0,10.0]:
        rho=K; p=K
        if not close(p/rho,1.0): failures.append("phase_w")
        acc=-kappa*(rho+3.0*p)/6.0
        if not acc<0: failures.append("phase_deceleration")

    # RF-F20 isotropic response: sign is exactly opposite R0+3Rs.
    A=1.4
    for R0,Rs in [(1.0,0.0),(-4.0,1.0),(0.0,-1.0),(2.0,-0.2)]:
        active=R0+3.0*Rs
        acc=-2.0*kappa*A*A*active/3.0
        if active<0 and not acc>0: failures.append("rf_f20_positive")
        if active>0 and not acc<0: failures.append("rf_f20_negative")
        if abs(active)<=TOL and abs(acc)>TOL: failures.append("rf_f20_zero")

    doc=(ROOT/"COSMOLOGY"/"CIR_COSMOLOGICAL_SOURCE_LEDGER_V0_1.md").read_text("utf-8")
    required=[
      "the current scalar action does not derive accelerated expansion from",
      "naming }D_h\\text{ a dark channel does not create dark energy",
      "Pure phase kinetic energy is a stiff decelerating source",
      "R_0+3R_s<0",
      "dimensionful cosmological scale / rho_crit binding      OPEN",
      "It does **not** yet establish a physical dark-energy source"
    ]
    for token in required:
        if token not in doc: failures.append("missing_firewall:"+token)

    pin=json.loads((ROOT/"provenance"/"TIR_COSMOLOGY_PARENT_PIN_V0_1.json").read_text("utf-8"))
    if pin.get("parent_commit")!="853032e019824b836de43634d949da5566396153":
        failures.append("parent_commit")
    for x in [
      "CURRENT_HOLONOMY_SPECTATOR_NO_GO",
      "EQUAL_STRESS_HOLONOMY_PARTITION_NO_GO",
      "PURE_PHASE_KINETIC_W_PLUS_ONE_DECELERATING"
    ]:
        if x not in pin.get("retained_no_go",[]): failures.append("missing_nogo:"+x)

    out={
      "schema":"CIR_COSMOLOGICAL_SOURCE_LEDGER_VALIDATION_V0_1",
      "checks":{
        "information_scalar_criterion":not any(x.startswith("scalar_criterion") for x in failures),
        "scalar_dynamic_lambda_equivalence":"scalar_lambda_bookkeeping" not in failures,
        "equal_stress_partition_invariance":"equal_stress_partition" not in failures,
        "naive_D_maximum_unstable":"naive_D_stability" not in failures,
        "pure_phase_w_plus_one_decelerating":not any(x.startswith("phase_") for x in failures),
        "rf_f20_sign_test":not any(x.startswith("rf_f20") for x in failures),
        "firewalls":not any(x.startswith("missing_firewall") for x in failures),
        "parent_pin":"parent_commit" not in failures
      },
      "values":{
        "scalar_rate_threshold":math.sqrt(2.0*alpha/kappa),
        "naive_D_hessian_at_pi":hessian_pi
      },
      "failures":failures,
      "verdict":"PASS" if not failures else "FAIL"
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__=="__main__":
    main()
