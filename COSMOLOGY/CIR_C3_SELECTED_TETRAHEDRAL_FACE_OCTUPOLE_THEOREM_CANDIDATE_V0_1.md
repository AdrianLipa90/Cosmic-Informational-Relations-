# CIR C3-Selected Tetrahedral-Face Octupole Theorem Candidate v0.1

Status: EXACT REPRESENTATION GEOMETRY / PHYSICAL CMB BINDING CANDIDATE
Date: 2026-09-27

## 1. Canonical tetrahedron and one selected vertex

Use the regular tetrahedral unit vectors

  s =( 1, 1, 1)/sqrt(3),
  u1=( 1,-1,-1)/sqrt(3),
  u2=(-1, 1,-1)/sqrt(3),
  u3=(-1,-1, 1)/sqrt(3).

Then

  u_i dot u_j = -1/3,  i!=j,

and

  u1+u2+u3 = -s.

Selecting the vertex s reduces the proper tetrahedral A4 symmetry to the C3 stabilizer of that vertex.

This selection is representation-theoretically natural in a framework that already contains a distinguished C3 sector; no GL(3) deformation is required.

## 2. Octupole from the opposite face

Take the Maxwell multipole-vector triple

  {u1,u2,u3}.

Let P3 be the traceless/harmonic projection of

  (u1 dot x)(u2 dot x)(u3 dot x).

The resulting real harmonic cubic H3^face is C3 invariant about s.

Its multipole-vector Gram matrix is exactly

  G_face =
    [ 1   -1/3 -1/3
     -1/3  1   -1/3
     -1/3 -1/3  1 ].

The sign of each multipole vector is projective; the sign-invariant prediction is

  boxed[
  |u_i dot u_j| = 1/3
  ]

for all three pairs.

## 3. Missing-vertex reconstruction

If three unoriented multipole vectors can be oriented so that all pairwise products are negative, define

  s_rec
  := -(u1+u2+u3)/|u1+u2+u3|.

For the exact tetrahedral-face configuration,

  boxed[s_rec = s].

Thus the physical C3 axis can be reconstructed from the octupole vectors without using the quadrupole.

## 4. Maximum-angular-momentum-dispersion axis

For H3^face define

  Q_ij
  := < {L_i,L_j}/2 >/ <1>.

In the canonical Cartesian frame one obtains

  Q =
    [ 4      78/41  78/41
      78/41  4      78/41
      78/41  78/41  4 ].

Its eigenvalues are

  lambda_parallel = 320/41

along

  s proportional to (1,1,1),

and the doubly degenerate transverse eigenvalue

  lambda_perp = 86/41.

Since

  320/41 > 86/41,

the unique maximum-angular-momentum-dispersion axis is

  boxed[n_3 = +/- s].

Therefore, unlike the fully A4-symmetric tetrahedral harmonic xyz, the C3-selected opposite-face octupole has a unique AoE-type axis.

## 5. Translation descendant and scale coefficient

Let the observer be displaced from the tetrahedral centre by d s and evaluate on a local sphere of radius R.

With

  q:=|d|/R,

the translated solid harmonic is

  H3^face(x+d s)
  = H3^face(x)
    + d D_s H3^face(x)
    + ...

The first derivative is a pure l=2 harmonic because differentiation preserves harmonicity and lowers homogeneous degree by one.

The exact sphere-norm ratio is

  ||D_s H3^face||^2 / ||H3^face||^2
  = 343/205.

Hence

  A2/A3
  = sqrt(343/205) q,

so

  boxed[
  q = sqrt(205/343) A2/A3
  ].

Using

  A_l=sqrt[(2l+1)C_l],

this becomes

  boxed[
  q = (5 sqrt(41)/49) sqrt(C2/C3)
  ].

Using

  D_l=l(l+1)C_l/(2pi),

  boxed[
  q = (5 sqrt(82)/49) sqrt(D2/D3)
  ].

This coefficient is derived from the selected tetrahedral-face parent and may not be replaced by the earlier ideal-A4 sqrt(7) coefficient.

## 6. C6/ARPL comparison

A separate candidate branch has already frozen

  q_C6 = 1/6

under REGULAR_C6_CHILD_BINDING.

If both the C3-selected tetrahedral-face translation model and that C6/ARPL radial bridge are physically admitted, then before data inspection they jointly predict

  D2/D3
  = [ (49/(5 sqrt(82))) * (1/6) ]^2
  = 2401/(25*82*36).

Equivalently,

  boxed[
  D2/D3 = 2401/73800
  ].

This joint prediction is conditional on two independent physical bridges and is not promoted by algebra alone.

## 7. Morphology firewall

The model predicts simultaneously:

1. octupole multipole-vector absolute dot products = 1/3;
2. the reconstructed missing vertex equals the octupole MAMD axis;
3. the l=2 translation descendant shares the same physical C3 axis;
4. the cross-l power ratio follows the derived coefficient above.

The model is not allowed to fit an unrestricted GL(3) deformation after seeing the octupole.

Any nonzero deformation requires a new prospective version with an independently sourced F.

## 8. Provenance boundary

EXACT:
- tetrahedral face Gram geometry;
- missing-vertex reconstruction;
- unique MAMD eigenaxis and eigenvalues;
- translation derivative and sphere-norm coefficient 343/205.

CANDIDATE:
- CMB octupole is the selected-face tetrahedral state;
- C3 internal selector binds to the physical sky vertex stabilizer;
- observer displacement generates the CMB quadrupole;
- C6/ARPL q=1/6 and the C3-face translation q are the same physical scale coordinate.

CONTAMINATED FOR VALIDATION:
- WMAP1/3 multipole-vector values already inspected before this theorem;
- Planck-2013 SMICA multipole-vector values already inspected before this theorem;
- ELC2026 C2/C3 values already inspected.

Prospective validation must use a newly unopened map/release or observable.
