# CIR AoE Interior-Tidal Planck-2013 Exploratory Diagnostic v0.1

Status: CONTAMINATED EXPLORATORY DIAGNOSTIC / NOT PROSPECTIVE EVIDENCE
Date: 2026-09-26

The Planck-2013 SMICA/NILC low-l coefficients used here were already inspected during the scalar Green-shadow v0.2 failure analysis. The tidal v0.3 model was formulated afterwards. Therefore none of the numerical proximity below can be counted as validation.

The sole purpose of this file is provenance: record what the already-seen data imply under the now-frozen v0.3 equations without hiding either favourable or unfavourable behaviour.

## Frozen transformation

From the previously recorded scalar-axis ratios

  r_23 = |g_3/g_2|,

the interior tidal model defines

  q = r_23/3,
  n_cont = log2(1/q),
  d_cont = q R_CMB,

with

  R_CMB = 13873 Mpc.

## Results

| Variant | r_23 | q=r_23/3 | n_cont | d_cont [Mpc] | Domain q<1 |
|---|---:|---:|---:|---:|---|
| SMICA raw | 1.5733929310 | 0.5244643103 | 0.9310834938 | 7275.8934 | PASS |
| SMICA de-boosted | 2.2093873357 | 0.7364624452 | 0.4413161357 | 10216.9435 | PASS |
| NILC raw | 1.3543497914 | 0.4514499305 | 1.1473621051 | 6262.9649 | PASS |
| NILC de-boosted | 1.8604751393 | 0.6201583798 | 0.6892913882 | 8603.4572 | PASS |

## Honest reading

1. The scalar-kernel fatal condition q>1 disappears under the physically different tidal operator. This means v0.3 is mathematically capable of representing the observed ordering |g_3|>|g_2|.

2. The two RAW component-separation variants bracket the first dyadic shell n=1:

   SMICA raw: n_cont ~= 0.931
   NILC raw:  n_cont ~= 1.147

   but this is post-model-design contaminated and is NOT evidence for n=1.

3. The de-boosted variants shift materially:

   SMICA de-boosted: n_cont ~= 0.441
   NILC de-boosted:  n_cont ~= 0.689.

   Therefore the exploratory set is not robust enough to promote an integer shell.

4. The correct next test is genuinely independent low-l extraction from a dataset not used in model construction, with the boost/mask policy fixed before coefficient inspection.

## Exploratory verdict

  TIDAL_MODEL_DOMAIN_CONDITION = SURVIVES_ON_SEEN_DATA
  DYADIC_INTEGER_LOCK = NOT_ESTABLISHED
  ROBUSTNESS_TO_DEBOOSTING = TENSION
  PROSPECTIVE_EVIDENCE = NONE

No parameter is changed in response to these results.
