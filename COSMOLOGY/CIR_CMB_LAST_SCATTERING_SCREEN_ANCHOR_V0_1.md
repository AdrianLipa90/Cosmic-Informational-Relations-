# CIR CMB Last-Scattering Screen Anchor v0.1

Status: EXTERNAL COSMOLOGICAL ANCHOR / FROZEN BEFORE GREEN-SHADOW COEFFICIENT EVALUATION
Date: 2026-09-26

## Purpose

The reciprocal Green-shadow model requires an observation-sphere radius R fixed independently of the inferred low-l ratio q and independently of any black-hole/source catalog.

For the specific interpretation in which the observed shadow is projected onto the CMB last-scattering screen, choose the present-day transverse comoving radius of the photon-decoupling surface.

## Frozen external source

Planck Collaboration VI, "Planck 2018 results. VI. Cosmological parameters",
Astronomy & Astrophysics 641, A6 (2020), DOI 10.1051/0004-6361/201833910,
baseline TT,TE,EE+lowE+lensing parameter set.

Published derived parameters include, for this baseline, approximately

  z_* = 1089.92 +/- 0.25,
  r_* = 144.43 +/- 0.26 Mpc,
  100 theta_* = 1.04110 +/- 0.00031,
  D_M(z_*) = 13.873 +/- 0.025 Gpc.

The last quantity is the transverse comoving distance to the last-scattering surface. It is consistent with r_*/theta_* at the quoted central values.

## Frozen screen radius

Define

  R_CMB := D_M(z_*) = 13.873 Gpc = 13,873 Mpc.

For geometric intuition only,

  R_CMB ~= 45.25 billion light-years

in present-day comoving distance units.

The Planck quoted uncertainty is

  sigma_R ~= 0.025 Gpc.

No AoE low-l coefficient and no target/source property enters this anchor.

## Coordinate convention

All radial predictions generated from this anchor are present-day comoving radial distances from the observer.

They are not:
- light-travel times;
- proper distances at recombination;
- Schwarzschild radii;
- target black-hole distances inferred from a catalog.

## Reciprocal shell consequence

For a measured Green ratio q,

  d_in  = R_CMB q,
  d_out = R_CMB/q.

Under the dyadic sub-hypothesis q=2^{-n},

  d_in(n)  = R_CMB 2^{-n},
  d_out(n) = R_CMB 2^{+n}.

The outer branch can lie outside the observable last-scattering volume. That is a physical interpretation issue, not grounds to discard the branch after seeing a target catalog.

## Frozen inner-shell ladder

Using the nominal R_CMB=13,873 Mpc:

| n | d_in [Mpc] | d_in [Gly, comoving] |
|---:|---:|---:|
| 1 | 6936.5000 | 22.6238 |
| 2 | 3468.2500 | 11.3119 |
| 3 | 1734.1250 | 5.6560 |
| 4 | 867.0625 | 2.8280 |
| 5 | 433.53125 | 1.4140 |
| 6 | 216.765625 | 0.7070 |
| 7 | 108.3828125 | 0.3535 |
| 8 | 54.19140625 | 0.17675 |
| 9 | 27.095703125 | 0.08837 |
| 10 | 13.5478515625 | 0.04419 |
| 11 | 6.77392578125 | 0.02209 |
| 12 | 3.386962890625 | 0.01105 |

The table is a pre-data shell lattice. It does not select n.

## Uncertainty rule

Once n is selected independently by q_23, the Planck screen-radius uncertainty scales linearly:

  sigma[d_in(n)] = sigma_R 2^{-n},
  sigma[d_out(n)] = sigma_R 2^{+n},

before adding the much larger expected uncertainty from the low-l coefficient inversion.

Correlations in the underlying Planck derived parameters must not be reconstructed by naïvely treating r_* and theta_* as independent if a higher-precision covariance is later needed; use the published D_M posterior or chains.

## No-retune rule

R_CMB is now frozen for this CMB-screen branch. Changing the radial anchor after q_23 is measured retires this branch version and requires a new prospective freeze.
