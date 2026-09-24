#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOL=1e-10

def main():
    failures=[]

    # Flat-FLRW distance reciprocity reference control.
    H0=70.0
    c=299792.458
    # Constant-H toy control: chi=c*z/H0 exactly.
    for z in [0.01,0.1,0.5,1.0,2.0]:
        chi=c*z/H0
        DA=chi/(1.0+z)
        DL=(1.0+z)*chi
        if abs(DL-(1.0+z)**2*DA)>TOL*max(1.0,abs(DL)):
            failures.append("distance_duality")

    # Event acceleration estimator: y=x^2 has exact centered y''=2;
    # the y'^2 term is also exact at the center for a symmetric stencil.
    for x,h in [(0.3,0.1),(1.1,0.05),(-0.7,0.2)]:
        ym=(x-h)**2; y0=x*x; yp=(x+h)**2
        y1=(yp-ym)/(2*h)
        y2=(yp-2*y0+ym)/(h*h)
        A=y2+y1*y1
        target=2+4*x*x
        if abs(A-target)>TOL: failures.append("event_acceleration_estimator")

    doc=(ROOT/"OBSERVABLES"/"CIR_OBSERVATIONAL_FALSIFICATION_CONTRACT_V0_1.md").read_text("utf-8")
    required=[
      "similar lensing morphology}\\neq\\text{same microscopic mechanism",
      "LOCAL_PPN_LENSING_GW_VALIDATION_AFTER_BINDING = OPEN",
      "PROSPECTIVE_PREDICTION_FREEZE           NONE",
      "cross-observable no-retune audit"
    ]
    for token in required:
        if token not in doc: failures.append("missing_contract:"+token)

    freeze=json.loads((ROOT/"schemas"/"CIR_PREDICTION_FREEZE_V0_1.json").read_text("utf-8"))
    if freeze.get("status")!="TEMPLATE_ONLY": failures.append("freeze_status")
    if freeze.get("verdict") is not None: failures.append("premature_verdict")
    if freeze.get("exact_commit") is not None: failures.append("premature_commit_pin")

    pin=json.loads((ROOT/"provenance"/"TIR_OBSERVABLES_PARENT_PIN_V0_1.json").read_text("utf-8"))
    if pin.get("parent_commit")!="853032e019824b836de43634d949da5566396153":
        failures.append("parent_commit")
    if "LOCAL_PPN_LENSING_GW_VALIDATION_AFTER_BINDING" not in pin.get("inherited_open",[]):
        failures.append("lensing_gate_not_open")

    out={
      "schema":"CIR_OBSERVATIONAL_CONTRACT_VALIDATION_V0_1",
      "checks":{
        "distance_duality_control":"distance_duality" not in failures,
        "event_acceleration_estimator":"event_acceleration_estimator" not in failures,
        "contract_firewalls":not any(x.startswith("missing_contract") for x in failures),
        "freeze_is_unpopulated":not any(x.startswith("premature_") or x=="freeze_status" for x in failures),
        "parent_pin":"parent_commit" not in failures,
        "lensing_gate_remains_open":"lensing_gate_not_open" not in failures
      },
      "failures":failures,
      "verdict":"PASS" if not failures else "FAIL"
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__=="__main__":
    main()
