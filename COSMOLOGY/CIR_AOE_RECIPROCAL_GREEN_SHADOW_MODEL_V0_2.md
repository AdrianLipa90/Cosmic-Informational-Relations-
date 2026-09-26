# CIR AoE Reciprocal Green-Shadow Model v0.2

Status: CANDIDATE FORWARD MODEL / FROZEN BEFORE LOW-L COEFFICIENT EVALUATION
Date: 2026-09-26

This v0.2 supersedes v0.1 for future evaluation while preserving v0.1 unchanged as provenance. The change was made before evaluating the frozen Planck low-l m=0 coefficients.

## 1. Exact source/sphere geometry

Let an observation sphere have radius R>0 and let a point-like harmonic source/centre lie at distance d>0 from the observer along axis a. For sky direction n, mu=a dot n,

  G(mu;R,d) = 1 / sqrt(R^2 + d^2 - 2 R d mu).

There are two convergent Legendre expansions.

### Interior-source branch: d<R

  G = (1/R) sum_{ell=0}^infinity (d/R)^ell P_ell(mu).

### Exterior-source branch: d>R

  G = (1/d) sum_{ell=0}^infinity (R/d)^ell P_ell(mu).

Define

  x := d/R,
  q := min(x,1/x) = exp(-|ln x|),  0<q<1.

Then in either branch the adjacent Legendre-coefficient magnitude ratio is

  |g_{ell+1}/g_ell| = q.

Thus the low-l sky determines q but is exactly degenerate under the reciprocal map

  x -> 1/x,
  d/R -> R/d.

## 2. Log-radius form

Let

  B := ln(d/R).

Then reciprocal inversion is

  B -> -B,

and

  q = exp(-|B|).

For the dyadic candidate q=2^{-n},

  |B| = n ln 2,

so the two reciprocal radial branches are

  d_- = R 2^{-n},
  d_+ = R 2^{+n}.

This is the physical radial realization of the local log-scale reflection/translational algebra.

The singular boundary d=R corresponds to n=0 and is excluded for a point source lying exactly on the observation sphere.

## 3. Low-l estimator

With the fixed sky axis rotated to +z,

  g_ell = sqrt[(2ell+1)/(4pi)] a_{ell0}^{(a)}.

Therefore

  q_23 = |g_3/g_2|
       = sqrt(7/5) |a_{30}^{(a)}/a_{20}^{(a)}|,

and

  n_cont = -log2(q_23).

No source catalog is needed to obtain q_23 or n_cont.

## 4. Physical radial prediction

After freezing an independently justified observation-sphere radius R,

  d_in  = R q_23,
  d_out = R/q_23.

If the dyadic sub-hypothesis survives,

  d_in  = R 2^{-n},
  d_out = R 2^{+n}.

The sky position prediction is the reciprocal pair of radial shells along the fixed unoriented axis:

  x_in  = +/- d_in a,
  x_out = +/- d_out a.

The axis sign and inside/outside degeneracies require independent observables; they may not be broken by choosing whichever known black hole looks attractive.

## 5. Held-out cross-multipole test

Infer q only from ell=2,3.

Then predict, before inspection,

  |g_4/g_3| = q,
  |g_5/g_4| = q.

Failure of these held-out ratios rejects the single-kernel Green-shadow component as a complete low-l explanation under the declared extraction pipeline. A more general shadow model would require a new freeze.

## 6. Connection to local dihedral representation

The radial log coordinate B has reflection

  J(B)=-B.

A dyadic shell translation is

  T(B)=B+ln2.

Thus the radial branches d/R=2^{+/- n} are precisely the reciprocal pair generated around the local anchor R.

This does not make the physical Green-shadow hypothesis exact; it shows that, if admitted, its radial geometry realizes the already established log-scale representation without an extra fitted base.

## 7. Falsification

Primary Green-shadow failure if:
- a_{20}^{(a)} is consistent with zero so q is unidentified;
- q_23 >= 1;
- q_23 is unstable across the preregistered map/mask robustness set;
- held-out ell=4,5 ratios fail the frozen prediction beyond propagated uncertainty.

Additional dyadic failure if the uncertainty interval for n_cont excludes all integers under the preregistered rule.

## 8. No-retune rule

After low-l coefficient evaluation begins:
- axis fixed;
- base 2 fixed;
- zero shell offset fixed;
- q estimator fixed;
- reciprocal interpretation fixed;
- R-anchor policy fixed separately before astronomical target comparison.

No target mass, target radius or target catalog position may be used to alter these quantities.
