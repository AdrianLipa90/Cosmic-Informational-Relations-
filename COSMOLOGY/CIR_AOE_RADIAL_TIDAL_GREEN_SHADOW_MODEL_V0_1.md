# CIR AoE Radial-Tidal Green-Shadow Model v0.1

Status: POST-DIAGNOSTIC-MOTIVATED / PROSPECTIVE FOR NEW MAP COEFFICIENTS
Date: 2026-09-26

## Provenance warning

This model is introduced only after the simple scalar Green kernel failed against published Planck-2013 SMICA/NILC coefficients at the frozen axis.

Therefore those Planck-2013 coefficients are DEVELOPMENT / EXPLORATORY DATA for this model and may not be counted as prospective confirmation.

The next evidential test must use a separately frozen map/coefficient product not used to choose this operator.

## Physical motivation

A gravitational observable is generally not the Newtonian/Green potential itself. Relative acceleration and curvature are controlled by second derivatives of the potential. The simplest scalar proxy for a radial tidal response on an observation sphere is therefore

  E_RR(mu;R,d) := d^2/dR^2 [1/sqrt(R^2+d^2-2Rd mu)].

This is not yet a full GR Weyl-tensor or Kerr transfer calculation. It is the minimal curvature-like successor to the failed scalar kernel.

## Interior-source branch: d<R

Let

  x := d/R,  0<x<1.

The Green expansion is

  G = sum_{ell>=0} d^ell R^{-(ell+1)} P_ell(mu).

Taking two derivatives with respect to the field radius R,

  E_RR
  = R^{-3} sum_{ell>=0} (ell+1)(ell+2) x^ell P_ell(mu).

Hence the Legendre coefficients obey

  |g_{ell+1}/g_ell|
  = [(ell+3)/(ell+1)] x.

For ell=2 -> 3,

  r23 := |g_3/g_2| = (5/3) x,

so

  x = (3/5) r23.

The interior branch exists only if

  r23 < 5/3.

## Exterior-source branch: d>R

Let

  q := R/d,  0<q<1.

Then

  G = sum_{ell>=0} R^ell d^{-(ell+1)} P_ell(mu),

and

  E_RR
  = d^{-3} sum_{ell>=2} ell(ell-1) q^{ell-2} P_ell(mu).

Therefore

  |g_{ell+1}/g_ell|
  = [(ell+1)/(ell-1)] q.

For ell=2 -> 3,

  r23 = 3 q,

so

  q = r23/3.

The exterior branch exists if

  r23 < 3.

## Branch discriminator

The interval

  0 < r23 < 5/3

permits both the interior and exterior radial-tidal branches.

The interval

  5/3 <= r23 < 3

forbids the interior branch and selects the exterior branch within this model.

Values

  r23 >= 3

falsify both radial-tidal point-source branches.

This branch rule is frozen before the next map/coefficient evaluation.

## Exact ALM estimator

At the fixed axis a,

  g_ell = sqrt[(2ell+1)/(4pi)] a_{ell0}^{(a)}
        = T_ell(a).

Thus

  r23 = sqrt(7/5) |a_{30}^{(a)}/a_{20}^{(a)}|.

No axis optimization is permitted after coefficient inspection.

## Dyadic geometric shell test

The dyadic law applies to the geometric radial ratio, not directly to r23.

Interior:
  x = d/R = (3/5) r23,
  n_in = -log2(x).

Exterior:
  q = R/d = r23/3,
  n_out = -log2(q).

The candidate dyadic condition is

  n_in in Z_{>=1}

or

  n_out in Z_{>=1}

for the corresponding admitted branch.

With the frozen CMB screen anchor R_CMB,

  d_in  = R_CMB x,
  d_out = R_CMB/q.

## Held-out multipole predictions

Infer the radial ratio only from ell=2,3.

Then:

### Interior branch

  |g_4/g_3| = (3/2)x = (9/10) r23,
  |g_5/g_4| = (7/5)x = (21/25) r23.

### Exterior branch

  |g_4/g_3| = (5/2)q = (5/6) r23,
  |g_5/g_4| = 2q = (2/3) r23.

These ell=4,5 relations are prospective discriminators and may not be altered after those coefficients are inspected.

## Why second derivative is not an arbitrary polynomial rescue

For the derivative family d^kG/dR^k:

- k=0 is the scalar potential kernel already tested and failed;
- k=1 is a force-like radial response;
- k=2 is the first tidal/curvature-like response and still retains the quadrupole;
- k>2 annihilates or qualitatively changes the low-order hierarchy in a way that no longer provides the same quadrupole anchor.

The physical motivation for k=2 is curvature/tidal response, not numerical optimization of k against r23.

Nevertheless, because the operator was selected after observing failure of k=0 on Planck-2013 coefficients, only new data can validate it.

## Epistemic boundary

EXACT:
- both Legendre derivative expansions;
- branch inequalities;
- ALM normalization;
- held-out coefficient-ratio formulas.

CANDIDATE:
- the AoE shadow is proportional to E_RR;
- the geometric ratio is dyadic;
- the CMB last-scattering screen is the appropriate R.

OPEN:
- full GR/Kerr transfer function;
- tensor/polarization signature;
- source identity.
