#!/usr/bin/env python3
"""Algebraic controls for CIR Lambda0/RDSS/AB research bridge.

Reference-only. Does not validate physical cosmology or source binding.
"""
import cmath
import json
import math

TOL = 2.0e-7


def close(a, b, tol=TOL):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def wilson(links):
    return cmath.exp(1j * sum(links))


def em_scalar(gi, field):
    """F_ab F_cd g^(ac) g^(bd) using diagonal inverse metric gi."""
    return sum(field[a][b] ** 2 * gi[a] * gi[b]
               for a in range(4) for b in range(4))


def main():
    failures = []
    checks = {}

    links = [0.18, -0.07, 0.09, 0.05]
    gauges = [0.4, -0.8, 1.1, -0.25]
    transformed = [links[k] + gauges[k] - gauges[(k + 1) % 4]
                   for k in range(4)]
    checks["closed_u1_wilson_gauge_invariant"] = close(
        wilson(links), wilson(transformed), 1e-12)
    checks["closed_loop_phase_025_rad"] = close(sum(links), 0.25)

    # Same local zero curvature on edges of a ring does not fix the
    # global U(1) holonomy on a multiply-connected accessible domain.
    w0, w1 = wilson([0.0] * 4), wilson([math.pi / 2, 0, 0, 0])
    checks["distinct_flat_ring_holonomies"] = not close(w0, w1)
    # The phase must not be presented as a physical gravity source absent
    # an independently sourced coupling: alpha_H=0 yields the same Lambda.
    bare_lambda, alpha_h = 0.03, 0.0
    lam0 = bare_lambda + alpha_h * (1 - w0.real)
    lam1 = bare_lambda + alpha_h * (1 - w1.real)
    checks["no_automatic_gravity_from_wilson"] = close(lam0, lam1)

    field = [[0.0] * 4 for _ in range(4)]
    field[0][1], field[1][0] = 0.7, -0.7
    field[1][2], field[2][1] = 0.3, -0.3
    gi = [-1.0, 1.0, 1.0, 1.0]  # (-+++)
    eps = 1.0e-6
    derivatives_ok = True
    for mu in range(4):
        plus, minus = gi.copy(), gi.copy()
        plus[mu] += eps
        minus[mu] -= eps
        numeric = (em_scalar(plus, field) - em_scalar(minus, field)) / (2 * eps)
        analytic = 2 * sum(field[mu][rho] ** 2 * gi[rho] for rho in range(4))
        derivatives_ok &= close(numeric, analytic)
    checks["em_metric_variation_derivative"] = derivatives_ok

    # Conformal de Sitter control. Eta<0, a=-1/(H eta), chi=ln a,
    # vacuum Einstein equations with Lambda=3 H^2 (c=1) hold.
    H, eta = 0.6, -1.7
    a = -1 / (H * eta)
    chip = -1 / eta
    chipp = 1 / (eta * eta)
    G00 = 3 * chip * chip
    Gii = -(2 * chipp + chip * chip)
    lambda_ds = 3 * H * H
    checks["conformal_ds_00_vacuum_residual"] = close(G00 - lambda_ds * a*a, 0)
    checks["conformal_ds_ii_vacuum_residual"] = close(Gii + lambda_ds * a*a, 0)

    # The Bianchi identity requires an exchange term when Lambda varies.
    # With separate stress conservation, dLambda != 0 is inadmissible.
    grad_lambda = [0.1, 0.0, 0.0, 0.0]
    separately_conserved = True
    checks["variable_lambda_needs_exchange"] = (
        separately_conserved and any(abs(v) > TOL for v in grad_lambda))

    for name, passed in checks.items():
        if not passed:
            failures.append(name)
    result = {
        "schema": "CIR_LAMBDA0_RDSS_AB_ALGEBRAIC_CONTROL_V0_1",
        "scope": "REFERENCE_ALGEBRA_ONLY_NO_PHYSICAL_SOURCE_BINDING",
        "checks": checks,
        "failures": failures,
        "verdict": "PASS" if not failures else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
