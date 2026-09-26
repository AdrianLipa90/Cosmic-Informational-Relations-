# CIR C6-Regular ARPL Planck-PR3 Held-Out Audit v0.1

Status: HELD-OUT / NON-DECISIVE
Date: 2026-09-27

## Freeze precedence

Before opening the Planck PR3 low-l TT values, the branch had already frozen the conditional C6-regular ARPL prediction

  q_pred = 1/6,

with the CMB-screen anchor

  R_CMB = 13,873 Mpc,

so

  d_pred = 2312.1666666666665 Mpc.

The tetrahedral translation data-side estimator was already fixed as

  q_data = (1/7) sqrt(10 D2/D3),

where

  D_l = l(l+1) C_l/(2 pi).

No parameter was changed after opening PR3.

## Held-out source

Official Planck Public Release 3 TT full spectrum:

  COM_PowerSpect_CMB-TT-full_R3.01.txt

IRSA / Planck PR3.

Published low-l entries:

  l=2:
    D2 = 225.895 uK^2
    -dD2 = 132.369
    +dD2 = 533.062

  l=3:
    D3 = 936.920 uK^2
    -dD3 = 450.471
    +dD3 = 1212.308

## Central-value result

  q_PR3
  = (1/7) sqrt(10*225.895/936.920)
  = 0.22182169230576443.

Therefore

  n_cont = -log2(q_PR3)
         = 2.172527638983372,

and

  d_PR3 = q_PR3 R_CMB
        = 3077.33233735787 Mpc.

Relative to q_pred=1/6,

  (q_PR3-q_pred)/q_pred
  = 0.3309301538345866,

i.e. the PR3 central value is 33.09% above the frozen C6 prediction.

## Conservative interval diagnostic

A deliberately conservative endpoint propagation using the published asymmetric low-l intervals gives

  D2_low  = 93.526,
  D2_high = 758.957,

  D3_low  = 486.449,
  D3_high = 2149.228.

Since q increases with D2 and decreases with D3,

  q_low  = (1/7) sqrt(10 D2_low/D3_high)
         = 0.09423818112303212,

  q_high = (1/7) sqrt(10 D2_high/D3_low)
         = 0.5642764013227791.

The frozen value

  q_pred = 1/6 = 0.16666666666666666

lies inside this broad interval.

This endpoint interval is not a formal posterior for q because the published D2/D3 intervals need not be independent and their joint covariance is not encoded in the text table.

## Verdict

  CENTRAL_VALUE_MATCH = NO

  q=1/6 EXCLUDED_BY_PUBLISHED_LOW-L_INTERVALS = NO

  PROSPECTIVE_VERDICT = NON_DECISIVE

The held-out PR3 result neither validates nor rejects the conditional C6-regular ARPL scale prediction.

No retuning is permitted.
