# CIR AoE Interior Tidal Green-Shadow Model v0.3

Status: CANDIDATE FORWARD MODEL / FROZEN BEFORE ANY NEW INDEPENDENT LOW-L DATA
Date: 2026-09-26

This v0.3 does not erase the recorded FAIL of the scalar point-Green model. It is a new physical candidate motivated by the fact that a gravitational shadow/imprint is naturally controlled by derivatives of a potential, not by the potential kernel alone.

All Planck-2013 coefficients already inspected in the v0.2 scalar diagnostic are EXPLORATORY/CONTAMINATED for v0.3 and may not count as prospective validation.

## 1. Geometry

Let

  G(x;y) = 1/|x-y|,

with observation point

  x = R n

on a sphere of radius R and a candidate relational centre/source

  y = d a,

where a is the frozen unoriented AoE axis and

  0 < d < R.

Define

  q := d/R,
  0 < q < 1.

The branch d<R is not selected from target data. It is the declared "observer displaced from an interior centre inside the CMB screen" hypothesis being tested.

The exact scalar Green expansion is

  G = (1/R) sum_{ell=0}^infinity q^ell P_ell(mu),

where

  mu = a dot n.

## 2. Tidal operator

Define the axis-contracted trace-free Hessian

  T_a[G]
  := (a_i a_j - delta_ij/3) partial_i partial_j G.

Away from the source,

  Delta G = 0,

so

  T_a[G] = (a dot grad_x)^2 G.

Because y=d a and translational invariance gives

  partial_d G = - a dot grad_x G,

the square removes the sign and therefore

  T_a[G] = partial_d^2 G.

This is a scalar component of the Newtonian/electric-Weyl tidal Hessian along the declared axis.

## 3. Exact multipole coefficients

Differentiate the interior Green series twice with respect to d:

  T_a[G]
  = (1/R^3) sum_{ell=2}^infinity ell(ell-1) q^{ell-2} P_ell(mu).

Thus the tidal Legendre coefficients are

  t_ell = A/R^3 * ell(ell-1) q^{ell-2},

for one overall amplitude A.

The operator annihilates ell=0 and ell=1 exactly. Therefore the first nonzero modes are the quadrupole and octupole, matching the multipole sector in which the Axis of Evil is defined.

## 4. Primary q estimator

For ell=2 and ell=3,

  t_2 = 2 A/R^3,
  t_3 = 6 A q/R^3.

Hence

  |t_3/t_2| = 3 q,

and the no-refit estimator is

  q_23 = (1/3) |t_3/t_2|.

Using the fixed-axis scalar CMB Legendre projections

  g_ell = sqrt[(2ell+1)/(4pi)] a_{ell0}^{(a)},

the candidate physical identification is

  t_ell proportional to g_ell

within the low-l shadow component. Therefore

  q_23
  = (1/3) |g_3/g_2|
  = (sqrt(7/5)/3) |a_{30}^{(a)}/a_{20}^{(a)}|.

Model-domain condition:

  0 < q_23 < 1.

## 5. Dyadic shell hypothesis

The existing local log-scale representation supplies the separate candidate law

  q = 2^{-n},
  n in Z_{>=1}.

Therefore

  |g_3/g_2| = 3 * 2^{-n},

and

  n_cont = log2(3/|g_3/g_2|).

The shell condition is tested only after q_23 has been estimated. Base 2 and zero shell offset remain frozen.

## 6. Held-out higher-multipole predictions

For general ell>=2,

  |t_{ell+1}/t_ell|
  = [(ell+1)/(ell-1)] q.

After inferring q only from ell=2,3, the first held-out predictions are

  |g_4/g_3| = 2 q,
  |g_5/g_4| = (5/3) q.

Equivalently, eliminating q using r_23:=|g_3/g_2|,

  r_34(pred) = (2/3) r_23,
  r_45(pred) = (5/9) r_23.

Under exact n=1 dyadic closure:

  r_23 = 3/2,
  r_34 = 1,
  r_45 = 5/6.

No ell>=4 data may be used to alter the q estimator.

## 7. CMB-screen radial prediction

For the already frozen CMB screen anchor R_CMB,

  d = q R_CMB.

Under the dyadic sub-hypothesis,

  d_n = R_CMB 2^{-n}.

This d is a candidate comoving displacement of the relational centre from the observer inside the declared CMB-screen geometry. It is not a black-hole Schwarzschild radius and is not selected from a black-hole catalogue.

## 8. Falsification

The v0.3 interior tidal model fails if any preregistered independent map pipeline yields, beyond propagated uncertainty:

- g_2 consistent with zero so q is unidentified;
- q_23 <= 0 or q_23 >= 1;
- severe instability of q_23 across the frozen component-separation/mask robustness set;
- held-out r_34 or r_45 inconsistent with the frozen equations above.

The dyadic sub-hypothesis additionally fails if n_cont is inconsistent with every positive integer under the declared uncertainty rule.

## 9. Provenance boundary

PRESERVED FAIL:
- v0.2 scalar point-Green kernel.

EXACT CONDITIONAL MATHEMATICS:
- harmonic Green expansion for d<R;
- trace-free Hessian identity away from source;
- ell(ell-1) coefficient law;
- q and held-out ratio formulas.

CANDIDATE PHYSICS:
- the AoE low-l temperature component is proportional to this axis-contracted tidal Green response;
- q obeys the dyadic shell law;
- the inferred d corresponds to a physical relational centre.

CONTAMINATED/EXPLORATORY FOR v0.3:
- Planck-2013 low-l coefficients already inspected before this freeze.
