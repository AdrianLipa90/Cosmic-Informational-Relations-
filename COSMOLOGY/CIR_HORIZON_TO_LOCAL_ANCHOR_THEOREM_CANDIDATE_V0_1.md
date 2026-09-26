# CIR Horizon-to-Local-Anchor Theorem Candidate v0.1

Status: CONDITIONAL EXACT WITHIN DECLARED STANDARD METRIC FAMILY / NESTING BINDING OPEN
Date: 2026-09-26

## Purpose

The local-domain binding gate requires a dimensional anchor L_star(S) derived from the parent domain S without using the target child's mass or radius.

The existing IDT horizon closure supplies the non-extremal Euclidean regularity condition

  beta_H = 2*pi/kappa_H,
  integral kappa_H d tau_E = 2*pi.

This fixes the horizon thermal/winding periodicity, but inverse surface gravity is not by itself a universal areal radius. The map from kappa_H to a physical length is metric-family dependent.

Throughout this note kappa_H denotes physical surface gravity with dimensions of acceleration. Define

  kappa_hat_H := kappa_H/c^2,

which has dimensions 1/length.

## Proposition 1 — generic static spherical horizon

For

  ds^2 = -f(r)c^2 dt^2 + dr^2/f(r) + r^2 dOmega^2

with a simple non-extremal horizon f(r_H)=0, standard Euclidean regularity gives

  kappa_hat_H = |f'(r_H)|/2.

Therefore kappa_H determines the local slope of f at the horizon. It does not determine r_H unless the metric family and its independent parameters are declared.

This rules out a universal identification L_star = C c^2/kappa_H with one constant C across all horizon families.

## Proposition 2 — Schwarzschild anchor

For Schwarzschild,

  f(r) = 1 - r_s/r,
  r_s = 2GM/c^2.

At r=r_s,

  kappa_hat_H = 1/(2 r_s),

hence

  r_s = c^2/(2 kappa_H).

Thus an independently characterized Schwarzschild parent horizon S admits

  L_star(S) := r_s(S) = c^2/[2 kappa_H(S)].

## Proposition 3 — Kerr anchor with independently known spin

Let

  a_* = Jc/(GM^2),
  s = sqrt(1-a_*^2),
  r_+ = (GM/c^2)(1+s).

For the Kerr outer horizon,

  kappa_hat_H = s/(2 r_+).

Therefore, if a_* is independently known,

  r_+ = c^2 s/(2 kappa_H)
      = c^2 sqrt(1-a_*^2)/(2 kappa_H).

Surface gravity alone is insufficient: the extremal limit s -> 0 is explicitly degenerate and must be excluded from this non-extremal gate.

## Proposition 4 — de Sitter static-patch anchor

For the de Sitter static patch,

  f(r) = 1 - r^2/r_dS^2.

At r=r_dS,

  kappa_hat_H = 1/r_dS,

so

  r_dS = c^2/kappa_H.

The factor differs by exactly two from Schwarzschild. This is a direct demonstration that a cosmological horizon and a black-hole horizon cannot be assigned one universal kappa_H-to-radius conversion.

## Consequence for CIR local scale binding

For a declared parent domain S with a horizon boundary, define

  L_star(S) = R_H[S; metric family, independent invariants],

where R_H is the metric-specific invariant horizon radius.

Then the local log-scale coordinate is

  nu_S(L) = ln[L/L_star(S)].

Only after this parent anchor is frozen may the dyadic representation be tested:

  nu_S(L_X) ?= n(S->X) ln 2.

The target child X must not contribute to the derivation of L_star(S) or n(S->X).

## Consequence for the failed v0.2 universal-Hubble test

The v0.2 population audit used a single cosmological Hubble-scale proxy as if it were a universal parent anchor for all SMBHs. That physical binding failed.

The present theorem candidate explains why the representation did not require that assignment: horizon regularity is local, and the conversion from surface gravity to areal radius is domain/metric specific.

No retrospective reclassification of the v0.2 FAIL is allowed.

## Remaining selector gate

Even after L_star(S) is validly derived, the integer shell index remains independent:

  n(S->X) = OPEN.

Candidate sources must be upstream of child size/mass, for example:

- topological winding number of the parent-to-child relational map;
- graph nesting index with a proven phase-block correspondence;
- an orbital/holonomy index derived from parent geometry;
- a frozen observable from the proposed AoE shadow geometry.

The forbidden selector remains

  n = round(log2(L_X/L_star(S))).

## AoE-specific implication

If the Axis of Evil is tested as a projected parent-horizon geometry, the first task is not to identify a black-hole mass. It is to infer from the CMB low-l field a parent-domain invariant package sufficient to determine:

  (i) the horizon family / projection class,
  (ii) the local anchor L_star(S),
  (iii) an independent winding or shell selector n.

Only then may a dimensional child scale be predicted and compared with an astronomical object.
