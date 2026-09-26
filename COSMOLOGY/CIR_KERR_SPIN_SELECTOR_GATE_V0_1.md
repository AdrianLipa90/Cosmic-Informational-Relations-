# CIR Kerr Spin-Selector Gate v0.1

Status: SELECTOR AUDIT / CHI NOT FIXED BY CURRENT HORIZON WINDING
Date: 2026-09-26

## Question

Does the current TIR/IDT horizon-winding canon independently select the Kerr dimensionless spin

  chi=a/M

needed by the polar-shadow forward family?

Current verdict:

  NO.

## Existing exact horizon structure

The present IDT canon contains the non-extremal Euclidean horizon closure

  beta_H=2pi/kappa_H,

  integral kappa_H d tau_E = 2pi,

and standard spin-structure consequences:

  bosonic periodic modes:
    omega_n^B = n kappa_H,

  fermionic antiperiodic modes:
    omega_n^F = (n+1/2) kappa_H.

These facts constrain field periodicity/spin structure relative to surface gravity.

## Missing Kerr selector

For Kerr,

  Omega_H/kappa_H
  = chi/sqrt(1-chi^2).

Neither the bosonic/fermionic thermal boundary condition nor the primitive 2pi Euclidean frame winding fixes a numerical value of this ratio.

In particular, the current canon does NOT prove

  beta_H Omega_H = 24pi m,

  beta_H Omega_H = 12pi m,

or any other discrete rotational-potential rule.

Imposing such a condition now would be a new model assumption and, after the already-seen CMB residuals, risks post-hoc spin quantization.

## Consequence

The source-family parameter

  chi

remains OPEN.

Admissible future selectors include:
- an independently identified Kerr-like parent with measured/inferred spin from non-CMB observables;
- a separately proved horizon holonomy theorem involving Omega_H, not merely kappa_H;
- a source graph/topological invariant that maps to Omega_H/kappa_H before CMB evaluation.

Forbidden:
- choose chi to land on a desired CMB shell;
- infer chi from ELC C2/C3 and call that an independent prediction;
- equate 24pi normalization with Kerr rotational potential without a bridge theorem.

## Status

  PHOTON_RADIUS_SELECTOR = CLOSED GIVEN chi

  GL3_DEFORMATION_SELECTOR = CLOSED GIVEN chi

  HORIZON_TWIST = CLOSED GIVEN chi

  KERR_SPIN chi = OPEN

Thus the absolute forward family is now one continuous source parameter away from a point prediction.
