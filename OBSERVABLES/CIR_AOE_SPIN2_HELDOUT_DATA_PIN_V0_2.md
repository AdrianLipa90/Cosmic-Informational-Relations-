# CIR AoE Spin-2 Held-Out Data Pin v0.2

Status: DATA PRODUCT PIN / BYTES NOT EVALUATED
Date: 2026-09-26

The official Planck PR3 all-sky CMB products provide a full-mission SMICA polarization map at Nside=2048. The official product page for

  COM_CMB_IQU-smica_2048_R3.00_full.fits

lists the fields

  I_STOKES,
  Q_STOKES,
  U_STOKES,
  TMASK,
  PMASK,
  I_STOKES_INP,
  Q_STOKES_INP,
  U_STOKES_INP,
  TMASKINP,
  PMASKINP.

The PR3 archive also documents separate common polarization masks.

For the prospective spin-2 low-l test, the primary extraction is now frozen to the official full-sky inpainted polarization fields

  Q_STOKES_INP,
  U_STOKES_INP,

with spin-2 harmonic extraction through ell=5 and E-mode used as the primary channel.

Reason: at these extremely low multipoles, a cut-sky Q/U transform requires an additional E/B leakage treatment. Using the official inpainted full-sky product makes the primary estimator deterministic without inventing a new mask-dependent transfer after inspection.

The ordinary Q_STOKES/U_STOKES plus official polarization mask remain a robustness path only. That robustness estimator must itself be frozen before it is run.

No PR3 polarization pixel values, E/B coefficients, or low-l polarization powers were inspected before this pin.

Official archive provenance:
- NASA/IPAC IRSA Planck PR3 CMB Maps page;
- product preview/download page for COM_CMB_IQU-smica_2048_R3.00_full.
