"""CIR Lambda0–RDSS–Aharonov–Bohm reference calculator, v0.1.

Research/validation-only, not a physical gravity simulation or an inferred
spacetime model. Uses c=1, real Lorentzian metric signature (-,+,+,+).

No external dependencies. No mutable global state. All functions are pure.
Canonical TIR kappa is NOT the Einstein gravitational coupling kappa_E.
"""

from __future__ import annotations

from math import cos, exp, isfinite, log, pi, sin, sqrt
from typing import Sequence

KAPPA_TIR = log(2.0) / (24.0 * pi)
DIMENSION = 4


def _matrix4(m: Sequence[Sequence[float]]) -> list[list[float]]:
    if len(m) != 4 or any(len(row) != 4 for row in m):
        raise ValueError("Expected a 4x4 matrix")
    out = [[float(v) for v in row] for row in m]
    if any(not isfinite(v) for row in out for v in row):
        raise ValueError("Nonfinite matrix entry")
    return out


def diagonal(values: Sequence[float]) -> list[list[float]]:
    if len(values) != 4:
        raise ValueError("Expected four diagonal entries")
    return [[float(values[i]) if i == j else 0.0 for j in range(4)] for i in range(4)]


def identity4() -> list[list[float]]:
    return diagonal([1.0] * 4)


