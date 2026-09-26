# CIR D3 Symmetry-Only Scale No-Go v0.1

Status: EXACT REPRESENTATION NO-GO / DYNAMICAL TRANSFER REQUIRED
Date: 2026-09-26

## Claim

D3 symmetry alone cannot determine the radial/fractal scale parameter q or the dyadic shell index n from the relative amplitudes of the CMB quadrupole and octupole.

## Proof

Let H_l be the (2l+1)-dimensional spherical-harmonic carrier at fixed l.

Restrict the SO(3) representation to D3:

  H_l |_{D3}
  = direct_sum_rho N_{l,rho} V_rho.

Let P_{l,rho} be the D3 projector onto an allowed irrep rho.

A D3-compatible sky field has independent components

  T_l = sum_rho c_{l,rho} v_{l,rho},

where

  v_{l,rho} in image(P_{l,rho}).

The symmetry fixes:
- which representation sectors exist;
- how m-components transform within each sector;
- reflection/rotation selection rules.

But for different l, the scalar coefficients c_{l,rho} belong to different irreducible SO(3) carriers H_l. D3 contains no generator mapping H_2 to H_3 and supplies no equation fixing

  c_{3,rho3}/c_{2,rho2}.

Therefore the cross-multipole amplitude ratio

  rho_23^planar = A_3^planar/A_2^planar

remains dynamically free under symmetry alone.

QED.

## Consequence

A scale estimator requires an additional transfer law

  A_l^planar
  = A0 K_l(q) C_l,

where:
- K_l(q) is derived from propagation/dynamics/radial geometry;
- C_l is a fixed angular representation coefficient;
- q is the physical dimensionless scale coordinate.

Only after K_l and C_l are fixed upstream may rho_23 determine q.

## Relation to the dyadic scale algebra

The exact TIR/ARPL log-scale law

  q_n = 2^{-n}

may be imposed as a candidate discrete spectrum only after a physical transfer map K_l(q) exists.

Neither

  W(A2) ~= D3

nor the existence of an AoE preferred axis supplies n by itself.

In particular, identifying the Coxeter number h=3 with the shell index n=3 without an independently derived transfer theorem is forbidden.

## Next required theorem

Derive K_l(q) from one of:

1. a source-bound Green/Poisson propagation problem with a non-zonal D3 boundary condition;
2. a tensor/spin-weighted tidal response with a declared scalar observation map;
3. a Kerr/frame-dragging projection operator;
4. another TIR-derived propagation law that produces the corrected high-|m| observables.

The chosen transfer law must be frozen before using cross-l amplitudes to infer q.
