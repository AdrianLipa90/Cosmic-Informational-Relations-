# CIR C3-Face Freeze Provenance Correction v0.1

Status: APPEND-ONLY CORRECTION
Date: 2026-09-27

## Error

The original file

  schemas/CIR_C3_SELECTED_TETRAHEDRAL_FACE_FREEZE_V0_1.json

listed WMAP1/3 multipole vectors, Planck-2013 multipole vectors, and ELC2026
low-l powers as contaminated for prospective validation of the newly derived
C3-face model.

It omitted one dataset that had also already been inspected before the C3-face
translation coefficient was derived:

  Planck PR3 TT low-l powers
  D2 = 225.895 uK^2
  D3 = 936.920 uK^2.

Those values were opened earlier while evaluating the previous ideal-A4
tetrahedral translation estimator.

## Corrected provenance rule

Therefore Planck PR3 D2/D3 is also

  CONTAMINATED / POST-HOC ONLY

for every prediction that depends on the NEW C3-face coefficient

  q = (5 sqrt(82)/49) sqrt(D2/D3).

It may not be counted as a prospective test of:
- the C3-selected tetrahedral-face translation coefficient;
- the joint C3-face + C6/ARPL prediction D2/D3=2401/73800.

The earlier PR3 audit remains valid as a held-out test of the older frozen
ideal-A4 estimator, because that older freeze preceded opening PR3.

## Scope

No numerical result is deleted or changed.

This correction changes only the provenance class of PR3 relative to the later
C3-face model.

The next prospective power-spectrum test of the C3-face coefficient must use
a low-l amplitude dataset not inspected before this correction.
