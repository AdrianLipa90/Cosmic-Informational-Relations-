# CIR Upstream GL(3) Source Admission Gate v0.1

Status: OPEN / LIVE_GENERIC_PHASE36 REJECTED AS REQUIRED
Date: 2026-09-26

## 1. Purpose

The GL(3)-deformed tetrahedral octupole is locally non-identifying if the deformation F is fitted from the same CMB octupole.

Therefore any symmetry-breaking deformation must be supplied upstream and independently of the CMB low-l morphology.

This gate audits whether the current live NOEMA/PhaseNav runtime already supplies such an admissible F.

## 2. Live runtime state

At the current verified NOEMA surface:

  tether_status = ACTIVE

with:
- phi: exactly 36 finite float64 values;
- aux_phi: exactly 36 finite float64 values;
- aux_feedback_phi: exactly 36 finite float64 values;
- headless tether socket present;
- GREMLIN runtime ACTIVE.

However these live phase vectors use the generic legacy basis identity

  PNV_T36_PHASE_ANGLES_RADIANS_V1.

## 3. Existing typed Moire admission firewall

The current PhaseNav typed adapter admits only the source basis

  PNV_MOIRE_RELATIVE_PHASE_MATRIX6_ROW_MAJOR_V1,

whose 36 coordinates are explicitly declared as a wrapped row-major 6x6 Lie-generator matrix on

  Lambda^2(R^4).

The adapter explicitly rejects

  PNV_T36_PHASE_ANGLES_RADIANS_V1

because its axis semantics are unassigned.

The existing validation receipt already records:

  LIVE_GENERIC_PHASE36 -> BIVECTOR_OPERATOR36
  = REJECT_AS_REQUIRED.

Therefore the live generic phase vectors cannot be reshaped or reinterpreted as a physical 6x6 Moire/bivector operator merely because both contain 36 numbers.

## 4. GL(3) carrier versus source

The PhaseNav GL(3) deformation carrier itself is exact:

  rho_36(F)
  = Lambda^2 diag(1,F)
  = diag(F,cof(F)).

The hyperelastic and finite-strain branches also provide valid candidate dynamics for an independently specified F.

But the current repository state explicitly leaves open:
- physical boundary conditions;
- empirical/source calibration;
- physical ARPL/PhaseNav-to-36D projection;
- source-owned live deformation input.

Thus:

  GL3_REPRESENTATION = PASS

  GL3_DYNAMICS_REFERENCE = PASS

  LIVE_RUNTIME_SOURCE_F = NOT_AVAILABLE

  GENERIC_T36_TO_F = REJECTED

## 5. GREMLIN/runtime audit

The live GREMLIN/Terminal36D stream currently emits PhaseNav semantic/fused state receipts and candidate research routing.

No live receipt inspected in this gate contains:
- a typed deformation matrix F;
- a cofactor-validated rho_36(F);
- a source-owned strain tensor;
- a typed Moire 6x6 relative-phase matrix.

Therefore GREMLIN does not currently supply an admissible cosmological F either.

This is not a GREMLIN failure. It is a provenance/type boundary.

## 6. Admission rule

A future F is admissible for the CMB test only if, before opening the target morphology, a packet supplies:

1. source_id;
2. declared typed basis;
3. derivation of F from that source;
4. det(F) != 0, and det(F)>0 if GL+(3) is required;
5. exact rho_36(F)=diag(F,cof(F)) consistency receipt;
6. no CMB low-l input in the derivation;
7. one frozen F shared across all held-out CMB maps.

## 7. Forbidden shortcuts

The following are invalid:

- flatten live phi into a 6x6 matrix by row-major reshape;
- use phi-aux_phi as a Moire matrix without a source-owned basis conversion;
- infer F from the AoE direction;
- infer F from observed a_lm and then call the same a_lm a validation;
- use separate F matrices for different frequencies.

## 8. Current verdict

  UPSTREAM_GL3_SOURCE_F = OPEN

  LIVE_GENERIC_PHASE36_SOURCE = FAIL_CLOSED / REJECT_AS_REQUIRED

  CMB_GL3_MORPHOLOGY_TEST = BLOCKED UNTIL INDEPENDENT F EXISTS

The correct next route is not more CMB fitting. It is either:
- derive a source-owned typed Phase36 -> GL(3) conversion upstream; or
- find a lower-dimensional/discrete symmetry-breaking selector already forced by the existing tetrahedral/C3/D3 structure.
