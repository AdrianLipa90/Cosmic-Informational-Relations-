# CIR Local-Domain Scale Binding Gate v0.3

Status: PHYSICAL BINDING GATE / NO NEW EMPIRICAL PROMOTION
Date: 2026-09-26

## Why v0.3 exists

The preregistered v0.2 population test falsified the over-broad assignment that every SMBH should be placed on one dyadic comb anchored to the cosmological Hubble scale. The exact representation identity remains untouched; the failed object was the universal physical anchor.

## Exact upstream representation

Let

  kappa_I = ln(2)/(24*pi),
  Phi_n = 24*pi*n,
  nu_n = kappa_I Phi_n = n ln 2.

Let

  J(nu) = -nu,
  T(nu) = nu + ln2.

Then

  J^2 = id,
  J T J = T^{-1}.

Thus the log-scale representation is an infinite-dihedral action, and the conjugate reflection

  J_n = T^n J T^{-n}

has fixed point

  nu_n = n ln2.

## Physical-domain object

For an admitted relational domain S, define a source-bound positive reference length L_star(S) without using the target child mass/radius. The physical scale coordinate is

  nu_S(L) = ln[L/L_star(S)].

Only after L_star(S) is independently fixed may the dyadic shell law be tested:

  nu_S(L_n) = n ln2,

or

  L_n = L_star(S) 2^n.

## Admissible anchor routes

An anchor is admissible only if it is determined upstream by one of the following typed structures:

1. a metric/source-defined causal boundary of S;
2. an invariant areal radius or other declared geometric boundary scalar of S;
3. a non-extremal horizon closure with independently known surface gravity kappa_H,S, together with the metric-specific map from kappa_H,S to the chosen length coordinate;
4. another source-backed invariant whose definition contains no target child mass/radius.

A galaxy effective radius, cluster radius, virial radius, Hubble radius, lensing Einstein radius, or similar observational scale is NOT automatically admissible. Its use requires a derivation that identifies that observable with L_star(S) before target evaluation.

## Existing exact horizon fact

The current IDT relativistic branch contains the Euclidean near-horizon regularity condition

  beta_H = 2*pi/kappa_H,
  integral kappa_H d tau_E = 2*pi,

for a non-extremal horizon. This gives a source-local winding anchor, but does not by itself identify kappa_H with the TIR information normalization kappa_I or select a child-shell index n.

## Required independent shell selector

A physical prediction requires an integer n(S->X) fixed without the child target mass/radius. Admissible selectors may be topological winding, graph nesting depth, a source-derived orbital index, or another independently measurable/discrete invariant.

Forbidden:

- n = round(log2(L_target/L_star));
- selecting n because it makes one object land on a shell;
- changing q=2 to the best value in a post-hoc q scan;
- changing the phase offset after target inspection.

## Prediction packet

For a parent domain S and child X, freeze before evaluation:

  L_star(S),
  n(S->X),
  predicted L_X = L_star(S) 2^n,
  allowed spin/metric correction,
  directional prediction if present,
  uncertainty propagation,
  PASS/TENSION/FAIL threshold.

The primary residual is

  Delta_n = ln[L_X/L_star(S)] - n ln2.

The normalized shell residual is

  eta_n = Delta_n/ln2.

## Current verdict

EXACT:
- phase-block/log-dyadic identity;
- infinite-dihedral log-scale representation;
- local self-dual axes at n ln2.

FALSIFIED IN v0.2:
- one universal Hubble anchor applied to the full SMBH population.

OPEN:
- source theorem for L_star(S) in the black-hole/cosmological nesting sector;
- independent shell-index selector n(S->X);
- physical identification of the AoE with a particular parent/child shadow geometry.
