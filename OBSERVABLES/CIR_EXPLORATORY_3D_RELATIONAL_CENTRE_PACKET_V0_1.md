# CIR Exploratory 3D Relational-Centre Packet v0.1

Status: EXPLORATORY COMBINATION / RADIAL SCALE MORE STABLE THAN DIRECTION
Date: 2026-09-26

## 1. Inputs

### Radial amplitude branch

From the already recorded 2026 ELC held-out continuous tetrahedral-translation inversion:

  d_mean = 2350.770443 Mpc
         ~= 2.35077 Gpc
         ~= 7.66718 Gly comoving.

Across the six ELC cross-spectra the point-estimate radial range is approximately

  2275.3 Mpc to 2427.5 Mpc.

This cross-spectrum spread is a robustness diagnostic, not a formal statistical confidence interval.

The integer dyadic zero-offset hypothesis already failed and is not resurrected here.

### Direction branch

From the already-inspected WMAP9 quadrupole/octupole preferred axes, the conditional two-tangent inversion is

  s = +/- normalize(a2 x a3).

This direction is post-hoc/exploratory because the WMAP axes had already been inspected before the cross-product centre construction.

## 2. Raw-WMAP exploratory point

Using the raw WMAP9 axes:

  a2 = (l,b)=(235.9 deg,58.1 deg),
  a3 = (l,b)=(237.7 deg,62.9 deg),

gives

  s_+ = (137.6583198 deg,+5.0988187 deg),
  s_- = antipode.

Combining s_+ with d_mean gives Galactic Cartesian comoving coordinates

  (X,Y,Z)
  =
  (-1730.676,
   +1577.097,
   +208.922) Mpc,

with the antipodal solution carrying the opposite sign.

This is a model-coordinate packet, not an observed object.

## 3. Processing sensitivity of the radial direction

Using the same WMAP9 directional source already recorded in the repository:

| Processing | gamma(a2,a3) | conditioning 1/sin(gamma) | radial axis (l,b), one antipode |
|---|---:|---:|---|
| raw | 4.8807 deg | 11.7536 | (137.6583 deg,+5.0988 deg) |
| sparse inpainting | 13.4084 deg | 4.3124 | (71.9773 deg,+32.2696 deg) |
| inpainting + ISW subtraction | 24.6381 deg | 2.3987 | (184.5998 deg,-5.4224 deg) |

The inferred radial direction is therefore not robust under the published low-l processing variants.

## 4. Structural conclusion

The current candidate separates into two very different identifiability classes:

RADIAL:
- the continuous C2/C3 scale inversion is numerically fairly stable across six 2026 ELC cross-spectra;
- its physical tetrahedral binding remains unvalidated;
- the integer dyadic subhypothesis failed.

ANGULAR:
- two-axis inversion is exact geometry;
- the AoE alignment makes it ill-conditioned;
- published processing changes produce large changes in the inferred radial axis;
- no unique upstream PhaseNav edge/GL3 selector currently exists.

Therefore:

  RADIAL_CANDIDATE_SCALE = IDENTIFIED_CONDITIONALLY

  UNIQUE_CENTRE_DIRECTION = NOT_ROBUST

  PRECISE_3D_CENTRE = NOT_ESTABLISHED

## 5. No black-hole catalogue search

No black-hole mass, distance or sky position is used to construct this packet.

This preserves the intended order:

  derive candidate geometry first
  -> freeze
  -> only later compare against independent external populations.

A future catalogue comparison may test this packet, but may not be used to choose between its directional variants.
