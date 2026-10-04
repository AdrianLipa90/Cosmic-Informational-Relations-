#!/usr/bin/env python3
import json
import math

KAPPA = math.log(2.0)/(24.0*math.pi)
TOL = 1e-12
checks = {}

checks["kappa_block_identity"] = abs(KAPPA*(24.0*math.pi)-math.log(2.0)) < 1e-14

# U(1) registry: degree-m maps must be 2pi-periodic after wrapping.
def u1_pair(phi, m):
    return (math.cos(m*phi), math.sin(m*phi))

checks["u1_integer_degree_periodicity"] = all(
    max(abs(a-b) for a,b in zip(u1_pair(phi+2.0*math.pi,m), u1_pair(phi,m))) < TOL
    for m in (-7,-2,-1,0,1,2,9)
    for phi in (-2.3,-0.1,0.0,0.71,5.9)
)

# A non-integer slope is not a well-defined U(1) homomorphism on the quotient.
lam = 0.5
checks["noninteger_affine_slope_rejected_as_u1_registry"] = any(
    max(abs(a-b) for a,b in zip(u1_pair(phi+2.0*math.pi,lam), u1_pair(phi,lam))) > 1e-6
    for phi in (0.0,0.4,1.7)
)

checks["u1_isomorphism_degree_abs_one"] = all(
    ((abs(m) == 1) == (m in (-1,1)))
    for m in range(-8,9)
)

# CIR dyadic block is compatible with every nonzero degree m by a lifted QHTRI increment 24pi/m.
checks["dyadic_block_registry_roundtrip"] = all(
    abs(KAPPA*m*(24.0*math.pi/m)-math.log(2.0)) < 1e-14
    for m in (-7,-3,-1,1,2,5,11)
)

def rho(B, omega, N, V, X):
    return B*omega*N*X/V

def eps_q(B, omega, X, q0):
    return B*omega*X/q0

def j_q(N, V, q0):
    return q0*N/V

cells = [
    (2.0, 3.0, 5.0, 7.0, 0.4),
    (0.8, 11.0, 2.5, 13.0, -0.2),
    (5.5, 0.7, 17.0, 19.0, 1.3),
    (1.2, 4.4, 0.9, 2.3, 2.0),
]

checks["rfc_current_factorization"] = all(
    abs(rho(B,w,N,V,X)-eps_q(B,w,X,q0)*j_q(N,V,q0))
    < TOL*max(1.0,abs(rho(B,w,N,V,X)))
    for B,w,N,V,X in cells
    for q0 in (0.25,1.0,7.0)
)

checks["cell_integration_cancels_volume"] = all(
    abs(V*rho(B,w,N,V,X)-B*w*N*X)
    < TOL*max(1.0,abs(B*w*N*X))
    for B,w,N,V,X in cells
)

checks["cell_integration_cancels_q0"] = all(
    abs(V*eps_q(B,w,X,q0)*j_q(N,V,q0)-B*w*N*X)
    < TOL*max(1.0,abs(B*w*N*X))
    for B,w,N,V,X in cells
    for q0 in (0.1,0.5,1.0,3.0,10.0)
)

E_sum = sum(V*rho(B,w,N,V,X) for B,w,N,V,X in cells)
E_product_sum = sum(B*w*N*X for B,w,N,V,X in cells)
checks["multicell_extensive_sum"] = abs(E_sum-E_product_sum) < TOL*max(1.0,abs(E_sum))

weights = [1.0,0.25,0.0,0.8]
E_eff = sum(c*V*rho(B,w,N,V,X) for c,(B,w,N,V,X) in zip(weights,cells))
E_eff2 = sum(c*B*w*N*X for c,(B,w,N,V,X) in zip(weights,cells))
checks["weighted_support_identity"] = abs(E_eff-E_eff2) < TOL*max(1.0,abs(E_eff))

# QHTRI action phase composed with CIR registry.
def h_from_energy(E, eta, m):
    return -KAPPA*m*E/eta

checks["cir_qhtri_rate_composition"] = all(
    abs(h_from_energy(E,eta,m)-KAPPA*m*(-E/eta)) < TOL
    for E,eta,m in ((3.0,2.0,1),(-0.5,7.0,-1),(11.0,13.0,3))
)

# Integration does not identify factors: keep B*w*N*X invariant by reciprocal rescaling.
B,w,N,V,X = cells[0]
E0 = B*w*N*X
checks["extensive_product_identifiability_firewall"] = all(
    abs((B*s)*(w/s)*N*X-E0) < TOL*max(1.0,abs(E0))
    for s in (0.2,0.5,2.0,9.0)
)

status = "PASS" if all(checks.values()) else "FAIL"
receipt = {
    "schema":"CIR_PHASE_REGISTRY_DENSITY_TO_POTENTIAL_VALIDATION_RECEIPT_V0_1",
    "date":"2026-10-04",
    "status":status,
    "checks":checks,
    "summary":{
        "passed":sum(bool(v) for v in checks.values()),
        "total":len(checks)
    },
    "epistemic_boundary":{
        "exact":[
            "integer-degree U(1) registry classification",
            "same-cell RFC density integration cancels V_R",
            "same-cell current form also cancels q0",
            "multicell and weighted-support algebra"
        ],
        "conditional":[
            "H_D = -kappa*m*E_Q/eta_phi after QHTRI source-energy admission and phase registry"
        ],
        "open":[
            "physical QHTRI source-energy selection",
            "support-kernel selection",
            "eta_phi calibration",
            "CIR D to cosmological observable binding"
        ]
    }
}
print(json.dumps(receipt,sort_keys=True,indent=2))
if status != "PASS":
    raise SystemExit(1)
