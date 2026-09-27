# CIR C3-Face Translation Planck-PR4 Axis Held-Out Audit v0.1

Status: PROSPECTIVE STRUCTURAL FAIL
Date: 2026-09-27

## Freeze/provenance

The C3-selected tetrahedral-face model and its no-refit freeze were committed
before opening the Planck PR4/NPIPE quadrupole-octupole Power-tensor alignment
reported by Aluri & Patel.

The exact model corollary is

  theta23_pred = 90 deg.

## Held-out observation

Aluri & Patel analyze the Planck PR4 NPIPE Commander temperature map with the
Power-tensor method.

They report for l=2 and l=3 principal eigenvectors

  theta23_obs approximately 14.8 deg.

They quote random-chance p-values for this observed alignment of

  0.08

using 100 Planck-like simulations and

  0.035

using 5000 ideal CMB simulations.

The paper also notes that foreground residuals tend to misalign intrinsically
aligned modes, so their measured PR4 angle is treated conservatively in their
own interpretation.

## Structural residual

The direct angular mismatch relative to the frozen C3-face translation
prediction is

  |90 - 14.8| = 75.2 deg.

Equivalently,

  model: |n2 dot n3| = 0,
  data:  |n2 dot n3| = cos(14.8 deg) approximately 0.9668.

This is not a significance calculation; it is a direct incompatibility between
the deterministic geometry of the model and the reported PR4 principal-axis
geometry.

## Verdict

  C3_SELECTED_FACE_PLUS_PURE_VERTEX_TRANSLATION = FAIL

This FAIL retires as a physical CMB model:
- the pure translation descendant used to generate l=2;
- the associated C3-face cross-l scale coefficient as a prospective physical
  estimator for the same model.

It does NOT falsify:
- the exact tetrahedral representation identities;
- the C3-selected face octupole geometry as a standalone representation;
- the independent conditional C6/ARPL q=1/6 bridge;
- a future independently sourced deformation/dynamical model.

No retune is permitted.
