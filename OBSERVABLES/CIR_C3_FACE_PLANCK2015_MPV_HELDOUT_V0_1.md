# CIR C3-Face Planck-2015 Multipole-Vector Held-Out Audit v0.1

Status: PROSPECTIVE MORPHOLOGY TEST / EXACT FACE NOT HIT / AXIS-RECONSTRUCTION PARTIAL COMPATIBILITY / STATISTICAL VERDICT NON-DECISIVE
Date: 2026-09-27

## Freeze precedence

The test method was frozen before opening the four Pinkwart-Schwarz Planck-2015 MPV files:

  schemas/CIR_C3_FACE_PLANCK2015_MPV_METHOD_FREEZE_V0_1.json

The frozen exact face prediction is

  |v_i dot v_j| = 1/3

for all three octupole multipole-vector pairs.

The frozen residual is

  R_face
  = sqrt( mean_{i<j} ( |v_i dot v_j| - 1/3 )^2 ).

The model also predicts that, after a consistent projective orientation with all three signed pair products negative,

  s_rec = -(v1+v2+v3)/|v1+v2+v3|

is the unique maximum-angular-momentum-dispersion (MAMD) axis of the octupole.

No GL(3) deformation is admitted in this test.

## Source

Pinkwart & Schwarz, Phys. Rev. D 98, 083536 (2018), arXiv:1803.07473.

Public repository:

  MPinkwart/MPV-files-Pinkwart-Schwarz

Files:
- COMMANDER_MPVs.txt, sha a0043a80fb6497b2e08cfad988d92cca67f0ee4e
- NILC_MPVs.txt,      sha 16088587c42b663c9cb666ee509086d0179aafdc
- SEVEM_MPVs.txt,     sha 4548437395be5657556f2839be1a89e0c36c7537
- SMICA_MPVs.txt,     sha 7e4fb21c93fbaa57338fd18582411cb7fda2f56c

The repository specifies that lines 3-5 are the three l=3 vectors when counting the text-file rows from one.

## Octupole input vectors, Galactic (l,b) degrees

COMMANDER:
- (86.34663, 38.42042)
- (25.56401, 8.81346)
- (-42.26413, 4.95101)

NILC:
- (86.81043, 37.68892)
- (-44.69731, 7.85774)
- (23.20239, 9.29508)

SEVEM:
- (140.53719, 0.57996)
- (61.27135, 35.04181)
- (33.00704, 5.38588)

SMICA:
- (88.09357, 38.77928)
- (-45.20573, 10.50218)
- (22.14418, 8.84982)

## Frozen face residual

| Map | absolute pair dots | pair angles [deg] | R_face | mean | min | max |
|---|---|---|---:|---:|---:|---:|
| COMMANDER | 0.4731300, 0.4334514, 0.3847619 | 61.7623, 64.3132, 67.3710 | 0.1036205 | 0.4304478 | 0.3847619 | 0.4731300 |
| NILC | 0.4359315, 0.4458888, 0.3898848 | 64.1554, 63.5198, 67.0527 | 0.0937962 | 0.4239017 | 0.3898848 | 0.4458888 |
| SEVEM | 0.1582951, 0.2989124, 0.7718278 | 80.8921, 72.6077, 39.4817 | 0.2733134 | 0.4096784 | 0.1582951 | 0.7718278 |
| SMICA | 0.4115150, 0.4102806, 0.4021850 | 65.7000, 65.7775, 66.2852 | 0.0747748 | 0.4079935 | 0.4021850 | 0.4115150 |

Exact tetrahedral-face morphology would have

  R_face = 0

and all pair angles

  arccos(1/3) = 70.528779 deg.

Therefore:

  EXACT_C3_FACE_GEOMETRY = NOT_HIT

for all four maps.

## Missing-vertex reconstruction

One valid projective orientation with all signed pair products negative gives:

| Map | s_rec representative [l,b] deg | separation from frozen CIR AoE axis |
|---|---|---:|
| COMMANDER | (251.66728, 59.13539) | 10.65792 deg |
| NILC | (241.73313, 60.23538) | 8.30986 deg |
| SEVEM | (305.71129, 39.69541) | 44.74911 deg |
| SMICA | (235.97473, 61.79142) | 6.92512 deg |

The sign-antipodal representatives describe the same unoriented axis.

This comparison is secondary because the primary model prediction is internal morphology plus the self-consistent MAMD relation, not proximity to a separately frozen AoE average.

## Self-consistent MAMD reconstruction from the same MPVs

For each map construct the unique harmonic cubic from the three multipole vectors, compute

  Q_ij = <{L_i,L_j}/2>/<1>,

and take the principal eigenvector as the actual l=3 MAMD axis.

Exact C3-face target eigenvalues:

  (86/41, 86/41, 320/41)
  = (2.09756098, 2.09756098, 7.80487805).

Observed:

| Map | Q eigenvalues | MAMD axis representative [l,b] deg | angle(MAMD,s_rec) |
|---|---|---|---:|
| COMMANDER | 1.5857211, 1.8422152, 8.5720637 | (244.26974, 62.95618) | 5.23055 deg |
| NILC | 1.6465835, 1.8253552, 8.5280613 | (237.97695, 63.12139) | 3.39059 deg |
| SEVEM | 1.0642150, 2.5112928, 8.4244922 | (247.82693, 67.30066) | 41.66115 deg |
| SMICA | 1.7767518, 1.8081745, 8.4150737 | (235.60627, 62.31140) | 0.54791 deg |

Thus the strongest internal compatibility is SMICA, followed by NILC and COMMANDER; SEVEM fails the missing-vertex/MAMD relation badly.

No map is selected as the preferred validation map after inspection. All four remain in the audit.

## Statistical boundary

The method freeze intentionally assigned no arbitrary R_face PASS/FAIL threshold because the public MPV text files do not contain per-vector covariance and no null-calibrated threshold was preregistered.

Therefore the proper statistical verdict is

  PLANCK2015_C3_FACE = NON_DECISIVE_STATISTICALLY.

Descriptively:
- the exact 1/3 face geometry is not realized;
- COMMANDER/NILC/SMICA show a similar moderately deformed face geometry;
- their reconstructed missing vertex is close to their actual octupole MAMD axis;
- SEVEM is qualitatively different.

The source paper independently reports that SEVEM differs from the other three cleaned maps, and also reports no globally abnormal intramultipole correlation. Therefore the numerical regularity above must not be promoted as anomalous without a preregistered null calibration.

## Current verdict

EXACT_C3_FACE = NOT_HIT

MISSING_VERTEX_EQUALS_MAMD:
- COMMANDER: APPROXIMATE
- NILC: APPROXIMATE
- SMICA: CLOSE
- SEVEM: FAIL_DESCRIPTIVELY

STATISTICAL_MODEL_VALIDATION = NON_DECISIVE

PHYSICAL_CMB_TETRAHEDRAL_BINDING = OPEN

No retuning is permitted.
