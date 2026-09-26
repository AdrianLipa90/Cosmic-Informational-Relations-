# CIR Kerr Polar-Shadow Dyadic Forward Family v0.1

Status: TWO-PARAMETER SOURCE FAMILY / SPIN SELECTOR OPEN / NO NEW DATA EVALUATED
Date: 2026-09-26

## 1. Inputs fixed upstream

Use the polar Kerr photon-region gate.

For dimensionless spin

  chi=a/M,  0<=chi<1,

let x_ph(chi) be the unique exterior root of

  x^3-3x^2+chi^2(x+1)=0.

Then

  lambda_ph^2
  = x_ph(x_ph+1)/[2(x_ph-1)],

and

  C_ph(chi)=C(lambda_ph(chi)).

Use the previously declared Kerr horizon twist candidate

  delta_n(chi)
  = chi/[12 sqrt(1-chi^2)].

No CMB datum enters these source functions.

## 2. Dyadic/fractal source law

Let

  n in Z_{>=1}

be the discrete topological shell index.

The source-family contraction is

  boxed[
  q_src(n,chi)
  = 2^{-n-delta_n(chi)}.
  ]

The predicted quadrupole/octupole total-amplitude ratio is

  boxed[
  R_23_pred(n,chi)
  := (A_2/A_3)_pred
  = C_ph(chi) q_src(n,chi).
  ]

For standard full-sky powers,

  A_l=sqrt[(2l+1) C_l],

so the equivalent power prediction is

  boxed[
  (C_2/C_3)_pred
  = (7/5) R_23_pred^2.
  ]

For D_l=l(l+1)C_l/(2pi),

  boxed[
  (D_2/D_3)_pred
  = (7/10) R_23_pred^2.
  ]

## 3. Parameter count

The mass M cancels from every dimensionless prediction above.

The complete polar-shadow scale family has only

  (n,chi),

with
- n discrete;
- chi continuous but REQUIRED to be source-owned.

There is no free radius, no free GL(3) shear, no cross-l normalization and no phase offset.

## 4. Limiting envelopes

At chi=0,

  x_ph=3,
  lambda_ph=sqrt(3),
  delta_n=0,
  C_ph=1.518718306667686... .

Therefore each n branch begins at

  R_23_pred(n,0)
  = 1.518718306667686... * 2^{-n}.

As chi->1^-,

  delta_n->+infinity,

so

  R_23_pred(n,chi)->0

despite the finite C_ph extremal limit.

Hence every fixed-n branch spans a bounded interval ending at zero. A future observed ratio larger than the chi=0 endpoint of a branch excludes that branch without fitting chi.

## 5. Direction/morphology sector

The radial/power law above does not by itself identify the observed AoE maximum-dispersion axis.

At leading order in Kerr spin, chirality enters the ADM shift beta^phi rather than the spatial triad.

A complete direction prediction therefore requires the separate shift/holonomy forward map

  beta^phi
  -> boundary phase/tangent selector
  -> full rotated a_lm morphology.

That bridge remains OPEN and may not be replaced by fitting a GL(3) deformation to the octupole.

## 6. Prediction discipline

This family is frozen before opening any new low-l amplitude dataset.

Previously inspected Planck-2013 and ELC-2026 amplitudes are contaminated and may be used only as post-hoc diagnostics.

A prospective point prediction requires an independent spin packet

  chi=chi_star +/- sigma_chi

or a theorem selecting chi.

Only then is

  R_23_pred(n,chi_star)

eligible for a held-out CMB test.

No source spin may be inferred from the held-out CMB statistic and reused as validation.
