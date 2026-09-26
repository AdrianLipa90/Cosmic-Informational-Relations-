# CIR Tetrahedral AoE-Axis Uniqueness No-Go v0.1

Status: EXACT REPRESENTATION NO-GO / SCALE BRIDGE UNAFFECTED
Date: 2026-09-26

## 1. Parent octupole

Take the normalized tetrahedral degree-three harmonic in any orientation,

  T_3 = R · (x y z),

with R in SO(3).

Let L_i be the angular-momentum generators on the l=3 harmonic carrier and define the symmetric second-moment tensor

  Q_ij
  := (1/2) <T_3|L_i L_j + L_j L_i|T_3>
     / <T_3|T_3>.

The tetrahedral state is invariant under the proper tetrahedral group A4. Therefore Q is an A4-invariant real symmetric rank-two tensor.

The defining three-dimensional A4 representation is irreducible, so Schur/isotropy implies

  Q_ij = lambda delta_ij.

Taking the trace,

  Tr Q
  = <L^2>
  = l(l+1)
  = 12.

Hence

  boxed[Q_ij = 4 delta_ij].

Therefore for every unit direction n,

  M_3(n)
  := <(n·L)^2>
  = n_i Q_ij n_j
  = 4.

The ideal tetrahedral l=3 mode has isotropic angular-momentum dispersion. It has no unique maximum-dispersion axis.

## 2. Translation-induced quadrupole

For displacement along a tetrahedral vertex axis s, the first translation descendant is

  T_2 ∝ D_s(xyz),

which is a pure l=2,m=0 state in the frame with z||s.

For a candidate direction n making angle beta with s,

  M_2(n)
  = [l(l+1)/2] sin^2 beta
  = 3 sin^2 beta.

Thus M_2 is maximal for every direction in the great circle

  n·s = 0.

It does not select one point on that circle.

## 3. Joint l=2,3 AoE functional

For the commonly used normalized joint angular-momentum-dispersion functional,

  J(n)
  = M_2(n)/[2·3] + M_3(n)/[3·4],

the ideal translated tetrahedral model gives

  J(beta)
  = (1/2) sin^2 beta + 1/3.

Therefore

  J_max = 5/6

for every n perpendicular to s.

Hence:

  boxed[
  ideal translated tetrahedral parent
  => a maximum-dispersion GREAT CIRCLE,
  not a unique AoE axis.
  ]

## 4. Consequence

The exact tetrahedral translation scale estimator

  q = (1/7) sqrt(5 C2/C3)

is not affected by this no-go because it uses rotation-invariant total multipole powers.

But an observed unique/quasi-unique AoE direction requires an additional symmetry-breaking structure beyond the ideal tetrahedral parent plus pure vertex translation.

Admissible examples, only after derivation, include:
- a Moire/holonomy phase that selects one tangent direction on the great circle;
- a non-isotropic deformation of the tetrahedral cell;
- a source/metric tensor coupling that breaks the residual axial degeneracy;
- a frame-dragging/chiral operator.

No such term may be selected from the observed AoE direction after the fact.

## 5. Predictive geometry if a tangent selector exists

If a separate upstream operator selects a unique maximum-dispersion direction a within the plane perpendicular to s, then

  a·s = 0.

Thus the physical displacement/centre direction s lies on the great circle perpendicular to the observed AoE axis a.

A second independent tangent/phase observable is required to select s on that circle.

## 6. Epistemic boundary

EXACT:
- Q_ij=4 delta_ij for the tetrahedral l=3 state;
- M_3(n)=4 for all n;
- M_2(beta)=3 sin^2 beta for the translated l=2 descendant;
- joint preferred set n·s=0.

UNAFFECTED:
- the continuous q scale estimator from C2/C3.

OPEN:
- the physical source binding;
- the symmetry-breaking tangent selector;
- the unique three-dimensional centre direction.
