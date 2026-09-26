# CIR AoE WMAP9 Directional Cross-Experiment Audit v0.1

Status: INDEPENDENT-INSTRUMENT DIRECTIONAL CROSSCHECK / NON-DECISIVE
Date: 2026-09-26

## Frozen reference

The reference axis was frozen from Planck low-l information before this WMAP9 check:

  a_P = (l,b)
      = (239.9881633256477 deg, 68.5117419161366 deg),

treated as an unoriented axis.

No WMAP value was used to alter this direction.

## WMAP9 published axes

Rassat, Starck & Dupe, A&A 557, A32 (2013), DOI 10.1051/0004-6361/201219793, report for WMAP9:

Before inpainting:
- quadrupole: (l,b)=(-124.1 deg, 58.1 deg) = (235.9 deg,58.1 deg);
- octupole:   (l,b)=(-122.3 deg, 62.9 deg) = (237.7 deg,62.9 deg).

After sparse inpainting:
- quadrupole: (225.5 deg,54.8 deg);
- octupole:   (249.2 deg,57.7 deg).

After inpainting plus reconstructed 2MASS+NVSS ISW subtraction:
- quadrupole: (269.9 deg,40.8 deg);
- octupole:   (262.8 deg,65.1 deg).

The official WMAP nine-year analysis separately reports an approximately 3-degree quadrupole-octupole misalignment in the nine-year ILC, but emphasizes that CMB/foreground separation substantially degrades its significance below 3 sigma.

## Angular separation from the frozen Planck reference

Using the unoriented great-circle distance

  Delta(a,b)=acos(|a dot b|),

the separations are:

| WMAP9 processing | ell=2 to frozen Planck axis | ell=3 to frozen Planck axis |
|---|---:|---:|
| raw / before inpainting | 10.5668 deg | 5.6892 deg |
| sparse inpainting | 15.2503 deg | 11.5574 deg |
| inpainting + ISW subtraction | 31.9662 deg | 9.5420 deg |

The raw WMAP9 quadrupole-octupole axis separation from these published coordinates is 4.8807 deg.

## Interpretation

The WMAP9 octupole direction remains within about 6-12 degrees of the frozen Planck axis across the listed processing variants.

The quadrupole is more processing-sensitive and moves to about 32 degrees from the frozen Planck axis after ISW subtraction.

Therefore:

  CROSS_EXPERIMENT_DIRECTIONAL_COMPATIBILITY = PRESENT_BUT_NOT_ROBUST_ENOUGH_FOR_PASS.

This is consistent with the literature conclusion that the large-angle alignment is sensitive to foreground/secondary-anisotropy treatment.

## Relation to the corrected shadow pipeline

This audit supports retaining a fixed cross-experiment direction as a useful observable, but it does NOT validate any radial scale law.

The corrected shadow interface must operate on the full rotated a_lm vector and planar/high-|m| statistics. No m=0 scale estimate is inferred here.

## Verdict

  DIRECTION_ONLY = TENSIONED_COMPATIBILITY / NON-DECISIVE
  RADIAL_SCALE = NOT_TESTED
  SHADOW_PHYSICS = NOT_ADJUDICATED
