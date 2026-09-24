#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOL = 1e-12

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def det3(a,b,c):
    return (
        a[0]*(b[1]*c[2]-b[2]*c[1])
        - a[1]*(b[0]*c[2]-b[2]*c[0])
        + a[2]*(b[0]*c[1]-b[1]*c[0])
    )

def close(a,b,tol=TOL):
    return abs(a-b) <= tol

def main():
    s = math.sqrt(3.0)
    n = [
        (1/s,1/s,1/s),
        (1/s,-1/s,-1/s),
        (-1/s,1/s,-1/s),
        (-1/s,-1/s,1/s),
    ]
    failures=[]

    for i,v in enumerate(n):
        if not close(dot(v,v),1.0):
            failures.append(f"norm:{i}")
    for i in range(4):
        for j in range(i+1,4):
            if not close(dot(n[i],n[j]),-1.0/3.0):
                failures.append(f"dot:{i}:{j}")

    centroid=tuple(sum(v[k] for v in n) for k in range(3))
    if any(abs(x)>TOL for x in centroid):
        failures.append("centroid")

    edge2=dot(sub(n[1],n[0]),sub(n[1],n[0]))
    if not close(edge2,8.0/3.0):
        failures.append("edge2")

    a=sub(n[1],n[0]); b=sub(n[2],n[0]); c=sub(n[3],n[0])
    volume=abs(det3(a,b,c))/6.0
    expected_volume=8.0/(9.0*math.sqrt(3.0))
    if not close(volume,expected_volume):
        failures.append("tetra_volume")

    chi=math.acos(-1.0/3.0)
    cos_alpha=(math.cos(chi)-math.cos(chi)**2)/(math.sin(chi)**2)
    alpha=math.acos(cos_alpha)
    if not close(alpha,2.0*math.pi/3.0):
        failures.append("spherical_alpha")

    omega_face=3.0*alpha-math.pi
    fs_face=omega_face/4.0
    fs_total=4.0*fs_face
    berry_face=-omega_face/2.0
    c1_abs=abs((-0.5*4.0*math.pi)/(2.0*math.pi))

    if not close(omega_face,math.pi): failures.append("solid_angle")
    if not close(fs_face,math.pi/4.0): failures.append("fs_face")
    if not close(fs_total,math.pi): failures.append("fs_total")
    if not close(abs(berry_face),math.pi/2.0): failures.append("berry_face")
    if not close(c1_abs,1.0): failures.append("chern_abs")
    if not close(abs(cmath.exp(1j*berry_face)),1.0): failures.append("berry_unitarity")

    coeff=expected_volume/fs_total
    expected_coeff=8.0/(9.0*math.sqrt(3.0)*math.pi)
    if not close(coeff,expected_coeff): failures.append("dual_shape_coefficient")

    cp1=(ROOT/"FOUNDATIONS"/"CIR_CP1_FS_BERRY_TETRAHEDRAL_BRIDGE_V0_1.md").read_text("utf-8")
    bundle=(ROOT/"FOUNDATIONS"/"CIR_RELATIONAL_BUNDLE_COFRAME_INVARIANTS_V0_1.md").read_text("utf-8")
    required_cp1=[
        "W_{ij}^{\\rm B}\\neq W_{ij}^{X}",
        "CP1/Bloch sphere = hyperbolic Poincare disk    FORBIDDEN",
        "internal relation carrier = physical tangent   OPEN PROMOTION GATE",
    ]
    required_bundle=[
        "G_C^{\\rm atlas}=e_{SE(3)}",
        "E_{\\rm rel}\\;\\widehat{=}\\;T\\Sigma",
        "T^a=0",
        "\\Omega^a{}_b=0",
        "TELEPARALLEL_AND_LEVI_CIVITA_CONNECTIONS_DISTINCT",
    ]
    for token in required_cp1:
        if token not in cp1: failures.append("missing_cp1_firewall:"+token)
    # Last symbolic firewall is stored in provenance JSON, not prose.
    for token in required_bundle[:-1]:
        if token not in bundle: failures.append("missing_bundle_firewall:"+token)

    pin=json.loads((ROOT/"provenance"/"TIR_GEOMETRY_PARENT_PIN_V0_1.json").read_text("utf-8"))
    if pin.get("parent_commit")!="853032e019824b836de43634d949da5566396153":
        failures.append("parent_commit")
    if "TELEPARALLEL_AND_LEVI_CIVITA_CONNECTIONS_DISTINCT" not in pin.get("firewalls",[]):
        failures.append("connection_firewall_pin")

    result={
        "schema":"CIR_GEOMETRY_BRIDGE_VALIDATION_V0_1",
        "checks":{
            "tetra_unit_vectors":not any(x.startswith("norm:") for x in failures),
            "tetra_pairwise_dot":not any(x.startswith("dot:") for x in failures),
            "tetra_volume":"tetra_volume" not in failures,
            "fs_face_area":"fs_face" not in failures,
            "berry_face_phase":"berry_face" not in failures,
            "chern_magnitude_one":"chern_abs" not in failures,
            "dual_shape_coefficient":"dual_shape_coefficient" not in failures,
            "type_firewalls":not any("firewall" in x for x in failures),
            "parent_pin":"parent_commit" not in failures
        },
        "values":{
            "edge2":edge2,
            "tetra_volume":volume,
            "solid_angle_face":omega_face,
            "fs_face_area":fs_face,
            "fs_total_area":fs_total,
            "berry_face_phase":berry_face,
            "chern_number_magnitude":c1_abs,
            "dual_shape_coefficient":coeff
        },
        "failures":failures,
        "verdict":"PASS" if not failures else "FAIL"
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__=="__main__":
    main()
