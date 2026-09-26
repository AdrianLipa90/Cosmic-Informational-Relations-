# CIR Kerr Horizon Twist -> Log-Scale Offset Candidate v0.1

Status: EXACT KERR INVARIANT / PHASE-SCALE BINDING CANDIDATE / PROSPECTIVE ONLY
Date: 2026-09-26

## 1. Exact Kerr horizon invariants

For a subextremal Kerr source in geometric units define

  chi := a/M,
  0 <= |chi| < 1,

and

  r_+ = M + sqrt(M^2-a^2),
  r_- = M - sqrt(M^2-a^2).

The horizon angular velocity and surface gravity are

  Omega_H = a/(r_+^2+a^2),

  kappa_H = (r_+-r_-)/(2(r_+^2+a^2)).

Therefore their dimensionless ratio is exactly

  boxed[
  Upsilon_H
  := Omega_H/kappa_H
  = chi/sqrt(1-chi^2)
  ].

The mass scale M cancels.

The standard thermodynamic/Euclidean period is

  beta_H = 2 pi/kappa_H,

so the corresponding dimensionless horizon rotation potential is

  boxed[
  Theta_H := beta_H Omega_H
           = 2 pi Upsilon_H
           = 2 pi chi/sqrt(1-chi^2).
  ].

This section is standard Kerr geometry. It does not use CMB data.

## 2. Candidate PhaseNav binding

The existing CIR/TIR log-scale representation uses

  nu = ln(L/L_star)

and the candidate continuous phase-to-log-scale map

  nu = kappa_I Phi,

with

  kappa_I = ln2/(24 pi).

A new physical binding candidate is now declared:

  Phi_spin := Theta_H.

If admitted, one horizon rotational potential contributes

  delta nu_spin
  = kappa_I Theta_H
  = (ln2/12) chi/sqrt(1-chi^2).

In base-two shell units,

  delta n_spin
  := delta nu_spin/ln2

so

  boxed[
  delta n_spin
  = chi/[12 sqrt(1-chi^2)].
  ].

## 3. Spin-shifted shell law

Let the topological/dyadic parent shell index remain integer n.

The source-owned Kerr spin correction gives the candidate law

  boxed[
  nu
  = [n + delta n_spin] ln2
  ]

and therefore

  boxed[
  L/L_star
  = 2^{n + chi/[12 sqrt(1-chi^2)]}.
  ].

Equivalently for a contraction coordinate q=L_child/L_parent,

  boxed[
  q
  = 2^{-n - chi/[12 sqrt(1-chi^2)]}.
  ].

The base 2 and zero topological offset are not changed. The continuous displacement is attributed to an independently sourced Kerr horizon holonomy.

## 4. Inverse spin map

If delta n_spin is known independently,

  u := 12 delta n_spin,

then

  boxed[
  chi = u/sqrt(1+u^2)
  ].

This inverse is monotone on chi in [0,1).

## 5. Identifiability firewall

The function

  chi -> delta n_spin

maps [0,1) continuously onto [0,infinity).

Therefore, if chi is left free, the spin correction can absorb any positive fractional shell residual.

Consequently:

  CMB residual -> fit chi -> claim shell agreement

is FORBIDDEN.

A Kerr-spin-corrected shell test is predictive only if chi is fixed upstream by:
- an independently identified parent source;
- a non-CMB source geometry/holonomy receipt;
- another preregistered observable not used in the shell statistic.

## 6. Relation to the 2026 ELC result

The ELC C2/C3 amplitudes were inspected before this candidate existed.

Therefore they are permanently contaminated for this model and may be used only as a post-hoc diagnostic.

No ELC numerical proximity to a spin-shifted integer shell counts as confirmation.

## 7. Why this route is structurally preferable to arbitrary half-steps

This candidate does not change the dyadic generator T or assert a universal half-integer lattice.

Instead it keeps

  T: nu -> nu + ln2

and adds a source-owned continuous holonomy term fixed by Kerr spin.

Thus:

  integer topology
  + continuous physical holonomy
  -> noninteger observed shell coordinate.

A half-step lattice remains a separate OPEN hypothesis.

## 8. Epistemic boundary

EXACT:
- Omega_H;
- kappa_H;
- Upsilon_H=chi/sqrt(1-chi^2);
- Theta_H=2pi Upsilon_H;
- algebra following from the declared phase-scale map.

CANDIDATE:
- identify Phi_spin with Theta_H;
- add the horizon rotation potential linearly to the same unwrapped phase variable Phi used by the scale law;
- apply this source model to the AoE/CMB parent geometry.

OPEN:
- independent parent Kerr spin chi;
- proof that the CMB shadow transfer reads this horizon phase;
- independent held-out test.
