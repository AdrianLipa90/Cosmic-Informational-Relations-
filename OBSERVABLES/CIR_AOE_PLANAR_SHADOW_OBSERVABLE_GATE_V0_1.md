# CIR AoE Planar-Shadow Observable Gate v0.1

Status: OBSERVABLE INTERFACE / PHYSICAL MODEL OPEN
Date: 2026-09-26

## 1. Axis convention

Let a be a frozen preferred direction defined by maximizing angular-momentum dispersion. Rotate the CMB harmonic coefficients into the frame where a is +z:

  a_{lm} -> a_{lm}^{(a)}.

All future AoE-shadow models must use this same convention.

## 2. Primary orientation statistic

For each l,

  M_l(a)
  = [sum_{m=-l}^{l} m^2 |a_{lm}^{(a)}|^2]
    / [sum_{m=-l}^{l} |a_{lm}^{(a)}|^2].

The AoE orientation problem is a maximization of M_l, individually or jointly for l=2,3.

## 3. Planarity interface

Define

  A_l^planar
  := sqrt(|a_{l,l}^{(a)}|^2 + |a_{l,-l}^{(a)}|^2),

and

  f_l^planar
  := (A_l^planar)^2
     / sum_m |a_{lm}^{(a)}|^2.

For a real temperature map,

  |a_{l,-l}|=|a_{l,l}|,

but the symmetric definition is kept explicitly.

## 4. Cross-multipole scale datum

The data-side amplitude ratio is

  rho_23^planar := A_3^planar/A_2^planar.

This is NOT by itself a scale.

A physical operator O must derive a spectral response F_l(O) such that, for a declared local scale coordinate q,

  A_l^planar = A0 F_l(O) q^{p_l}

with p_l fixed by the model.

Only then may q be inferred from rho_23^planar.

Forbidden:

- reusing the retired m=0 ratio;
- selecting F_l after seeing rho_23;
- moving the AoE axis to improve the scale fit;
- using a target black-hole mass/location to choose the shell index.

## 5. Morphology discriminator

A candidate shadow model must predict at minimum:

  f_2^planar,
  f_3^planar,
  M_2(a),
  M_3(a),
  rho_23^planar.

If it is axisymmetric/zonal in the frame a, then

  f_l^planar = 0 for l>0

and

  M_l(a)=0,

so it cannot represent an AoE axis defined by maximum angular-momentum dispersion.

## 6. Held-out continuation

Once a physical F_l and q estimator are frozen using l=2,3, the model must predict at least one of:

  A_4^planar/A_3^planar,
  A_5^planar/A_4^planar,
  f_4^planar,
  f_5^planar,

without further parameter changes.

## 7. Scale-algebra connection

The exact local log-scale result remains available:

  nu = ln(L/L_star),
  T: nu -> nu + ln2.

But the physical map from the planar harmonic observable to nu is OPEN.

The next theorem must derive that map; it cannot be assumed from the old m=0 Green kernel.
