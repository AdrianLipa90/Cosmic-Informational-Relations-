# CIR AoE Same-Map Zonal / Max-Dispersion Null Audit v0.1

Status: SAME-COEFFICIENT GEOMETRY AUDIT / ORTHOGONALITY NOT EVIDENTIAL
Date: 2026-09-26

## Purpose

The previous cross-release diagnostic found the common-zonal axis nearly orthogonal to a separately frozen Axis-of-Evil maximum-dispersion axis. This audit removes that release mismatch and asks a stricter question:

Does the same set of ell=2,3 coefficients produce an unusually orthogonal pair of estimators, or is near-orthogonality largely built into the estimator geometry?

## Input

Use exactly the 2017 published SMICA coefficients already recorded in

  OBSERVABLES/CIR_AOE_ZONAL_TIDAL_2017_SMICA_COEFFICIENT_DIAGNOSTIC_V0_1.md.

No black-hole/source catalogue enters this audit.

## 1. Same-map maximum-dispersion axis

For each multipole define the normalized angular-momentum quadratic form

  Q_ij^(ell)
  = Re[a^dagger {L_i,L_j}/2 a]
    / [P_ell ell(ell+1)],

with

  P_ell = sum_m |a_{ell m}|^2.

The joint ell=2,3 maximum-dispersion axis is the top eigenvector of

  Q = Q^(2) + Q^(3).

For the 2017 coefficients:

  joint AoE axis
  (l,b) = (241.53016626 deg, +61.32143535 deg)

up to antipodal equivalence.

Joint eigenvalues:

  0.28558834,
  0.34171746,
  1.37269420.

Individual top-eigenvector axes:

  ell=2:
    (l,b) = (244.87677450 deg, +58.96551433 deg)

  ell=3:
    (l,b) = (237.97529966 deg, +63.12137751 deg)

Their undirected angular separation is

  alpha_23 = 5.32658073 deg.

Under independent isotropic unoriented axes,

  P(alpha <= alpha_23)
  = 1 - cos(alpha_23)
  = 0.00431826.

This reproduces a genuinely uncommon quadrupole/octupole axis alignment at the level of this simple isotropic-axis null. It does not identify a physical mechanism.

## 2. Same-map common-zonal axis

Maximize

  Z_23(s)=Z_2(s)+Z_3(s),

  Z_ell(s)=|a_{ell0}^{(s)}|^2/P_ell.

Continuous refinement gives

  zonal axis
  (l,b) = (148.95585845 deg, +5.97888785 deg),

with

  Z_23 = 1.31062723024.

This reproduces the previously recorded zonal solution.

The undirected separation from the SAME-MAP joint maximum-dispersion axis is

  alpha_zm = 85.98907183 deg,

so the orthogonality residual is

  delta_perp = |90 deg - alpha_zm|
             = 4.01092817 deg.

## 3. Isotropic Monte Carlo null

Generate independent isotropic real Gaussian multipoles for ell=2 and ell=3:

  a_{ell,0} ~ N(0,1),

  Re a_{ell,m}, Im a_{ell,m}
  ~ N(0,1/2), m>0,

with the real-sky condition

  a_{ell,-m}=(-1)^m a_{ell,m}^*.

For every realization:

1. obtain the joint maximum-dispersion axis from the top eigenvector of Q;
2. obtain the common-zonal axis by maximizing Z_23 over a deterministic Fibonacci sphere;
3. measure delta_perp and Z_23,max.

Primary run:

  N = 100000
  seed = 20260926
  grid = 4096 directions

Using the same grid resolution for observed and null:

  P(delta_perp <= observed)
  ~= 0.32984,

  P(Z_23,max >= observed)
  ~= 0.22372,

  P(both)
  ~= 0.13467.

Higher-grid control:

  N = 30000
  seed = 2026092602
  grid = 8192 directions

gave

  P(delta_perp <= observed)
  ~= 0.30026,

  P(Z_23,max >= observed)
  ~= 0.22736,

  P(both)
  ~= 0.12446.

The finite-grid change does not alter the conclusion.

## 4. Verdict

  SAME_MAP_ELL2_ELL3_MAXDISP_ALIGNMENT = ANOMALOUS_UNDER_SIMPLE_ISOTROPIC_AXIS_NULL

with simple null probability about 0.43 percent for a separation this small or smaller.

But:

  ZONAL_MAXDISP_NEAR_ORTHOGONALITY = NOT_ANOMALOUS

and

  COMMON_ZONAL_MAXIMUM_SCORE = NOT_ANOMALOUS

under the declared Gaussian low-l null.

Therefore the previous near-90-degree zonal/AoE geometry is an estimator-geometry consequence often produced by random low-l skies. It must not be used as independent evidence for a source axis or black-hole-like shadow.

## 5. Consequence for the physical branch

Preserve:
- the exact SO(3) zonal/max-dispersion lemma;
- the real ell=2/3 alignment anomaly;
- the zonal estimator as an inverse coordinate construction.

Demote:
- near-orthogonality itself as a discriminator;
- Z_23=1.31 as evidence for a common zonal physical source.

The next physical test should therefore use an observable not mechanically coupled to the same temperature multipoles, preferably a tensor/polarization channel or a genuinely independent CMB release with a fully frozen transfer law.

## Epistemic boundary

The 0.43 percent number is a simple isotropic independent-axis null, not a global look-elsewhere significance for the historical Axis-of-Evil literature. A complete cosmological anomaly significance analysis must account for estimator selection, masks, foreground treatment and a-posteriori choices.
