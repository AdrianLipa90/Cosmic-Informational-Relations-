# CIR Axisymmetric-Deformed Tetrahedral Translation Coefficient v0.1

Status: EXACT HARMONIC THEOREM / SOURCE PARAMETER BINDING OPEN
Date: 2026-09-26

## 1. Geometry

Let the canonical tetrahedral cubic be

  H_0(x,y,z)=x y z,

and let the selected tetrahedral vertex axis be

  s=(1,1,1)/sqrt(3).

Take an axisymmetric positive deformation around s with transverse eigenvalue one and longitudinal eigenvalue lambda>0:

  F_lambda
  = I + (lambda-1) s s^T.

An overall isotropic factor is omitted because it cancels from normalized harmonic morphology and from the derivative/parent norm ratio.

Define the pulled-back cubic

  P_lambda(x)=H_0(F_lambda^{-1}x),

and let

  H_lambda = Pi_3 P_lambda

be its degree-three harmonic projection.

For homogeneous cubics in R^3,

  Pi_3 P
  = P - (r^2/10) Delta P.

## 2. Exact parent norm

With the rotation-invariant L2 norm on S^2,

  ||H_lambda||^2
  =
  [20 lambda^6 + 9 lambda^4 + 12 lambda^2 + 4]
  / [4725 lambda^6]
  * 4 pi

up to the common convention that the displayed rational factor is the spherical average and 4pi restores the integral.

## 3. Exact translation descendant

Translate the observer along the same physical axis s.

The first descendant is

  D_s H_lambda := (s dot grad) H_lambda.

Its spherical norm is

  ||D_s H_lambda||^2
  =
  (3 lambda^2 + 2)^2
  / [375 lambda^6]
  * 4 pi.

Therefore the exact source-dependent scale coefficient is

  boxed[
  C(lambda)^2
  =
  ||D_s H_lambda||^2 / ||H_lambda||^2
  =
  63 (3 lambda^2+2)^2
  /
  {5[20 lambda^6+9 lambda^4+12 lambda^2+4]}
  ]

and

  boxed[
  C(lambda)
  =
  sqrt{
    63 (3 lambda^2+2)^2
    /
    [5(20 lambda^6+9 lambda^4+12 lambda^2+4)]
  }.
  ]

At lambda=1,

  C(1)=sqrt(7),

recovering the undeformed tetrahedral translation theorem exactly.

## 4. Scale estimator for a frozen source lambda

Let

  R_23 := A_2/A_3

be the observed total quadrupole-to-octupole amplitude ratio.

For a source-owned lambda fixed before CMB evaluation,

  boxed[
  q = |d|/R = R_23 / C(lambda)
  ].

In terms of full-sky powers,

  R_23 = sqrt[5 C_2/(7 C_3)],

so

  boxed[
  q(lambda)
  =
  sqrt[5 C_2/(7 C_3)] / C(lambda).
  ]

The dyadic candidate then predicts

  q(lambda)=2^{-n}.

This equation may be tested only after lambda is independently frozen.

## 5. Kerr source specialization

For the polar-axis Kerr ADM source reference,

  lambda_Kerr = r/sqrt(Delta),

  Delta = r^2 - 2Mr + a^2.

Therefore

  C_Kerr(M,a,r)
  := C(r/sqrt(Delta))

is fixed by the parent source geometry.

No free cross-l normalization remains once M,a,r are fixed.

## 6. Structural limits

As lambda -> 1,

  C -> sqrt(7).

As lambda -> infinity,

  C(lambda) -> 0.

As lambda -> 0+,

  C(lambda)^2 -> 63/5,

so

  C -> sqrt(63/5).

For the exterior Kerr polar branch r>r_+, one has lambda>=1 in the Schwarzschild-like radial stretching regime, hence

  0 < C(lambda) <= sqrt(7).

Thus the source deformation can reduce the undeformed translation coefficient but not increase it above sqrt(7) on that branch.

## 7. Epistemic firewall

EXACT:
- harmonic projection;
- C(lambda) formula;
- undeformed sqrt(7) limit;
- source-fixed q estimator conditional on the axisymmetric deformation model.

CANDIDATE:
- the physical parent supplies this axisymmetric deformation;
- the parent is Kerr-like;
- the CMB low-l anomaly is the translated tetrahedral response.

FORBIDDEN:
- solve lambda from the already-seen CMB amplitude ratio and count the same CMB data as validation;
- choose lambda to force an integer n;
- change the dyadic base or shell offset after evaluation.

The 2026 ELC C2/C3 amplitudes are already contaminated for any lambda model derived after their inspection and may be used only as post-hoc diagnostics.
