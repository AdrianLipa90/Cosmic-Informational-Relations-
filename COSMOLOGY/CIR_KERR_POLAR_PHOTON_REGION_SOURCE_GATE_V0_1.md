# CIR Kerr Polar Photon-Region Source Gate v0.1

Status: STANDARD-KERR PHOTON-REGION REDUCTION / CIR SHADOW BINDING CANDIDATE
Date: 2026-09-26

## 1. Why the photon region is the correct shadow radius gate

For Kerr, the shadow boundary is not set directly by the event-horizon areal radius. It is the lensed image of unstable spherical null geodesics in the photon region.

For a spherical null orbit of Boyer-Lindquist radius r, standard Kerr impact parameters are

  xi(r)
  = -[r^3-3 M r^2+a^2(M+r)]/[a(r-M)],

  eta(r)
  = r^3[4 a^2 M-r(r-3M)^2]/[a^2(r-M)^2].

They follow from the radial criticality equations

  R(r)=0,
  dR/dr=0.

## 2. Polar/axis observer reduction

For an observer on the spin axis, regularity of the axis requires the critical orbit contributing to the circular axial shadow to have

  L_z=0,

hence

  xi=0.

Define

  chi=a/M,
  x=r_ph/M.

Then xi=0 gives exactly

  boxed[
  x^3-3x^2+chi^2(x+1)=0.
  ]

Equivalently,

  boxed[
  chi^2 = x^2(3-x)/(x+1).
  ]

The exterior polar photon orbit lies on the branch

  1+sqrt(2) <= x <= 3,

with

  x(chi=0)=3,

  x(|chi|->1)=1+sqrt(2).

On this branch x decreases monotonically with chi^2 because

  dx/d(chi^2)
  = -(x+1)^2/[2x(x^2-3)] < 0.

Thus the polar photon-region evaluation radius is fixed by spin and is not an additional free source parameter.

## 3. Kerr spatial anisotropy evaluated at the photon region

The previously derived polar Kerr source deformation uses

  lambda_Kerr = r/sqrt(Delta),

  Delta=r^2-2Mr+a^2.

At r=r_ph this becomes

  lambda_ph(chi)
  = x/sqrt(x^2-2x+chi^2).

Using the photon-orbit equation to eliminate chi,

  x^2-2x+chi^2
  = 2x(x-1)/(x+1),

hence

  boxed[
  lambda_ph^2
  = x(x+1)/[2(x-1)].
  ]

Endpoint values are

  lambda_ph(0)=sqrt(3),

and

  lambda_ph(|chi|->1)
  = sqrt[(2+sqrt(2))/2]
  ~= 1.70710678.

Therefore the shadow-relevant polar source deformation is confined to a narrow, source-derived interval; it is not an arbitrary GL(3) strain.

## 4. Tetrahedral translation coefficient on the photon region

Use the exact axisymmetric-deformed tetrahedral coefficient

  C(lambda)^2
  =
  63(3lambda^2+2)^2
  /
  [5(20lambda^6+9lambda^4+12lambda^2+4)].

Define

  C_ph(chi):=C(lambda_ph(chi)).

Then

  C_ph(0)
  = C(sqrt(3))
  ~= 1.518718306667686,

while in the extremal limit

  C_ph(1^-)
  ~= 1.543447... .

Thus Kerr photon-region geometry fixes the cross-l translation coefficient to a narrow spin-dependent band.

## 5. Source packet

A polar Kerr-shadow source packet now requires only

  (M, chi)

for dimensional geometry.

For all dimensionless low-l morphology/scale ratios, M cancels. The source-owned ingredients are

  x_ph(chi),
  lambda_ph(chi),
  C_ph(chi),
  Omega_H/kappa_H
  = chi/sqrt(1-chi^2).

This reduces the previous free radius r/M to a function of spin.

## 6. Firewall

EXACT/STANDARD:
- Kerr spherical-photon impact parameters;
- xi=0 polar branch;
- cubic photon-radius relation;
- lambda_ph reduction.

CIR EXACT CONDITIONAL:
- insertion of lambda_ph into the already proved tetrahedral coefficient C(lambda).

CANDIDATE PHYSICAL BINDING:
- the cosmological AoE shadow is described by the polar Kerr-shadow source class;
- the CMB-screen/tetrahedral transfer reads this local photon-region deformation.

FORBIDDEN:
- choose r/M from the CMB after this gate;
- use horizon radius in place of photon-region radius merely because it improves a fit;
- choose another photon orbit branch after looking at the low-l amplitudes.

References:
- Standard Kerr photon-region construction and xi(r), eta(r): rotating-black-hole shadow literature.
