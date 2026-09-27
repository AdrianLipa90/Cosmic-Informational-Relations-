# CIR C3-Face Translation Quadrupole-Axis Corollary v0.1

Status: EXACT COROLLARY / PROSPECTIVE PR4 FALSIFIER
Date: 2026-09-27

## Parent

CIR_C3_SELECTED_TETRAHEDRAL_FACE_OCTUPOLE_THEOREM_CANDIDATE_V0_1

## 1. Octupole axis

For the selected-face tetrahedral octupole, the angular-momentum second-moment
tensor has one largest eigenvalue

  lambda_parallel = 320/41

along the selected/missing vertex axis s, and two smaller eigenvalues

  lambda_perp = 86/41.

Therefore its unique MAMD/Power-tensor principal axis is

  n3 = +/- s.

## 2. Translation descendant

The parent model generates the quadrupole by translation along the same vertex axis:

  H2 proportional to D_s H3_face.

H3_face is invariant under the C3 stabilizer of s. Directional differentiation
along s commutes with that C3 action, so H2 is C3 invariant about s.

For l=2 the only C3-invariant weight is m=0. Therefore, in the frame z||s,

  H2 proportional to |2,0>.

For |2,0>,

  <L_s^2> = 0,

and rotational symmetry in the transverse plane gives

  <L_x^2> = <L_y^2> = l(l+1)/2 = 3.

Thus the l=2 MAMD maximum eigenspace is exactly the plane perpendicular to s.

Every allowed quadrupole principal axis n2 therefore satisfies

  n2 dot s = 0.

Since n3=+/-s,

  boxed[
  |n2 dot n3| = 0
  ]

and hence the unoriented quadrupole-octupole principal-axis angle is

  boxed[
  theta23 = 90 degrees.
  ]

This prediction contains no fitted parameter.

## 3. Consequence

A measured near-alignment of quadrupole and octupole MAMD/Power-tensor principal
axes is incompatible with the pure-translation C3-face model.

The model cannot be repaired by:
- choosing another member of the transverse l=2 maximum circle;
- reversing a headless axis sign;
- altering the radial q value.

Any repair needs a NEW symmetry-breaking/deformation/dynamical operator and a new
prospective freeze.

The prior GL(3) identifiability firewall remains in force: such a deformation may
not be fitted from the same CMB multipoles and then counted as validation.
