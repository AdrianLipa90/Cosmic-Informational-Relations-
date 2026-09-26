# CIR AoE Green-Shadow Planck-2013 Coefficient Diagnostic v0.1

Status: SAME-RELEASE DIAGNOSTIC / SIMPLE GREEN KERNEL FAIL
Date: 2026-09-26

## Scope

This test was performed after freezing the reciprocal Green-shadow v0.2 algebra and estimator, without altering the frozen axis.

It is not the primary preregistered Planck PR2/R2.02 map evaluation. The frozen axis itself was constructed from Planck-2013 low-l orientation information, so this coefficient test is same-release and must be treated as a diagnostic rather than a fully independent held-out validation.

## Frozen axis

Galactic coordinates:

  l = 239.9881633256477 deg
  b = 68.5117419161366 deg

No axis optimization was performed against the coefficients below.

## External coefficients

Source: Polastri, Gruppuso & Natoli, "CMB low multipole alignments in the LambdaCDM and Dipolar models", arXiv:1503.01611, Appendix A, Tables 4 and 5.

Units: microkelvin. Standard complex spherical-harmonic convention.

### Planck 2013 SMICA — no boost correction

  a20 = 13.089
  a21 = -1.530 + 2.497 i
  a22 = -15.503 - 17.091 i
  a30 = -5.959
  a31 = -12.841 + 1.671 i
  a32 = 22.086 + 1.670 i
  a33 = -12.465 + 29.402 i

### Planck 2013 SMICA — de-boosted

  a20 = 11.622
  a21 = -1.830 + 5.143 i
  a22 = -14.363 - 16.852 i
  a30 = -5.964
  a31 = -12.857 + 1.709 i
  a32 = 22.139 + 1.696 i
  a33 = -12.421 + 29.362 i

### Planck 2013 NILC — no boost correction

  a20 = 13.512
  a21 = -1.375 + 1.722 i
  a22 = -13.564 - 16.325 i
  a30 = -6.117
  a31 = -9.547 + 1.896 i
  a32 = 22.242 + 1.875 i
  a33 = -12.914 + 28.340 i

### Planck 2013 NILC — de-boosted

  a20 = 12.046
  a21 = -1.670 + 4.368 i
  a22 = -12.423 - 16.086 i
  a30 = -6.122
  a31 = -9.563 + 1.935 i
  a32 = 22.291 + 1.900 i
  a33 = -12.873 + 28.301 i

## Exact projection used

For each multipole,

  g_ell(a) = T_ell(a)
           = sum_{m=-ell}^{ell} a_{ell m} Y_{ell m}(a).

This equals the Legendre coefficient of the azimuthal average after rotating the frozen axis a to the pole.

The frozen simple Green kernel requires

  q_23 = |g_3/g_2| < 1.

## Results

| Map | g2 [uK] | g3 [uK] | q23=|g3/g2| | n_cont=-log2(q23) | Verdict |
|---|---:|---:|---:|---:|---|
| SMICA raw | 7.39046441 | -11.62810446 | 1.57339293 | -0.65387901 | FAIL |
| SMICA de-boosted | 5.28516016 | -11.67696593 | 2.20938734 | -1.14364636 | FAIL |
| NILC raw | 7.82862333 | -10.60269438 | 1.35434979 | -0.43760040 | FAIL |
| NILC de-boosted | 5.72508820 | -10.65138426 | 1.86047514 | -0.89567111 | FAIL |

Every tested variant violates the model-domain condition q<1.

## Verdict

  SIMPLE_POINT_GREEN_SHADOW_AT_FROZEN_AXIS = FAIL

This verdict applies to the model

  G(mu;R,d) = 1/sqrt(R^2+d^2-2Rd mu)

used as the full linear low-l shadow component with adjacent Legendre ratio q<1.

It does NOT imply

  GENERAL_BLACK_HOLE_LIKE_SHADOW_HYPOTHESIS = FAIL.

The failure is structurally informative: the observed low-l field along this frozen axis has an octupolar axial projection whose magnitude exceeds the quadrupolar axial projection. A monotone point-Green multipole ladder cannot produce that ordering.

## No rescue by inversion

The reciprocal exterior branch does not fix this result. Both d<R and d>R reduce to the same q=min(d/R,R/d)<1. Therefore q>1 is a genuine failure of this kernel, not a branch-selection issue.

## Next model gate

Any successor shadow model must be derived before further coefficient inspection and must explain why the low-l axial spectrum can satisfy

  |g3| > |g2|.

Natural mathematical possibilities include a derivative/tidal kernel, tensor rather than scalar projection, or an azimuthally non-axisymmetric Kerr-like response. None is promoted here.
