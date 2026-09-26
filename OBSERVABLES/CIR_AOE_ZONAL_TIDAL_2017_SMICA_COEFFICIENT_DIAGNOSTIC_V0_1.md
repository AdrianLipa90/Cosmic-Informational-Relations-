# CIR AoE Zonal/Tidal 2017 SMICA Coefficient Diagnostic v0.1

Status: INDEPENDENT-COEFFICIENT-SET DIAGNOSTIC / PRIMARY PR2 MAP EXECUTION STILL PENDING
Date: 2026-09-26

## Provenance class

The common-zonal-axis estimator and radial-tidal Green-shadow model were frozen before this coefficient set was discovered in the session.

Source discovered afterward:

O. V. Verkhodanov, "The Problem of Non-Gaussianity and Harmonic Analysis in Observational Cosmology", proceedings "Autumn Mathematical Readings in Adygea", 2017.

The proceedings give explicit Planck SMICA coefficients for ell=2 and ell=3. The excerpt does not explicitly tag the exact Planck component-map release filename. Therefore this is not substituted for the primary frozen PR2/R2.02 HEALPix execution.

It is an independent coefficient-set diagnostic relative to the Planck-2013 coefficients used during model development.

## Published coefficients

Units: K.

Quadrupole:

  a20 =  8.361e-6
  a21 = -3.638e-6 + 8.0101e-6 i
  a22 = -1.265e-5 - 1.493e-5 i

Octupole:

  a30 = -6.261e-6
  a31 = -8.912e-6 + 8.715e-7 i
  a32 =  2.172e-5 + 1.196e-6 i
  a33 = -1.401e-5 + 3.048e-5 i

## Common zonal-axis continuous optimum

Using

  Z_ell(s) = |a_{ell0}^{(s)}|^2 / sum_m |a_{ell m}|^2

and

  Z_23 = Z_2 + Z_3,

a global continuous spherical maximization gives the unoriented axis

  s_hat = (l,b)
        = (148.95586066 deg, +5.97889441 deg),

equivalently its antipode

  (328.95586066 deg, -5.97889441 deg).

The corresponding zonal fractions are

  Z_2  = 0.7328959437,
  Z_3  = 0.5777312865,
  Z_23 = 1.3106272302.

This is a substantial common-zonal component but not a pure common m=0 field.

## Duality check against the previously frozen AoE maximum-dispersion axis

Previously frozen unoriented AoE axis:

  a_AoE = (239.98816333 deg, +68.51174192 deg).

The undirected separation is

  alpha = 84.81576891 deg.

For a pure zonal field the exact SO(3) lemma predicts alpha=90 deg.

Therefore the cross-release orthogonality residual is

  delta_perp = 5.18423109 deg.

Because the two axes originate from different coefficient/release pipelines, this is a consistency diagnostic, not a formal same-map residual.

## Tidal radial inversion at the zonal axis

At s_hat,

  g_2 = -1.6995754204e-5 K = -16.99575420 microK,
  g_3 = +3.3061839520e-5 K = +33.06183952 microK,

so

  r_23 = |g_3/g_2|
       = 1.9452999333.

For the frozen radial-tidal model:

Interior branch requires

  r_23 < 5/3,

which is false.

Therefore

  INTERIOR_BRANCH = REJECTED_BY_DOMAIN.

Exterior branch requires

  r_23 < 3,

which is true.

Hence

  q = R/d = r_23/3
    = 0.6484333111,

  n_cont = -log2(q)
         = 0.6249698885.

Using the frozen CMB screen anchor

  R_CMB = 13,873 Mpc,

the nominal exterior radial distance is

  d_out = R_CMB/q
        = 21,394.64423 Mpc
        ~= 21.39464 Gpc
        ~= 69.78 Gly comoving.

This lies beyond the frozen last-scattering screen radius and therefore cannot be interpreted as an ordinary directly observed astrophysical object inside the CMB screen.

## Sky-coordinate packet

The zonal axis corresponds approximately to ICRS

  RA  = 67.05022049 deg,
  Dec = +57.44749816 deg,

or its antipode

  RA  = 247.05022049 deg,
  Dec = -57.44749816 deg.

No source catalog was used to obtain these directions.

## Dyadic shell status

The preregistered integer-shell rule was

  n in Z_{>=1}.

The measured central value

  n_cont = 0.6249698885

does not satisfy that rule.

No formal uncertainty is supplied with the published coefficient table, so the correct status is

  INTEGER_DYADIC = CENTRAL_TENSION / NO_FORMAL_SIGMA_VERDICT.

The nearest allowed integer is n=1, with log-shell residual

  eta = n_cont - 1
      = -0.3750301115.

## Post-hoc 5/8 coincidence

Numerically,

  n_cont - 5/8
  = -3.01115e-5,

and

  q / 2^(-5/8) - 1
  ~= 2.09e-5.

This is striking numerically but was NOT preregistered.

A repository search performed after obtaining the value found no pre-existing exact rule in the current ARPL / On-Primes / Infinities bridge documents that selects the physical radial exponent n=5/8.

Therefore:

  5/8_INTERPRETATION = QUARANTINED_POST_HOC.

It may not be used to claim a prediction unless an independently dated upstream theorem is later found that already fixes this exact selector without reference to the present CMB result.

## Held-out higher multipoles

The tidal model already froze predictions for ell=4,5, but this proceedings coefficient table exposes only ell=2,3 numerically.

Therefore:

  HIGHER_MULTIPOLE_TEST = PENDING.

No figure-based or manually read-off ell=4,5 values are used.

## Verdict ledger

PASS / exact:
- zonal-axis objective evaluated from explicit coefficients;
- substantial common zonal component found;
- near-orthogonality to the previously frozen maximum-dispersion AoE axis;
- radial-tidal exterior branch is mathematically admissible.

FAIL / rejected:
- radial-tidal interior branch for this coefficient set;
- exact integer n at the central value.

OPEN:
- primary PR2/R2.02 map execution;
- coefficient covariance / foreground-systematic uncertainty;
- ell=4,5 held-out tidal ratios;
- full GR/Kerr shadow transfer;
- source identity.

No black-hole catalog comparison is performed in this artifact.
