# CIR AoE Maximum-Dispersion / Zonal-Axis Duality Lemma v0.1

Status: EXACT SO(3) REPRESENTATION LEMMA / PHYSICAL SOURCE INTERPRETATION OPEN
Date: 2026-09-26

## Problem corrected

The standard "Axis of Evil" direction used in Planck low-l alignment analyses is commonly defined by maximizing angular-momentum dispersion of each multipole.

That direction must not automatically be identified with the symmetry/source axis of an axisymmetric m=0 shadow.

## Exact lemma

Take a pure zonal multipole |ell,m=0> about a physical symmetry axis s, and let n be a trial angular-momentum-dispersion axis making angle alpha with s.

Choose s as z. In the state |ell,0>,

  <L_z^2> = 0.

Rotational symmetry around z gives

  <L_x^2> = <L_y^2>.

Since

  L^2 = L_x^2 + L_y^2 + L_z^2

and

  <L^2> = ell(ell+1),

we have

  <L_x^2> = <L_y^2> = ell(ell+1)/2.

For a unit trial axis n at polar angle alpha,

  <(L dot n)^2>
  = [ell(ell+1)/2] sin^2(alpha).

Therefore

  M_ell(alpha)
  proportional to sin^2(alpha).

Consequences:

  minimum: alpha = 0 or pi,
  maximum: alpha = pi/2.

Thus for a pure axisymmetric shadow,

  source/symmetry axis s
  is orthogonal to
  maximum-angular-momentum-dispersion axis a_AoE.

The maximizer is a great-circle family, so the maximum-dispersion axis alone cannot recover the source azimuth.

## Combined ell=2,3 consequence

If quadrupole and octupole share one zonal source axis s, the normalized angular-momentum-dispersion statistic for both has the same sin^2(alpha) dependence.

A common AoE maximum therefore specifies, in the ideal zonal limit,

  s dot a_AoE = 0,

not

  s parallel a_AoE.

This converts the AoE from a putative point direction into a plane constraint on a source-axis inverse problem.

## Zonal source-axis estimator

For a general observed map define, for each trial unoriented axis s,

  Z_ell(s)
  = |a_{ell0}^{(s)}|^2
    / sum_{m=-ell}^{ell}|a_{ell m}|^2.

Define

  Z_23(s) = Z_2(s) + Z_3(s).

The candidate common zonal axis is

  s_hat = argmax_s Z_23(s).

Equivalent field-space expression:

  a_{ell0}^{(s)}
  = sqrt[4pi/(2ell+1)] T_ell(s).

Therefore no explicit Wigner-D rotation is required if the low-l multipole field can be evaluated at s.

For a perfect common zonal source,

  Z_2=Z_3=1,
  Z_23=2,

and the recovered s is orthogonal to any maximum-dispersion AoE axis.

## Physical interpretation boundary

EXACT:
- the SO(3) expectation-value identity;
- max/min geometry for a pure m=0 multipole;
- the zonal-score definition.

CANDIDATE:
- an AoE-producing physical shadow has a substantial common zonal component;
- s_hat is related to a parent centre/source.

OPEN:
- whether the real CMB low-l field is sufficiently zonal;
- whether Kerr/tensor structure changes the 90-degree relation;
- radial binding and source identity.

## Implication for previous CIR Green tests

The earlier simple/tidal Green diagnostics evaluated g_ell at the frozen maximum-dispersion AoE axis. For an axisymmetric physical source this is not the correct source-axis projection.

Those diagnostics remain valid for the literal models they tested ("source direction = frozen AoE axis") and their FAIL results are preserved.

They must not be silently reinterpreted as tests performed at the subsequently defined zonal source axis.
