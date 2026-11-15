"""CIR AB matter-mediated metric-source diagnostic v0.2 (offline only).

Mathematical controls for a charged phase field on a circle with nontrivial
U(1) holonomy. In the accessible ring, F=0, but the covariant phase gradient
may be nonzero because of the global Wilson loop. Such matter stress may source
gravity only after a physical metric response and full Einstein closure are
specified. This module does NOT solve Einstein equations.

Flat background metric: (-,+,+,+), c=1. The ring length L, transverse area A,
and f2>0 (phase stiffness per unit transverse area) are declared positive.
All outputs are deterministic, with no fitting or external dependencies.
"""
from __future__ import annotations

from cmath import exp as cexp
from math import cos, floor, isfinite, pi, sin
from typing import Sequence

TWO_PI = 2.0 * pi


def _finite(*numbers: float) -> None:
    if not all(isfinite(float(v)) for v in numbers):
        raise ValueError("all parameters must be finite")


def _positive(**kwargs: float) -> None:
    _finite(*kwargs.values())
    if any(v <= 0 for v in kwargs.values()):
        raise ValueError("length, area and stiffness must be positive")


def preferred_winding(flux_phase: float) -> int:
    """Ground-state winding minimizing (2*pi*m - flux_phase)^2.

    Exactly at the half-flux quantum the minimizer is degenerate; this
    conventional tie-breaking picks the upper integer. Avoid differentiating
    the minimum energy at that cusp.
    """
    _finite(flux_phase)
    return floor(flux_phase / TWO_PI + 0.5)


def phase_mismatch(flux_phase: float, winding: int | None = None) -> float:
    _finite(flux_phase)
    if winding is None:
        winding = preferred_winding(flux_phase)
    if not isinstance(winding, int):
        raise TypeError("winding must be integer")
    return TWO_PI * winding - flux_phase


def continuum_ring_energy(flux_phase: float, length: float, stiffness: float,
                          winding: int | None = None) -> float:
    """E_m = stiffness/(2 L) (2*pi*m - phi)^2.

    stiffness = f2 * transverse_area for a constant-modulus 3+1 scalar.
    """
    _positive(length=length, stiffness=stiffness)
    d = phase_mismatch(flux_phase, winding)
    return stiffness * d * d / (2.0 * length)


def finite_ring_energy(psi: Sequence[complex], edge_phases: Sequence[float],
                       length: float, stiffness: float) -> float:
    """Gauge-invariant N-link discretization of constant-modulus phase kinetic energy.

    E = stiffness*N/(2L)*sum(|psi[j+1] - exp(i*a[j])*psi[j]|**2).
    Edge phases a[j] are q/hbar line integrals, j -> (j+1) modulo N.
    """
    _positive(length=length, stiffness=stiffness)
    n = len(psi)
    if n < 3 or len(edge_phases) != n:
        raise ValueError("ring requires matching arrays of at least 3 sites")
    _finite(*edge_phases)
    return (stiffness * n / (2.0 * length) *
            sum(abs(complex(psi[(j + 1) % n]) -
                    cexp(1j * edge_phases[j]) * complex(psi[j])) ** 2
                for j in range(n)))


def uniform_ring_configuration(n: int, flux_phase: float,
                               winding: int = 0) -> tuple[list[complex], list[float]]:
    """Constant-modulus charge field and uniform link potential on the ring."""
    if not isinstance(n, int) or n < 3 or not isinstance(winding, int):
        raise ValueError("n>=3 and integer winding required")
    _finite(flux_phase)
    return ([cexp(1j * TWO_PI * winding * j/n) for j in range(n)],
            [flux_phase / n] * n)


def transform_ring_gauge(psi: Sequence[complex], edge_phases: Sequence[float],
                         vertex_angles: Sequence[float]) -> tuple[list[complex], list[float]]:
    """psi_j -> exp(i*chi_j) psi_j, a_j -> a_j+chi_(j+1)-chi_j."""
    n = len(psi)
    if n < 3 or n != len(edge_phases) or n != len(vertex_angles):
        raise ValueError("matching arrays of at least 3 sites required")
    _finite(*edge_phases, *vertex_angles)
    return ([cexp(1j * vertex_angles[j]) * complex(psi[j]) for j in range(n)],
            [edge_phases[j] + vertex_angles[(j+1) % n] - vertex_angles[j]
             for j in range(n)])


def finite_ring_uniform_energy(n: int, flux_phase: float, length: float,
                               stiffness: float, winding: int = 0) -> float:
    """Closed form: E_N = stiffness*N^2/L*(1-cos((2*pi*m-phi)/N))."""
    _positive(length=length, stiffness=stiffness)
    if not isinstance(n, int) or n < 3:
        raise ValueError("n must be integer >=3")
    d = phase_mismatch(flux_phase, winding)
    return stiffness * n * n / length * (1.0 - cos(d / n))


def phase_stress_covariant(flux_phase: float, length: float, f_squared: float,
                           winding: int | None = None) -> tuple[float, float, float, float]:
    """Flat 3+1 scalar-phase T_{mu nu} diagonal (rho, rho, -rho, -rho).

    For L_phi=-1/2*f2*g^mu nu v_mu v_nu, v=(0,(2*pi*m-phi)/L,0,0),
    F=0 locally and no other matter/Maxwell/potential contributions.
    This stress is anisotropic; it is NOT a cosmological constant term.
    """
    _positive(length=length)
    _finite(f_squared)
    if f_squared < 0:
        raise ValueError("f_squared cannot be negative")
    d = phase_mismatch(flux_phase, winding)
    rho = 0.5 * f_squared * (d / length) ** 2
    return (rho, rho, -rho, -rho)


def phase_stress_mixed(flux_phase: float, length: float, f_squared: float,
                       winding: int | None = None) -> tuple[float, float, float, float]:
    """T^mu_nu in flat (-,+,+,+): diag(-rho, rho, -rho, -rho)."""
    cov = phase_stress_covariant(flux_phase, length, f_squared, winding)
    return (-cov[0], cov[1], cov[2], cov[3])


def box_phase_energy(flux_phase: float, length: float,
                     transverse_area: float, f_squared: float,
                     winding: int | None = None) -> float:
    """Homogeneous constant-modulus phase energy on S^1 x transverse area."""
    _positive(length=length, transverse_area=transverse_area)
    _finite(f_squared)
    if f_squared < 0:
        raise ValueError("f_squared cannot be negative")
    d = phase_mismatch(flux_phase, winding)
    return 0.5 * f_squared * transverse_area * d * d / length


def matter_flux_current(flux_phase: float, length: float,
                        stiffness: float, winding: int | None = None) -> float:
    """Persistent phase-response current I_phi = -dE/dphi for fixed winding."""
    _positive(length=length, stiffness=stiffness)
    return stiffness * phase_mismatch(flux_phase, winding) / length


def wilson_real(flux_phase: float) -> float:
    _finite(flux_phase)
    return cos(flux_phase)


def closed_wilson(edge_phases: Sequence[float]) -> complex:
    """Wilson loop built from oriented dimensionless link phases."""
    if len(edge_phases) < 3:
        raise ValueError("ring requires at least three directed edges")
    _finite(*edge_phases)
    phase = sum(edge_phases)
    return complex(cos(phase), sin(phase))
