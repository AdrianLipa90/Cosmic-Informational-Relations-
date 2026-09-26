# CIR AoE Axis-Convention Walk-Back v0.1

Status: CORRECTION / APPEND-ONLY / NO SILENT REWRITE
Date: 2026-09-26

## Error found

Earlier Green-shadow artifacts used the frozen Axis-of-Evil preferred direction as though it were the symmetry axis of an axisymmetric Legendre field and therefore extracted/compared the m=0 coefficient in the frame whose z-axis was the AoE direction.

That identification is not compatible with the standard maximum-angular-momentum-dispersion definition of the AoE preferred axis.

## Exact reason

Let an axisymmetric multipole be the pure state

  |psi_l> = |l,m=0>_s

about physical symmetry axis s.

For a candidate angular-momentum axis n making angle beta with s,

  M_l(n)
  := <psi_l| L_n^2 |psi_l> / <psi_l|psi_l>.

For |l,0>,

  <L_s^2> = 0,

and rotational symmetry in the transverse plane gives

  <L_x^2> = <L_y^2> = l(l+1)/2.

Therefore

  M_l(beta)
  = [l(l+1)/2] sin^2(beta).

Consequences:

- M_l is MINIMAL on the physical symmetry axis s;
- M_l is MAXIMAL for every n perpendicular to s;
- the maximizing direction is a degenerate great circle, not a unique axis.

Thus a pure zonal/axisymmetric P_l(s·n) shadow cannot by itself identify a unique AoE maximum-dispersion axis.

## Impacted artifacts

### CIR_AOE_GREEN_SHADOW_PLANCK2013_DIAGNOSTIC_V0_1

The numerical g2/g3 values remain reproducible as projections along the frozen AoE direction, but the verdict

  SIMPLE_POINT_GREEN_SHADOW_AT_FROZEN_AXIS_FAIL

is reclassified as

  NON_ADJUDICATING_INVALID_AXIS_TO_M0_IDENTIFICATION.

It must not be cited as a physical falsification of a general scalar Green-shadow model.

### CIR_AOE_INTERIOR_TIDAL_GREEN_SHADOW_MODEL_V0_3

The v0.3 tidal derivative algebra is mathematically correct for a zonal source axis, but the proposed identification

  frozen AoE maximum-dispersion axis == zonal m=0 symmetry axis

is invalid.

Therefore v0.3 is

  RETIRED_BEFORE_INDEPENDENT_HELDOUT_EVALUATION.

Its freeze remains in repository history and is not deleted.

## Unaffected artifacts

The following results do not depend on the incorrect AoE-axis/m=0 identification and remain unchanged:

- CIR Local Log-Scale Dihedral Lemma v0.1;
- the v0.2 SMBH population FAIL for a universal Hubble anchor;
- CIR Local-Domain Scale Binding Gate v0.3;
- metric-specific horizon-to-local-anchor theorem candidate;
- CMB last-scattering screen anchor.

## Correct observable interface

For a frozen AoE axis a, rotate the sky so that a is the z-axis and use the complete harmonic vector

  a_l^(a) = {a_{lm}^{(a)} : -l <= m <= l}.

Define total power

  P_l = sum_m |a_{lm}^{(a)}|^2,

planar/high-|m| power

  P_l^planar = |a_{l,l}^{(a)}|^2 + |a_{l,-l}^{(a)}|^2,

and planar fraction

  f_l^planar = P_l^planar/P_l.

The maximum-angular-momentum-dispersion functional is

  M_l(a)
  = [sum_m m^2 |a_{lm}^{(a)}|^2]/P_l.

A physical shadow model intended to explain the AoE must predict these high-|m|/dispersion observables in the same axis convention. It may not substitute the m=0 Legendre projection.

## Required next gate

Before any new low-l coefficient evaluation, a successor model must provide:

1. a forward map from its physical source/boundary geometry to a_{lm};
2. the predicted maximizing angular-momentum-dispersion axis;
3. the predicted planar fractions for l=2 and l=3;
4. a scale estimator constructed from observables compatible with that same forward map;
5. held-out l>=4 predictions.

No existing q estimate from the retired m=0 pipeline may be reused as a prospective result.
