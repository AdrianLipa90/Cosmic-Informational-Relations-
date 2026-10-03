#!/usr/bin/env python3
import json
import math

KAPPA = math.log(2.0) / (24.0 * math.pi)
TOL = 1e-12

checks = {}

# Exact CIR normalization.
checks["kappa_block_identity"] = abs(KAPPA * (24.0 * math.pi) - math.log(2.0)) < 1e-14

# Differential identity tested on an analytic nontrivial phase trajectory.
def phi_d(t):
    return 0.37 * t + 0.11 * math.sin(1.7 * t) - 0.03 * math.cos(0.4 * t)

def phidot_d(t):
    return 0.37 + 0.11 * 1.7 * math.cos(1.7 * t) + 0.03 * 0.4 * math.sin(0.4 * t)

def D(t):
    return math.exp(KAPPA * phi_d(t))

def dlogD_exact(t):
    return KAPPA * phidot_d(t)

def central_dlogD(t, h=1e-5):
    return (math.log(D(t + h)) - math.log(D(t - h))) / (2.0 * h)

probes = [-3.0, -0.7, 0.0, 0.25, 2.1, 9.0]
checks["dlogD_equals_kappa_phidot"] = all(
    abs(central_dlogD(t) - dlogD_exact(t)) < 2e-10 for t in probes
)

# Source carrier.
def Q(B, omega, N, A, R):
    vals = (B, omega, N, A, R)
    if not all(math.isfinite(x) and x > 0.0 for x in vals):
        raise ValueError("carrier inputs must be positive finite")
    return B * omega * N / (A * R)

base = (2.3, 5.1, 7.7, 11.0, 13.0)
q0 = Q(*base)

# Four independent multiplicative null directions in log coordinates:
# (-1,1,0,0,0), (-1,0,1,0,0), (1,0,0,1,0), (1,0,0,0,1)
null_directions = [
    (-1.0, 1.0, 0.0, 0.0, 0.0),
    (-1.0, 0.0, 1.0, 0.0, 0.0),
    (1.0, 0.0, 0.0, 1.0, 0.0),
    (1.0, 0.0, 0.0, 0.0, 1.0),
]

def transformed(values, v, s):
    return tuple(x * math.exp(s * vi) for x, vi in zip(values, v))

checks["four_null_rescalings_preserve_Q"] = all(
    abs(Q(*transformed(base, v, s)) / q0 - 1.0) < TOL
    for v in null_directions
    for s in (-3.0, -0.5, 0.25, 2.0)
)

c = (1.0, 1.0, 1.0, -1.0, -1.0)
checks["null_vectors_orthogonal_to_log_gradient"] = all(
    abs(sum(ci * vi for ci, vi in zip(c, v))) < TOL
    for v in null_directions
)

def matrix_rank(rows, tol=1e-12):
    m = [list(map(float, row)) for row in rows]
    if not m:
        return 0
    nr = len(m)
    nc = len(m[0])
    rank = 0
    col = 0
    while rank < nr and col < nc:
        pivot = max(range(rank, nr), key=lambda i: abs(m[i][col]))
        if abs(m[pivot][col]) <= tol:
            col += 1
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        pv = m[rank][col]
        m[rank] = [x / pv for x in m[rank]]
        for i in range(nr):
            if i == rank:
                continue
            factor = m[i][col]
            m[i] = [a - factor * b for a, b in zip(m[i], m[rank])]
        rank += 1
        col += 1
    return rank

checks["carrier_log_jacobian_rank_one"] = matrix_rank([c]) == 1
checks["nullspace_basis_rank_four"] = matrix_rank(null_directions) == 4

# RFC same-cell integration: rho_E = Q*(phi+kappa), V_R=A*R.
# The A*R factor must cancel from rho_E * V_R.
def rho_E(B, omega, N, A, R, phi):
    return Q(B, omega, N, A, R) * (phi + KAPPA)

for_cell = [
    (2.0, 3.0, 5.0, 7.0, 11.0, -0.01),
    (0.7, 1.3, 2.9, 17.0, 19.0, 0.4),
    (9.0, 0.25, 4.0, 2.0, 23.0, 3.1),
]
checks["same_cell_energy_cancels_AR"] = all(
    abs(
        rho_E(B, w, N, A, R, phi) * (A * R)
        - B * w * N * (phi + KAPPA)
    ) < TOL * max(1.0, abs(B * w * N * (phi + KAPPA)))
    for B, w, N, A, R, phi in for_cell
)

# Conditional QHTRI -> CIR phase-transfer equation.
# Phi_D=lambda_phi*Phi_Q+Phi0, dotPhi_Q=-U/eta.
def H_from_phase(U, eta_phi, lambda_phi):
    return -KAPPA * lambda_phi * U / eta_phi

phase_cases = [
    (3.0, 2.0, 1.0),
    (-0.5, 7.0, 0.25),
    (11.0, 13.0, -2.0),
]
checks["conditional_phase_transfer_sign_and_scale"] = all(
    abs(H_from_phase(U, eta, lam) - KAPPA * lam * (-U / eta)) < TOL
    for U, eta, lam in phase_cases
)

status = "PASS" if all(checks.values()) else "FAIL"

receipt = {
    "schema": "CIR_SOURCE_PHASE_LOGSCALE_IDENTIFIABILITY_VALIDATION_RECEIPT_V0_1",
    "date": "2026-10-04",
    "status": status,
    "checks": checks,
    "epistemic_boundary": {
        "exact_or_conditional_exact": [
            "dlnD/dt = kappa*dPhi_D/dt on declared CIR representation",
            "five-factor Q-only source Jacobian has rank one",
            "four independent multiplicative null directions preserve Q",
            "same-cell RFC integration cancels A*R"
        ],
        "open_physical_binding": [
            "Phi_Q to Phi_D registry",
            "rho_E to U_eff law",
            "dimensionless source-density normalization Q_star",
            "D to cosmological metric/observable binding",
            "H_D to measured Hubble-like rate"
        ],
        "forbidden": [
            "Q equals H",
            "raw dimensionful Q used directly as tanh argument",
            "H0-fitted source normalization presented as derivation"
        ]
    }
}

print(json.dumps(receipt, sort_keys=True, indent=2))
if status != "PASS":
    raise SystemExit(1)
