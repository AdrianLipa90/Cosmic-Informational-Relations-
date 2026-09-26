# CIR AoE Spin-2 PR3 EE Ancillary Diagnostic v0.1

Status: SECONDARY ANCILLARY DIAGNOSTIC / PRIMARY FROZEN Q-U MAP TEST STILL BLOCKED
Date: 2026-09-26

## Provenance class

The spin-2 tidal harmonic law and its power ladder were committed before the numerical EE values below were inspected.

However, the primary held-out product frozen in
schemas/CIR_AOE_SPIN2_TIDAL_CROSSCHANNEL_FREEZE_V0_2.json
is the Planck PR3 SMICA full-sky Q/U map. The ancillary unbinned EE spectrum used here was selected as an accessible fallback only after the binary map download failed.

Therefore this file is a SECONDARY DIAGNOSTIC, not a replacement for the frozen primary map test.

## Official source

Planck PR3 ancillary cosmology product:

  COM_PowerSpect_CMB-EE-full_R3.01.txt

NASA/IPAC IRSA / Planck PR3.

The file reports

  D_l = l(l+1) C_l^(EE) / (2*pi)

with symmetric quoted uncertainties.

Low-l entries:

  l=2: D2 = 0.11043700 +/- 0.0614751615
  l=3: D3 = 0.03783000 +/- 0.0396450884
  l=4: D4 = 0.01754611 +/- 0.0235603232
  l=5: D5 = 0.04533970 +/- 0.0162989593

## Spin-2 model conversion

The frozen model gives for total spin-2 harmonic power

  P_l
  = |A|^2 q^(2l)
    [4*pi/(2l+1)]
    N_l^2,

  N_l^2=(l+2)!/(l-2)!.

Since

  D_l
  proportional to
  l(l+1) P_l/(2l+1),

the first ratio obeys

  D3/D2
  = (250/49) q^2.

Hence

  q_E
  = sqrt[(49/250)(D3/D2)].

Using the published central values:

  q_E = 0.2591128231,

  n_E = -log2(q_E)
      = 1.9483476810.

The exact n=2 dyadic shell has

  q_2 = 1/4 = 0.25.

Central fractional offset:

  q_E/q_2 - 1
  = 0.03645129
  = 3.645 percent.

## Uncertainty warning

A first-order propagation treating D2 and D3 as independent gives

  sigma(ln q)
  ~= 0.5 sqrt[(sigma_D2/D2)^2+(sigma_D3/D3)^2]
  ~= 0.5933,

therefore

  sigma_q ~= 0.1537,

  sigma_n ~= 0.8560.

This independence/linearization approximation is NOT a formal Planck low-l likelihood evaluation. Correlations and the non-Gaussian behavior of ratios near zero must be handled with the official likelihood/covariance for any promoted verdict.

Thus the apparent proximity to n=2 is not statistically sharp.

## Higher-multipole central-value check

From q_E inferred only from l=2,3, the model predicts

  D4/D3
  = (245/81) q^2
  = 0.20307613,

while the observed central ratio is

  D4/D3
  = 0.46381470.

For the next step the model predicts

  D5/D4
  = (567/242) q^2
  = 0.15730608,

while the observed central ratio is

  D5/D4
  = 2.58403145.

Because D3 and D4 have uncertainties comparable to or larger than their central values, these raw ratio discrepancies are not assigned a sigma verdict here.

Parameter-free closure combinations are:

  K234_model
  := D4 D2 / D3^2
  = 0.5928395062,

  K234_obs
  = 1.3540127869,

and

  K345_model
  := (D5/D4)/(D3/D2)
  = 0.4592231405,

  K345_obs
  = 7.5435548727.

Again, these are diagnostic central values only until covariance-aware low-l likelihood evaluation is performed.

## Verdict

  CENTRAL_q_NEAR_1_OVER_4 = TRUE_NUMERICALLY
  DYADIC_n_EQUALS_2 = NOT_ESTABLISHED
  HIGHER_MULTIPOLE_CENTRAL_CLOSURE = POOR
  FORMAL_STATISTICAL_VERDICT = DATA_INSUFFICIENT_WITHOUT_LOW_L_COVARIANCE
  PRIMARY_Q_U_MAP_TEST = STILL_PENDING

No parameter was changed after reading the EE values.

## Epistemic note

The ~3.6 percent central proximity to q=1/4 is allowed to be reported because the dyadic base and zero offset were frozen before these EE values were opened. It must not be described as confirmation because the uncertainty is much larger than the offset and the next central-value ratios do not track the simple single-component ladder.
