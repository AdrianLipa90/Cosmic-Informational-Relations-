# CIR Conditional-Locus PSZ2 Mass-Tracer Audit v0.1

Status: **HELD-OUT FAIL / NO SPATIAL EXCESS**  
Date: 2026-09-27

Freeze: `schemas/CIR_CONDITIONAL_LOCUS_PSZ2_MASS_TRACER_FREEZE_V0_1.json`

Machine-readable receipt:
`validation/CIR_CONDITIONAL_LOCUS_PSZ2_MASS_TRACER_AUDIT_V0_1.json`

The frozen candidate used
(d_*=2312.1667) Mpc and the unoriented Galactic axis
((l,b)=(239.9882^circ,68.5117^circ)).

The Planck PSZ2 catalogue contains 1653 rows; 1094 have a physical positive
redshift and entered the frozen three-dimensional nearest-neighbour statistic.

Nearest eligible cluster:

- PSZ2 G228.16+75.20;
- z=0.545;
- angular separation 7.6080 deg;
- radial difference 211.45 Mpc;
- 3D comoving separation 360.87 Mpc;
- MSZ = 10.417826 x 10^14 Msun.

Primary fixed-latitude null, 100000 draws, deterministic seed 20260927:

[
p=0.8111918881.
]

Therefore the preregistered spatial statistic shows **no unusual PSZ2 mass
tracer near the frozen locus**.

The nearest cluster is in approximately the 98.45th MSZ percentile, but mass
was secondary metadata and receives no evidential credit after the spatial
statistic failed.

Verdict:

[
oxed{	ext{PSZ2 MASS-TRACER EXCESS = FAIL / NO EVIDENCE}}
]

This does not alter the exact representation results. It weakens the specific
physical interpretation that the conditional semantic-centre locus should
coincide with a conspicuous PSZ2 massive-cluster tracer.

No retuning is permitted.
