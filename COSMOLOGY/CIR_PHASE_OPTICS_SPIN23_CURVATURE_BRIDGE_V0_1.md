# CIR Phase-Optics Spin-2 / Spin-3 Curvature Bridge v0.1

Status: EXACT DIFFERENTIAL-OPERATOR BRIDGE / CMB CARRIER BINDING OPEN
Date: 2026-09-26

## 1. Parent phase potential

The existing QHTRI/Phase-Optics layer already admits a typed scalar phase screen

  Phi(x,y)

after a source-owned potential and phase coupling have been declared.

It also already uses the Hessian of Phi as the thin-screen focusing/shear object.

Define the complex transverse derivative

  D := partial_x + i partial_y,

and its conjugate

  Dbar := partial_x - i partial_y.

## 2. Spin-2 channel

Define the complex shear-like curvature

  boxed[
  gamma
  := (1/2) D^2 Phi
  = (1/2)(Phi_xx-Phi_yy)
    + i Phi_xy.
  ]

This is exactly the traceless Hessian packaged as a complex field.

Under a rotation of the transverse frame through angle theta,

  D -> exp(i theta) D,

so

  gamma -> exp(2 i theta) gamma.

Thus gamma is a spin-2 field.

This reproduces the standard weak-lensing shear representation already cross-checked by the Phase-Optics lens tensor.

## 3. Third-derivative decomposition

The symmetric third derivative of one scalar in two dimensions contains two irreducible spin sectors.

Define

  F1
  := Dbar gamma
  = (1/2)[Phi_xxx+Phi_xyy]
    + (i/2)[Phi_xxy+Phi_yyy],

and

  G3
  := D gamma
  = (1/2)[Phi_xxx-3 Phi_xyy]
    + (i/2)[3 Phi_xxy-Phi_yyy].

Then

  F1 -> exp(i theta) F1,

  G3 -> exp(3 i theta) G3.

Therefore:

  F1 = spin-1 first-flexion channel,
  G3 = spin-3 second-flexion / three-flexion channel.

This is the standard weak-lensing flexion decomposition of third derivatives of a scalar lensing potential.

## 4. Exact relation to threefold angular grammar

The real and imaginary numerators of G3 are the cubic harmonic combinations

  x^3-3xy^2,

  3x^2y-y^3,

which form the real planar m=+/-3 basis.

Hence the spin-3 phase-curvature channel has exactly the same SO(2) weight as the planar octupole edge pair isolated in the CIR U(1)/D3 low-l analysis.

Under a C3 rotation theta=2pi/3,

  G3 -> exp(i 2pi) G3 = G3.

Thus spin-3 flexion lies in the C3-trivial rotational sector and splits into reflection-even/odd real components under D3.

This is an exact representation crosswalk.

## 5. Scale covariance

For a self-similar source phase

  Phi_L(x,y)=A f(x/L,y/L),

one has

  gamma_L ~ A L^{-2},

  G3_L ~ A L^{-3}.

Therefore

  boxed[
  |G3|/|gamma| ~ 1/L
  ]

wherever gamma is nonzero.

If the dimensionless source shape f and evaluation point are fixed upstream, define its coefficient

  c_f
  := L |G3|/|gamma|.

Then

  boxed[
  L = c_f |gamma|/|G3|.
  ]

This is a legitimate scale estimator only when c_f is derived from the source model before observing the target field.

## 6. Kerr/tetrahedral relevance

A source-owned Kerr axis may select one tetrahedral vertex, giving a C3 oriented frame.

The Phase-Optics hierarchy then supplies two natural angular channels in that same frame:

  Hessian(Phi) -> spin 2,

  third derivative(Phi) -> spin 3.

This provides a coefficient-free statement about ANGULAR WEIGHT.

It does not yet fix their relative amplitudes, because those require the physical source phase Phi and its scale.

## 7. Relation to existing PhaseNav/QHTRI code

Existing Phase Optics already implements:

  Hess(Phi)
  -> convergence/shear/focal tensor/lens Jacobian.

The present bridge is the next derivative order:

  third(Phi)
  -> F1, G3.

No generic T36 reshape is required.

## 8. Epistemic boundary

EXACT:
- differential formulas above;
- spin weights 1,2,3;
- C3 invariance of spin-3;
- self-similar derivative scaling.

STANDARD EXTERNAL IDENTIFICATION:
- gamma as weak-lensing shear;
- F1/G3 as first/second gravitational flexion.

OPEN:
- physical Kerr/tetrahedral source -> Phi;
- CMB temperature/polarization response to this project phase field;
- absolute phase coupling normalization.

FIREWALL:
- do not infer Phi from CMB and then call its derivatives a source prediction;
- do not identify spin weight with spherical multipole l without a declared sky-response operator.
