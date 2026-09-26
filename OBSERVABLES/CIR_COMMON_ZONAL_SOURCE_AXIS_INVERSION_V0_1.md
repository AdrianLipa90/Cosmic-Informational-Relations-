# CIR Common Zonal Source-Axis Inversion v0.1

Status: FROZEN INVERSE ESTIMATOR BEFORE PRIMARY PR2 MAP EXECUTION
Date: 2026-09-26

## Inputs

Use the same low-l coefficients ell=2,3 from the primary frozen Planck PR2/R2.02 SMICA temperature product.

No astronomical target catalog enters this estimator.

## Objective

For trial sky direction s calculate

  Z_ell(s)
  = |a_{ell0}^{(s)}|^2 / P_ell,

where

  P_ell = sum_m |a_{ell m}|^2.

Set

  Z_23(s)=Z_2(s)+Z_3(s).

Return the unoriented direction

  s_hat = argmax Z_23(s).

## Deterministic search contract

1. Coarse HEALPix grid NSIDE=32 over the whole sphere.
2. Treat antipodes as one unoriented axis.
3. Keep the best coarse direction.
4. Refine only inside a 5 degree cap around that direction at NSIDE=512.
5. If two disconnected maxima differ in Z_23 by less than 1e-8 relative, report the degeneracy instead of selecting one silently.
6. Do not constrain s_hat to be orthogonal to the frozen AoE axis during optimization.

The AoE/zonal orthogonality is a result variable, not a fitted constraint.

## Report

- s_hat Galactic (l,b);
- Z_2, Z_3, Z_23;
- undirected angular separation alpha between s_hat and frozen AoE axis;
- orthogonality residual delta_perp = |90 deg - alpha|;
- g_2=T_2(s_hat), g_3=T_3(s_hat);
- r23=|g3/g2|;
- radial-tidal branch outputs under the already frozen tidal model.

## No-retune

After PR2 coefficients are opened:
- objective weights remain 1:1 for ell=2,3;
- grid/refinement rule remains fixed;
- no AoE orthogonality penalty may be added;
- no target source position may guide the choice between near-degenerate maxima.

## Evidential role

This is an inverse estimator, not an independent prediction. Its output becomes a frozen sky-direction prediction for later comparison with held-out astrophysical structure/source data.

The subsequent source-catalog match must preserve the inferred s_hat and its uncertainty.