def determinant4(matrix: Sequence[Sequence[float]]) -> float:
    """Determinant using partial pivoting. For controlled small matrices only."""
    a = _matrix4(matrix)
    det = 1.0
    for k in range(4):
        pivot = max(range(k, 4), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-15:
            return 0.0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        v = a[k][k]
        det *= v
        for i in range(k + 1, 4):
            q = a[i][k] / v
            for j in range(k + 1, 4):
                a[i][j] -= q * a[k][j]
    return det


def inverse4(matrix: Sequence[Sequence[float]]) -> list[list[float]]:
    """Gauss–Jordan inverse. Raises on near-singular input."""
    a = _matrix4(matrix)
    inv = identity4()
    for k in range(4):
        pivot = max(range(k, 4), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-14:
            raise ValueError("Singular matrix")
        a[k], inv[k] = a[pivot], inv[pivot]
        a[pivot], inv[pivot] = a[k] if pivot == k else a[pivot], inv[k] if pivot == k else inv[pivot]
        # Maintain a properly ordered Gauss–Jordan state; all branches use
        # the same pivoted matrix rows and the matching inverse rows.
        div = a[k][k]
        a[k] = [v / div for v in a[k]]
        inv[k] = [v / div for v in inv[k]]
        for i in range(4):
            if i == k:
                continue
            factor = a[i][k]
            a[i] = [x - factor * y for x, y in zip(a[i], a[k])]
            inv[i] = [x - factor * y for x, y in zip(inv[i], inv[k])]
    return inv


def validate_field_tensor(F: Sequence[Sequence[float]]) -> list[list[float]]:
    f = _matrix4(F)
    for i in range(4):
        for j in range(4):
            if abs(f[i][j] + f[j][i]) > 1e-11:
                raise ValueError("F_cov must be antisymmetric")
    return f


def electromagnetic_invariant(
    inverse_metric: Sequence[Sequence[float]], F_cov: Sequence[Sequence[float]]
) -> float:
    """F_{ab} F_{cd} g^{ac} g^{bd}; indices on F are lower."""
    g = _matrix4(inverse_metric)
    F = validate_field_tensor(F_cov)
    return sum(
        F[a][b] * F[c][d] * g[a][c] * g[b][d]
        for a in range(4) for b in range(4)
        for c in range(4) for d in range(4)
    )


def candidate_u(
    inverse_metric: Sequence[Sequence[float]],
    F_cov: Sequence[Sequence[float]],
    u0: float,
    alpha: float,
) -> float:
    """Local candidate U = u0 + (alpha/4) F_ab F^ab.

    NOT a unique or physical Lambda0 identification. alpha has the units
    needed for U to be an energy-density potential.
    """
    return u0 + 0.25 * alpha * electromagnetic_invariant(inverse_metric, F_cov)


def candidate_u_metric_derivative(
    inverse_metric: Sequence[Sequence[float]],
    F_cov: Sequence[Sequence[float]],
    alpha: float,
) -> list[list[float]]:
    """Symmetric tensor dU/dg^mn for fixed covariant F and fixed alpha.

    dU/dg^mn = alpha/2 F_{m r} g^{r s} F_{n s}.
    This is a local partial derivative, not a substitute for functional
    derivatives of actions depending on metric derivatives or memory kernels.
    """
    g = _matrix4(inverse_metric)
    F = validate_field_tensor(F_cov)
    return [
        [0.5 * alpha * sum(F[m][r] * g[r][s] * F[n][s]
                           for r in range(4) for s in range(4))
         for n in range(4)]
        for m in range(4)
    ]


def potential_stress(
    inverse_metric: Sequence[Sequence[float]],
    F_cov: Sequence[Sequence[float]],
    u0: float,
    alpha: float,
) -> list[list[float]]:
    """T_U,mn = -U g_mn + 2*dU/dg^mn, for L_U = -U.

    No separate bare Maxwell contribution is computed here. Calling code
    must not include the same physical source twice.
    """
    gcov = inverse4(inverse_metric)
    u = candidate_u(inverse_metric, F_cov, u0, alpha)
    du = candidate_u_metric_derivative(inverse_metric, F_cov, alpha)
    return [[-u * gcov[m][n] + 2.0 * du[m][n] for n in range(4)]
            for m in range(4)]


def potential_action_density(
    inverse_metric: Sequence[Sequence[float]],
    F_cov: Sequence[Sequence[float]],
    u0: float,
    alpha: float,
) -> float:
    """L_U sqrt(-g) = -sqrt(-g) U for a Lorentzian inverse metric."""
    det_inv = determinant4(inverse_metric)
    if not det_inv < -1e-14:
        raise ValueError("Expected nondegenerate Lorentzian inverse metric")
    return -candidate_u(inverse_metric, F_cov, u0, alpha) / sqrt(-det_inv)


def closed_loop_phase(edge_integrals: Sequence[float]) -> float:
    """Dimensionless total q/hbar * integral A on a closed oriented cycle."""
    if len(edge_integrals) < 2:
        raise ValueError("Loop needs at least two oriented edges")
    return sum(float(x) for x in edge_integrals)


def closed_loop_wilson(edge_integrals: Sequence[float]) -> complex:
    phase = closed_loop_phase(edge_integrals)
    return complex(cos(phase), sin(phase))


def gauge_transform_loop(
    edge_integrals: Sequence[float], vertex_phases: Sequence[float]
) -> list[float]:
    """a_{i,i+1} -> a_{i,i+1}+theta[i+1]-theta[i], cyclic."""
    n = len(edge_integrals)
    if n < 2 or len(vertex_phases) != n:
        raise ValueError("Need one vertex gauge angle per directed edge")
    return [edge_integrals[i] + vertex_phases[(i + 1) % n] - vertex_phases[i]
            for i in range(n)]


def conformal_flat_einstein_diagonal(
    chi_prime: float, chi_double_prime: float
) -> tuple[float, float, float, float]:
    """G_mn for g_mn=a(eta)^2 diag(-1,1,1,1), chi=ln a.

    Derivatives are in conformal time eta. All expressions are coordinate
    lower-lower G_mn, not orthonormal-frame components.
    """
    p = float(chi_prime)
    pp = float(chi_double_prime)
    return (3.0 * p * p,) + (-(2.0 * pp + p * p),) * 3


def de_sitter_conformal_control(eta: float, H: float) -> tuple[tuple[float, ...], tuple[float, ...], float]:
    """de Sitter metric/einstein diagonal for eta<0, H>0, lambda=3H^2.

    Returns (G_mn diagonal, g_mn diagonal, Lambda). Minkowski background,
    conformal time. This checks a known GR solution, not emergent gravity.
    """
    if eta >= 0.0 or H <= 0.0:
        raise ValueError("Expected eta < 0, H > 0")
    a = -1.0 / (H * eta)
    gdiag = (-a * a, a * a, a * a, a * a)
    gEinstein = conformal_flat_einstein_diagonal(-1.0 / eta, 1.0 / (eta * eta))
    return gEinstein, gdiag, 3.0 * H * H


def bianchi_exchange_residual(
    partial_lambda: Sequence[float],
    divergence_other: Sequence[float],
    kappa_e: float,
) -> tuple[float, float, float, float]:
    """partial_nu Lambda_eff - kappa_E * nabla^mu T_other,mnu.

    Necessary equation for G+Lambda_eff*g=kappa_E*T_other.
    This is *not* a numerical covariant-derivative solver.
    """
    if len(partial_lambda) != 4 or len(divergence_other) != 4 or kappa_e <= 0.0:
        raise ValueError("Expected four components and positive kappa_E")
    return tuple(float(partial_lambda[i] - kappa_e * divergence_other[i])
                 for i in range(4))


def flrw_scalar_acceleration(kappa_e: float, kinetic: float, potential: float) -> tuple[float, float]:
    """Compare total-source and moved-potential source ledgers.

    Uses one fixed acceleration normalization and avoids counting U twice.
    """
    if kinetic < 0 or kappa_e <= 0:
        raise ValueError("Expected nonnegative kinetic and positive coupling")
    rho, p = kinetic + potential, kinetic - potential
    full = -kappa_e * (rho + 3.0 * p) / 6.0
    separated = -2.0 * kappa_e * kinetic / 3.0 + kappa_e * potential / 3.0
    return full, separated
