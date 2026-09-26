# CIR Two-Tangent-Axis Centre-Direction Lemma v0.1

Status: EXACT GEOMETRY / DIRECTIONAL CONDITIONING THEOREM
Date: 2026-09-26

## 1. Setup

Let s be an unknown unoriented radial direction from the observer toward a candidate relational centre.

Suppose two independently defined sky directions a_2 and a_3 are both tangent to the same sphere centred on s, so that

  a_2 · s = 0,
  a_3 · s = 0.

If a_2 and a_3 are not parallel, then their common normal is unique up to sign:

  boxed[
  s
  = +/- (a_2 x a_3)/||a_2 x a_3||
  ].

Thus two nonparallel tangent-axis observables are sufficient in exact geometry to determine one unoriented radial direction.

## 2. Conditioning

Let

  gamma = acos(|a_2 · a_3|)

be the acute angle between the two unoriented axes.

Then

  ||a_2 x a_3|| = sin gamma.

The normalized cross-product map therefore has first-order sensitivity proportional to

  boxed[
  kappa_dir = 1/sin gamma
  ].

A conservative small-error bound is

  delta theta_s
  <=
  (delta theta_2 + delta theta_3)/sin gamma
  + higher-order terms.

Therefore:

- orthogonal tangent axes give good conditioning;
- nearly aligned axes give poor conditioning;
- exact alignment gamma=0 makes the radial direction unidentified.

## 3. Axis-of-Evil consequence

The standard AoE phenomenon is precisely that the low-l preferred axes are unusually aligned.

Therefore using only the quadrupole and octupole preferred axes to infer a centre direction is geometrically ill-conditioned.

This is not a statistical statement about whether the AoE is cosmological. It is an exact consequence of cross-product geometry.

In compact form:

  stronger l=2/l=3 alignment
  => weaker radial triangulation from those two axes alone.

## 4. Precision requirement

For target radial angular precision epsilon_s, the two tangent axes require combined angular uncertainty roughly below

  delta theta_2 + delta theta_3
  << epsilon_s sin gamma.

If gamma is only a few degrees, sub-degree radial localization requires axis uncertainties far below one degree.

Thus a claim of extremely precise centre localization cannot follow from the AoE alignment alone.

A third independent tangent/phase observable or a source-owned discrete selector is needed to improve conditioning.

## 5. Relation to the tetrahedral model

In the translated-tetrahedral candidate:

- the physical radial direction is s;
- the induced quadrupole maximum-dispersion axis lies in s-perp;
- any symmetry-broken octupole preferred axis intended to share the same centre should also lie in s-perp.

Hence the cross-product construction is the correct exact two-axis inversion if those two tangent conditions are independently established.

It does not require GL(3).

## 6. Epistemic boundary

EXACT:
- s is the normalized cross product of two nonparallel tangent axes;
- conditioning scales as 1/sin gamma;
- exact alignment destroys radial identifiability.

OPEN:
- whether observed CMB l=2 and l=3 preferred axes are both physical tangent observables of one centre;
- foreground/systematic contamination;
- physical black-hole interpretation.

No catalogue target enters this lemma.
