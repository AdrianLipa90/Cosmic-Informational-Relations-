# CIR WMAP9 Two-Axis Radial Direction Diagnostic v0.1

Status: EXPLORATORY / POST-HOC SAME-DATA DIRECTIONAL DIAGNOSTIC
Date: 2026-09-26

## Inputs already inspected before this diagnostic

From the previously recorded WMAP9 directional audit:

  quadrupole axis:
    (l,b) = (235.9 deg, 58.1 deg)

  octupole axis:
    (l,b) = (237.7 deg, 62.9 deg)

These coordinates were already visible before the present centre-direction construction, so this diagnostic is not prospective evidence.

## Exact inversion

The acute axis separation is

  gamma = 4.8806578552 deg.

Therefore the directional conditioning factor is

  1/sin(gamma)
  = 11.75356517.

The normalized cross product gives the unoriented radial-axis pair

  s_+:
    (l,b) = (137.65831979 deg, +5.09881875 deg)

  s_-:
    (l,b) = (317.65831979 deg, -5.09881875 deg).

These are antipodal representations of the same unoriented axis.

## Interpretation

Under the conditional hypothesis that the WMAP9 l=2 and l=3 preferred axes are two tangent directions of one common centre geometry, the inferred radial axis lies close to the Galactic plane.

This does not establish a Galactic origin or a cosmological centre.

Instead it strengthens the requirement for a foreground/systematics firewall because the derived direction is geometrically close to b=0 by construction from these particular observed axes.

## Conditioning warning

Because gamma is only about 4.88 degrees, small changes in either input axis are amplified by about a factor 11.75 in the radial direction.

For illustration only, a combined one-degree perturbation budget in the two tangent axes can induce an order-ten-degree radial shift at first order.

Therefore this WMAP9 cross-product direction is not a high-precision centre estimate.

## Verdict

  RADIAL_AXIS_FROM_WMAP9_TWO_TANGENTS
  = IDENTIFIED_BUT_ILL_CONDITIONED / EXPLORATORY

  HIGH_PRECISION_CENTRE_FROM_AOE_AXIS_PAIR
  = NOT_SUPPORTED

  FOREGROUND_FIREWALL
  = REQUIRED

No target catalogue is searched in this diagnostic.
