# CIR AoE Tidal-Shadow HEALPix Evaluation Pipeline v0.1

Status: EXECUTABLE SPECIFICATION / REAL-DATA EXECUTION PENDING MAP BYTES
Date: 2026-09-26

## Frozen input

Primary map:

  COM_CMB_IQU-smica_1024_R2.02_full.fits

Planck Release 2 SMICA full-mission CMB map.

Primary field:

  field 0 / I_STOKES.

The full-sky released field is used directly. This v0.1 does not add a mask, optimize an inpainting rule, or rotate the axis to improve the result.

## Frozen geometry

Axis:

  Galactic l = 239.9881633256477 deg
  Galactic b = 68.5117419161366 deg

Screen anchor:

  R_CMB = 13,873 Mpc comoving.

Tidal model:

  E_RR = d^2 G/dR^2.

## Harmonic extraction

Compute real-map spherical harmonics through ell=5 from the released temperature field.

Recommended implementation:

  healpy.map2alm(T, lmax=5, iter=3, pol=False, use_weights=False, use_pixel_weights=False)

No map-dependent parameter optimization is allowed.

For each ell=2..5 evaluate the multipole at the fixed axis:

  g_ell = T_ell(a)
        = sum_m a_{ell m} Y_{ell m}(a).

For a real map this is evaluated from stored m>=0 coefficients as

  g_ell
  = a_{ell0}Y_{ell0}
    + 2 Re sum_{m=1}^{ell} a_{ell m}Y_{ell m}.

## Primary quantity

  r23 = |g3/g2|.

Fail closed if g2 is zero/non-finite.

Model branch domains:

  interior allowed iff 0<r23<5/3,
  exterior allowed iff 0<r23<3,
  both fail iff r23>=3.

## Derived geometry

Interior, if allowed:

  x = d/R = (3/5)r23,
  n_in = -log2(x),
  d_in = R_CMB x.

Exterior, if allowed:

  q = R/d = r23/3,
  n_out = -log2(q),
  d_out = R_CMB/q.

For each n report

  nearest_integer,
  eta = n - round(n).

Rounding is diagnostic only and does not create a shell assignment.

## Held-out ell=4,5 test

Observed:

  r34_obs = |g4/g3|,
  r45_obs = |g5/g4|.

Interior predictions:

  r34_pred = (9/10)r23,
  r45_pred = (21/25)r23.

Exterior predictions:

  r34_pred = (5/6)r23,
  r45_pred = (2/3)r23.

Report signed and fractional residuals. Do not assign significance until map/mask covariance or simulations are attached.

## Output policy

The evaluator outputs machine-readable JSON containing:
- file SHA-256;
- harmonic extraction settings;
- fixed axis;
- g2..g5;
- r23, r34, r45;
- allowed branches;
- n and eta;
- comoving predicted distances;
- held-out residuals;
- explicit epistemic status.

No astronomical source name may be read or emitted by this pipeline.

## Current execution blocker

The current ChatGPT execution environment can inspect the Planck archive metadata but cannot access the 169 MB FITS payload through the available web/container route. Therefore no PR2/R2.02 numerical result is claimed in this session.

This is a data-access blocker, not a PASS or FAIL of the tidal model.
