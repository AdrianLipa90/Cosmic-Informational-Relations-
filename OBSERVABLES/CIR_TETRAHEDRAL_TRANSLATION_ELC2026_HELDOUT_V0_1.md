# CIR Tetrahedral Translation 2026 ELC Held-Out Audit v0.1

Status: HELD-OUT EVALUATION / CONTINUOUS SCALE STABLE / INTEGER DYADIC ZERO-OFFSET FAIL
Date: 2026-09-26

## Freeze precedence

The evaluated estimator was committed before opening the 2026 ELC cross-spectra:

  q = (1/7) sqrt(5 C2/C3),

  n_cont = -log2 q.

Because the published files use

  D_l = l(l+1) C_l/(2 pi),

the identical estimator is

  q = (1/7) sqrt(10 D2/D3).

Frozen dyadic subhypothesis:

  q = 2^{-n},
  n in positive integers,
  zero offset.

No parameter, coefficient, base, or shell offset was changed after opening the held-out data.

## Held-out dataset

Nofi et al. 2026, Nearly Full-Sky Low-Multipole CMB Temperature Anisotropy II, supplementary ELC_Paper2.

The published final spectra are cross-spectra of four foreground-cleaned CMB maps at 70, 94, 100 and 143 GHz with a 1% mask. There are six frequency-pair cross-spectra.

## Results

| Cross-spectrum | D2 [uK^2] | D3 [uK^2] | q | n_cont | d=q R_CMB [Mpc] |
|---|---:|---:|---:|---:|---:|
| 100x70 | 138.848005 | 932.270434 | 0.17434152 | 2.52001191 | 2418.6399 |
| 100x94 | 122.575216 | 929.714756 | 0.16403194 | 2.60795130 | 2275.6152 |
| 143x100 | 136.977363 | 913.016594 | 0.17497944 | 2.51474267 | 2427.4898 |
| 143x70 | 138.163373 | 924.577677 | 0.17463316 | 2.51760053 | 2422.6859 |
| 143x94 | 122.050694 | 922.133780 | 0.16435205 | 2.60513866 | 2280.0560 |
| 94x70 | 124.125825 | 941.709238 | 0.16401162 | 2.60813006 | 2275.3332 |

Published mean cross-spectrum:

  D2 = 130.45674590166135 uK^2
  D3 = 927.23707991141737 uK^2

gives

  q_mean_spectrum = 0.16944932194983256,

  n_cont_mean_spectrum = 2.561074230987091,

  d_mean_spectrum = 2350.770443410027 Mpc
                  ~= 7.66718 Gly comoving.

Across the six cross-spectra,

  mean(n_cont) = 2.562262522784699,
  sample SD(n_cont) = 0.0491275946669983,
  min = 2.514742671253936,
  max = 2.608130062624722.

The cross-spectra are correlated, so this sample SD is a robustness diagnostic, not an independent statistical error bar.

## Dyadic verdict

No cross-spectrum yields an integer n.

The frozen exact integer/zero-offset subhypothesis therefore receives:

  INTEGER_DYADIC_ZERO_OFFSET = FAIL_AT_HELD_OUT_POINT_ESTIMATES.

No formal Gaussian sigma is assigned from the six-pair scatter because the cross-spectra are not independent and the freeze did not preregister a covariance-based acceptance threshold.

The continuous tetrahedral-translation scale inversion remains identified because every q lies strictly in (0,1):

  CONTINUOUS_TRANSLATION_SCALE_DOMAIN = PASS.

This PASS means only that the exact translation formula returns an admissible displacement. It is not validation of the physical tetrahedral CMB model.

## No half-step rescue

The values cluster near 2.5, but a half-integer shell lattice was NOT the frozen hypothesis.

Therefore this audit does not reinterpret the result as a hit at n=5/2.

Any half-step/spinorial scale law must:
1. be derived independently from pre-existing canon;
2. be versioned as a new candidate after this audit;
3. mark the 2026 ELC amplitudes as contaminated/exploratory;
4. use a new independent held-out dataset.

## Provenance

ELC files:
- ELC_Dl10070GHz_1%mask.txt
- ELC_Dl10094GHz_1%mask.txt
- ELC_Dl143100GHz_1%mask.txt
- ELC_Dl14370GHz_1%mask.txt
- ELC_Dl14394GHz_1%mask.txt
- ELC_Dl9470GHz_1%mask.txt
- ELC_mean_Dls.txt

Repository: hnofi/ELC_Paper2
Zenodo record: 10.5281/zenodo.20012802
