# CIR AoE Off-Centre Green-Shadow Model v0.1

Status: CANDIDATE FORWARD MODEL / PROSPECTIVE SCALE INVERSION
Date: 2026-09-26

## Purpose

Test the specific hypothesis that a component of the aligned CMB low-l field is the projection of an off-centre, approximately harmonic potential-like source/centre onto an observation sphere.

This is deliberately narrower than the general "Axis of Evil = black-hole-like shadow" hypothesis. Failure of this model does not falsify every possible horizon-shadow model.

## Geometry

Let the observation sphere have radius R_S. Let the candidate source/centre be displaced from the observer by

  d = epsilon R_S,
  0 <= epsilon < 1,

along an unoriented axis a.

For sky direction n define

  mu = a dot n.

The dimensionless Green kernel is

  K(mu;epsilon) = 1/sqrt(1 - 2 epsilon mu + epsilon^2).

## Exact Legendre expansion

For |epsilon|<1, the Legendre generating function gives

  K(mu;epsilon)
  = sum_{ell=0}^infinity epsilon^ell P_ell(mu).

Thus if the candidate shadow component is linear in this kernel,

  S(mu) = A K(mu;epsilon),

its Legendre coefficients are exactly

  g_ell = A epsilon^ell.

After removing monopole and dipole, the first relevant terms are

  g_2 = A epsilon^2,
  g_3 = A epsilon^3.

Therefore

  |epsilon| = |g_3/g_2|

provided g_2 != 0.

The absolute value makes the estimator invariant under reversal of the unoriented AoE axis, because a -> -a flips odd ell and leaves even ell unchanged.

## Map-space estimator

For a fixed axis a, define the azimuthal average

  Tbar(mu) = (1/2pi) integral_0^{2pi} T(mu,phi) dphi.

Define the Legendre projection

  g_ell = (2ell+1)/2 integral_{-1}^{1} Tbar(mu) P_ell(mu) dmu.

Equivalently, this isolates the m=0 component in the coordinate system whose polar axis is a, with a known spherical-harmonic normalization.

The primary geometric estimator is

  epsilon_23 = |g_3/g_2|.

## Dyadic shell test

The local log-scale representation supplies the candidate discrete law

  epsilon = 2^{-n},
  n in Z_{>=0}.

Therefore define before any black-hole target inspection

  n_cont = -log2(epsilon_23),

  eta = n_cont - round(n_cont).

No rounding is used to create the prediction. The continuous n_cont and its propagated uncertainty are the primary output; integer consistency is a separate test of the dyadic hypothesis.

## Radial location

Once an independently frozen observation-sphere radius R_S is supplied,

  d_pred = epsilon_23 R_S.

Together with the unoriented AoE direction a this gives the antipodal pair

  x_pred = +/- d_pred a.

A later physical model must break the sign degeneracy using an odd-parity or independent directional observable.

## Required controls

1. Hold the AoE axis fixed upstream.
2. Do not rotate the axis to maximize |g_3/g_2| after map inspection.
3. Evaluate at least one alternate component-separated CMB map.
4. Propagate map/mask uncertainty.
5. Report whether the m=0 axisymmetric component is actually large enough for this model to be meaningful.
6. Do not identify the resulting d_pred with a black-hole location before the scale inversion is frozen.

## Falsification

The simple Green-shadow candidate fails if, under the frozen axis and map pipeline:

- g_2 is consistent with zero, making the ratio unidentified;
- the inferred epsilon is >=1;
- map/component-separation changes make epsilon unstable beyond the declared uncertainty;
- or the axisymmetric m=0 component is negligible compared with the non-axisymmetric low-l power.

A dyadic sub-hypothesis additionally fails if n_cont is inconsistent with every integer under the frozen uncertainty rule.

## Epistemic boundary

EXACT:
- Legendre generating-function identity;
- g_{ell+1}/g_ell = epsilon inside the declared linear Green kernel.

CANDIDATE:
- a component of the CMB AoE is described by this kernel;
- epsilon follows the dyadic shell law.

OPEN:
- metric/horizon forward model connecting this Green component to a black-hole-like parent;
- physical radius R_S appropriate to that parent-domain interpretation;
- sign resolution and final three-dimensional source identification.
