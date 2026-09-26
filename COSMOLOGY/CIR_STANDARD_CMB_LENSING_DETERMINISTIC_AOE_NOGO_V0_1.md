# CIR Standard CMB-Lensing Deterministic-AoE No-Go v0.1

Status: STANDARD-LENSING IDENTIFIABILITY NO-GO / DIRECT-IMPRINT MODEL KEPT SEPARATE
Date: 2026-09-26

## 1. Standard CMB lensing response

For a scalar CMB lensing potential psi on the sky, standard weak gravitational lensing remaps the unlensed temperature field rather than replacing it by psi.

Schematically,

  boxed[
  T_lensed(n)
  = T_unlensed(n + grad psi(n)).
  ]

At first order,

  delta T(n)
  = grad_a psi(n) grad^a T_unlensed(n).

Therefore the induced harmonic perturbation is bilinear in

  psi

and the particular unlensed CMB realization.

## 2. No deterministic low-l temperature prediction from psi alone

Fixing a lens potential psi does NOT uniquely determine

  a_2m,
  a_3m

of the observed temperature sky.

Different unlensed CMB realizations passed through the same psi produce different lensed low-l coefficients.

Consequently,

  boxed[
  source lens potential alone
  NOT-IMPLIES
  deterministic Axis-of-Evil temperature pattern.
  ]

This is an identifiability statement inside the standard lens-remapping model.

## 3. What lensing does predict

A fixed lensing potential predicts statistical mode coupling and position-dependent remapping.

This is why CMB lensing reconstructions use induced correlations / quadratic estimators rather than treating the lens potential as a temperature template.

Thus a physically standard Kerr-lensing interpretation should target observables such as:

- reconstructed CMB lensing potential;
- off-diagonal harmonic covariance;
- temperature-gradient correlations;
- polarization remapping / E-to-B conversion;
- source-aligned shear/flexion signatures.

## 4. Consequence for CIR AoE work

The earlier tetrahedral translation model

  H3 -> translated H2

with its direct C2/C3 scale estimator is NOT standard CMB lensing. It is a separate DIRECT-IMPRINT candidate in which a source-mode field is assumed to contribute directly to the low-l scalar temperature component.

That model remains recorded with its own held-out results and FAILs.

It must not be retrospectively relabelled as ordinary gravitational lensing.

## 5. Two admissible branches

### A. Direct-imprint branch

Requires a physical response theorem

  source phase/geometry
  -> Delta T_direct(n).

Then low-l amplitude ratios may be direct source predictions.

### B. Standard-lensing branch

Uses

  source
  -> psi(n)
  -> remapping of an independent primordial CMB field.

Here the primary prediction is mode coupling / lensing reconstruction, not a fixed raw a_lm template.

## 6. New prospective target

The Phase-Optics spin-2/spin-3 bridge suggests a sharper standard-lensing test:

  Kerr/tetrahedral source
  -> predicted psi geometry
  -> gamma and G3
  -> predicted lensing-potential / mode-coupling morphology
  -> compare with an independent Planck/PR4 or future lensing reconstruction.

This avoids requiring the source to predict the random primordial CMB realization.

## 7. Firewall

Forbidden:
- infer a deterministic AoE temperature template from a lens potential without specifying the unlensed field;
- use the same observed temperature map both to construct the source potential and to validate its lensing remapping;
- merge direct-imprint and lensing evidence classes.

Required:
- declare DIRECT_IMPRINT or STANDARD_LENSING before evaluation;
- preserve independent source provenance and data-split logic.
