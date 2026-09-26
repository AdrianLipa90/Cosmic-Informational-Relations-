# CIR Tetrahedral Translation Scale Bridge v0.1

Status: EXACT SOLID-HARMONIC REPRESENTATION / CANDIDATE CMB PHYSICAL BINDING
Date: 2026-09-26

## 1. Canonical tetrahedral cell

Use the regular tetrahedral unit vectors

  v1=( 1, 1, 1)/sqrt(3),
  v2=( 1,-1,-1)/sqrt(3),
  v3=(-1, 1,-1)/sqrt(3),
  v4=(-1,-1, 1)/sqrt(3).

They satisfy

  sum_a v_a = 0,

and

  sum_a v_a v_a^T = (4/3) I_3.

Therefore the equal-weight tetrahedral source has no dipole and no trace-free quadrupole about its centre.

The first nontrivial tetrahedrally invariant harmonic is degree three. In this frame choose

  H3(x,y,z)=x y z.

It is harmonic:

  Delta H3 = 0,

and is invariant under the proper tetrahedral rotation group of this vertex set.

## 2. Vertex-axis displacement

Choose the vertex axis

  s=(1,1,1)/sqrt(3).

Let a local observation sphere of radius R be centred at a point displaced by d s from the tetrahedral centre. Write local position x=R n and define

  q := |d|/R.

The translated regular solid harmonic is

  H3(x+d s)
  = H3(x)
    + d D_s H3(x)
    + d^2/2 D_s^2 H3(x)
    + d^3/6 D_s^3 H3,

where D_s=s dot grad.

Because differentiation preserves harmonicity and lowers homogeneous degree, these four terms lie purely in l=3,2,1,0 respectively.

Explicitly,

  D_s H3
  = (xy+xz+yz)/sqrt(3).

If

  z_s := s dot x = (x+y+z)/sqrt(3),

then

  D_s H3
  = [3 z_s^2-r^2]/(2 sqrt(3)),

which is a pure zonal l=2 harmonic about the physical displacement axis s.

## 3. Exact norm ratio

Use the rotation-invariant L2 norm on the unit sphere.

The standard spherical moments give

  <x^2 y^2 z^2> = 1/105,

so

  ||H3||^2 = 4 pi/105.

Also

  ||D_s H3||^2 = 4 pi/15.

Hence

  ||D_s H3|| / ||H3|| = sqrt(7).

On a local sphere of radius R,

  A3 = |A| R^3 ||H3||,

  A2 = |A| |d| R^2 ||D_s H3||,

for one common ancestor amplitude A. Therefore the unknown source amplitude cancels:

  boxed[
  A2/A3 = sqrt(7) q
  ]

with

  q=|d|/R.

Thus

  boxed[
  q = A2/(sqrt(7) A3).
  ]

No independent cross-l boundary normalization C23 is needed in this candidate because l=2 and l=3 descend from one translated l=3 parent mode.

## 4. Power-spectrum form

For standard full-sky harmonic power

  C_l = [1/(2l+1)] sum_m |a_lm|^2,

define total multipole amplitude

  A_l = sqrt(sum_m |a_lm|^2)
      = sqrt[(2l+1) C_l].

Then

  A2/A3 = sqrt[5 C2/(7 C3)].

Therefore the tetrahedral translation candidate predicts the scale estimator

  boxed[
  q = (1/7) sqrt(5 C2/C3).
  ]

This estimator is rotationally invariant and does not use the AoE axis direction.

## 5. Dyadic shell selector

If the separately established candidate log-scale spectrum is imposed,

  q = 2^{-n},

then

  boxed[
  n_cont
  = -log2 q
  = log2[7 sqrt(C3/(5 C2))].
  ]

This is now an actual upstream selector of n from CMB low-l powers under the declared tetrahedral-translation physical model.

No black-hole mass, radius or catalogue coordinate enters n_cont.

## 6. Frozen CMB-screen distance prediction

Using the already frozen CMB last-scattering screen radius

  R_CMB = 13,873 Mpc

for this branch,

  d_pred = q R_CMB.

If the dyadic condition holds at integer n,

  d_n = R_CMB 2^{-n}.

The direction is not yet fixed by the power ratio.

## 7. Angular morphology

The parent l=3 tetrahedral harmonic carries full tetrahedral A4 symmetry.

Displacement along one vertex reduces the proper rotational stabilizer to C3. Including a reflection of the transverse plane produces the associated D3 angular grammar.

The induced l=2 mode is zonal about s. For a pure |2,0> state its maximum-angular-momentum-dispersion directions form the great circle perpendicular to s.

Therefore the standard AoE maximum-dispersion axis is NOT predicted to point at the tetrahedral centre. In the idealized translated-tetrahedral limit it is perpendicular to the physical displacement axis.

The full l=3 morphology, not the AoE axis alone, is required to recover the tetrahedral frame and select one of the vertex directions.

## 8. Additional exact translation descendants

For completeness,

  D_s^2 H3 = (2/3)(x+y+z),

  D_s^3 H3 = 2/sqrt(3).

The translated parent therefore also emits intrinsic l=1 and l=0 descendants with fixed q powers. Standard CMB monopole removal and kinematic-dipole subtraction mean these are not used as primary validators without a dedicated intrinsic-dipole separation theorem.

## 9. Falsification structure

Before evaluating a new held-out low-l amplitude dataset, freeze:

- tetrahedral parent H3 orbit;
- displacement along a tetrahedral vertex axis;
- q estimator q=(1/7)sqrt(5 C2/C3);
- dyadic base 2 and zero offset;
- R_CMB anchor;
- no target-catalog use.

The physical candidate fails if:
- a tetrahedral l=3 morphology is rejected by a preregistered full-a_lm test;
- the l=2 mode is incompatible with the translated derivative morphology;
- q is not in (0,1);
- or a declared held-out dataset gives a dyadic residual outside the frozen threshold.

## 10. Epistemic boundary

EXACT:
- regular tetrahedron first and second moments;
- H3=xyz harmonic and tetrahedral invariance;
- translation by exp(d D_s);
- pure-degree descent l=3 -> l=2 -> l=1 -> l=0;
- norm ratio sqrt(7);
- q estimator conditional on one translated l=3 parent mode.

CANDIDATE:
- the CMB low-l anomaly is this translated tetrahedral solid-harmonic mode;
- the physical displacement obeys the dyadic shell law;
- the CMB-screen radius is the correct dimensional anchor for the shadow interpretation.

NOT CLAIMED:
- black-hole origin established;
- AoE alone locates a centre;
- TIR A4 cell is physically identified with the CMB source without the remaining source/metric bridge.
