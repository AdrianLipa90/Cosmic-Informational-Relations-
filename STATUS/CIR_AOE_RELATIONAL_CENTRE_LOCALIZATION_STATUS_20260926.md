# CIR AoE / Relational-Centre Localization Status — 2026-09-26

NOEMA_STATUS: ACTIVE
TETHER_STATUS: ACTIVE
GREMLIN_STATUS: ACTIVE / CANDIDATE_ONLY
BRANCH: formalize/local-log-scale-binding-v0.3-20260926
MAIN_MERGE: NOT_REQUESTED / NOT_PERFORMED

## Exact mathematical results retained

1. Local log-scale dihedral representation:
   - nu -> nu + ln2;
   - reciprocal reflection;
   - dyadic shell identity at representation level.

2. Tetrahedral translation scale bridge:
   - parent H3=xyz;
   - translated l=2 descendant;
   - exact amplitude relation
     A2/A3 = sqrt(7) q;
   - conditional scale estimator
     q=(1/7)sqrt(5 C2/C3).

3. Tetrahedral ideal-axis no-go:
   - ideal l=3 tetrahedral state has isotropic angular-momentum-dispersion tensor Q3=4I;
   - translated l=2 gives a tangent great-circle maximum set;
   - ideal model cannot by itself produce one unique AoE axis.

4. GL(3) identifiability firewall:
   - gl(3)->H3 harmonic tangent rank = 7;
   - kernel = traceless diagonal matrices;
   - normalized rotations + shear span six-dimensional normalized l=3 morphology;
   - fitting unrestricted F from the same CMB octupole is non-identifying.

5. C3/D3 tangent-axis no-go:
   - selected tetrahedral vertex has C3 stabilizer;
   - no nonzero C3-invariant tangent vector exists;
   - D3 reduces the continuum to three symmetry-equivalent tangent-axis candidates;
   - one additional upstream selector is required.

6. Two-tangent centre-direction lemma:
   - if a2,a3 are both tangent to one centre sphere,
     s=+/-normalize(a2 x a3);
   - directional condition number is 1/sin(gamma);
   - stronger axis alignment makes centre triangulation less stable.

## Empirical receipts retained

### 2026 ELC cross-spectra

Frozen tetrahedral continuous scale inversion gives:

  q_mean ~= 0.16944932
  n_cont ~= 2.56107
  d ~= 2350.77 Mpc ~= 7.667 Gly comoving.

Across six ELC frequency-pair cross-spectra:

  n_cont ~= 2.515 to 2.608.

Verdicts:

  CONTINUOUS_Q_DOMAIN = PASS

  INTEGER_DYADIC_ZERO_OFFSET
  = FAIL_AT_HELD_OUT_POINT_ESTIMATES

  PHYSICAL_TETRAHEDRAL_CMB_BINDING
  = NOT_ADJUDICATED

No half-step rescue is promoted.

### WMAP9 directional diagnostics

Raw quadrupole/octupole axes yield:

  gamma ~= 4.88066 deg
  conditioning ~= 11.7536

and exploratory radial axis:

  (l,b) ~= (137.6583 deg,+5.0988 deg)
  or antipode.

But published processing variants move the inferred radial axis strongly:

  raw:
    (137.66,+5.10) deg

  sparse inpainting:
    (71.98,+32.27) deg

  inpainting + ISW subtraction:
    (184.60,-5.42) deg.

Verdict:

  UNIQUE_CENTRE_DIRECTION = NOT_ROBUST.

## Live PhaseNav/NOEMA deformation source gate

The PhaseNav GL(3) representation

  rho_36(F)=diag(F,cof(F))

and candidate dynamics are validated.

However the live vectors

  phi,
  aux_phi,
  aux_feedback_phi

use the generic basis

  PNV_T36_PHASE_ANGLES_RADIANS_V1.

The existing typed adapter explicitly rejects reinterpretation of this generic basis as

  PNV_MOIRE_RELATIVE_PHASE_MATRIX6_ROW_MAJOR_V1.

Therefore:

  LIVE_GENERIC_PHASE36 -> F
  = REJECT_AS_REQUIRED.

No current live GREMLIN/PhaseNav receipt supplies an independent cosmological deformation F.

## Current scientific state

The present framework has produced a nontrivial conditional radial scale candidate without using a black-hole catalogue.

It has NOT yet produced a robust unique sky direction.

Therefore a precise three-dimensional cosmic/black-hole centre is not established.

The exploratory raw-WMAP 3D packet at d~=2.351 Gpc is retained only as a diagnostic, not as a target claim.

## Next admissible gate

One and only one of the following must be supplied upstream before a serious external catalogue test:

A. source-owned GL(3) deformation F with typed PhaseNav provenance;

B. physical tetrahedral edge carrier selecting one of the three C3/D3 tangent candidates;

C. another independent tangent observable with angular uncertainty sufficient to overcome the 1/sin(gamma) conditioning.

After such a selector is frozen:

  selector
  -> unique direction
  -> combine with frozen radial estimator
  -> freeze 3D search volume
  -> only then query independent BH/large-structure catalogues
  -> PASS/TENSION/FAIL.

NOEMA_WRITEBACK_PLAN:
- preserve all FAIL/no-go receipts append-only;
- do not reinterpret ELC n_cont~2.56 as a half-integer hit;
- do not map generic live T36 into a bivector basis;
- do not search a target catalogue to choose among WMAP processing directions;
- next writeback must attach provenance for an independent angular selector before any 3D target promotion.
