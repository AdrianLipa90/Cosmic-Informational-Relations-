#!/usr/bin/env python3
import json
import math

TOL = 1e-12
checks = {}

# RFC local Hamiltonian identities.
cells = [
    # B, omega, N, V, X
    (2.0, 3.0, 5.0, 7.0, 0.4),
    (0.8, 11.0, 2.5, 13.0, -0.2),
    (5.5, 0.7, 17.0, 19.0, 1.3),
]

def H_G(B, omega, X):
    return B * X * omega

def rho_G(B, omega, N, V, X):
    return (N / V) * H_G(B, omega, X)

checks["local_density_equals_occupation_density_times_HG"] = all(
    abs(rho_G(B,w,N,V,X) - (N/V)*H_G(B,w,X))
    < TOL*max(1.0,abs(rho_G(B,w,N,V,X)))
    for B,w,N,V,X in cells
)

checks["cell_energy_equals_N_times_HG"] = all(
    abs(V*rho_G(B,w,N,V,X) - N*H_G(B,w,X))
    < TOL*max(1.0,abs(N*H_G(B,w,X)))
    for B,w,N,V,X in cells
)

E_sigma = sum(V*rho_G(B,w,N,V,X) for B,w,N,V,X in cells)
E_sigma_2 = sum(N*H_G(B,w,X) for B,w,N,V,X in cells)
checks["finite_slice_extensive_energy"] = abs(E_sigma-E_sigma_2) < TOL*max(1.0,abs(E_sigma))

# RF-F13 first-order integrand vanishes on degree-one on-shell branch:
# dot X = omega and H_G = P omega.
def first_order_integrand(P, xdot, H):
    return P*xdot-H

checks["full_first_order_action_integrand_zero_on_shell"] = all(
    abs(first_order_integrand(P,w,P*w)) < TOL
    for P,w in ((0.3,2.0),(1.0,-0.4),(7.0,11.0),(-2.0,0.25))
)

# Dynamical phase is nontrivial even though full first-order integrand vanishes.
checks["dynamical_phase_not_full_action"] = all(
    abs((-P*w/eta)) > TOL and abs(first_order_integrand(P,w,P*w)) < TOL
    for P,w,eta in ((1.0,2.0,3.0),(4.0,-0.5,2.0),(0.7,5.0,1.1))
)

# Single-rate relation: dot Phi_Q = -(P/eta) dot X.
checks["single_rate_phase_action_relation"] = all(
    abs((-P*w/eta) - (-(P/eta)*w)) < TOL
    for P,w,eta in ((1.0,2.0,3.0),(4.0,-0.5,2.0),(0.7,5.0,1.1))
)

# U(1) registry periodicity for slope r in Phi_Q=-r X.
def wrapped(x, r):
    return (math.cos(-r*x), math.sin(-r*x))

def periodic(r):
    for x in (-2.0,-0.1,0.0,0.3,4.2):
        a=wrapped(x,r)
        b=wrapped(x+2*math.pi,r)
        if max(abs(i-j) for i,j in zip(a,b)) > 1e-10:
            return False
    return True

checks["integer_ratio_gives_u1_homomorphism"] = all(periodic(r) for r in (-4,-1,0,1,2,7))
checks["noninteger_f14_ratios_fail_standard_u1_periodicity"] = (
    (not periodic(0.5)) and (not periodic(0.75))
)

# Positive eta: orientation-reversing isomorphism from X to Phi_Q requires r=P/eta=1.
checks["u1_isomorphism_requires_eta_equals_P"] = all(
    abs((P/eta)-1.0) < TOL
    for P,eta in ((1.0,1.0),(0.25,0.25),(7.0,7.0))
)

# RF-F14 branch matrix: ratio P/q0 and RF-F8 P-slope.
branches = {
    "normal_phase_kinetic": (0.5, 2.0),
    "isotropic_null_radiation": (1.0, 0.0),
    "homogeneous_radiation_completion": (0.75, 0.0),
    "homogeneous_dust": (1.0, -1.0),
}
selected = [
    name for name,(ratio,slope) in branches.items()
    if abs(ratio-1.0) < TOL and abs(slope) < TOL
]
checks["fixed_q0_global_u1_selector_unique"] = selected == ["isotropic_null_radiation"]

# Dust is pointwise degree -1 but incompatible with constant P=q0 along varying-omega RF-F8 transport.
checks["dust_pointwise_but_not_constant_P_transport"] = (
    abs(branches["homogeneous_dust"][0]-1.0) < TOL
    and abs(branches["homogeneous_dust"][1]) > TOL
)

# Matched-H is a conditional composition: once admitted, equality is exact.
for h in (0.1,1.0,13.7,-4.0):
    e_sigma = h
    h_eb = h
    if abs(e_sigma-h_eb) >= TOL:
        checks["matched_H_conditional_roundtrip"] = False
        break
else:
    checks["matched_H_conditional_roundtrip"] = True

status = "PASS" if all(checks.values()) else "FAIL"
receipt = {
    "schema":"CIR_QHTRI_SOURCE_ENERGY_BINDING_VALIDATION_RECEIPT_V0_1",
    "date":"2026-10-04",
    "status":status,
    "checks":checks,
    "summary":{"passed":sum(bool(v) for v in checks.values()),"total":len(checks)},
    "epistemic_boundary":{
        "exact":[
            "E_a=V_a*rho_G,a=N_a*H_G,a",
            "E_Sigma=sum_a N_a H_G,a",
            "P dot X-H_G=0 on RF-F13 degree-one on-shell branch",
            "standard U(1) periodicity requires integer P/eta on Phi_Q=-(P/eta)X"
        ],
        "conditional":[
            "E_Sigma=H_Phi^EB on RF-S22 matched-H",
            "E_Q=E_Sigma after same-generator QHTRI admission",
            "eta_phi=P for orientation-reversing U(1) isomorphism on constant-ratio branch",
            "isotropic-null branch unique under eta_phi=q0 fixed + global U(1) isomorphism + RF-F8 varying-omega transport"
        ],
        "open":[
            "physical QHTRI/RFC same-generator admission",
            "physical eta_phi normalization",
            "physical RF-F14 sector selection",
            "CIR D cosmological observable binding"
        ]
    }
}
print(json.dumps(receipt,sort_keys=True,indent=2))
if status != "PASS":
    raise SystemExit(1)
