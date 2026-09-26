# CIR AoE Tidal Scale-Selector Closure v0.1

Status: CONDITIONAL EXACT SELECTOR CLOSURE / EMPIRICAL VALIDATION OPEN
Date: 2026-09-26

## 1. Problem closed by this note

Earlier local-scale work required two independent objects:

  L_star(S),
  n(S->X).

For the specific CMB-screen / interior-tidal-shadow branch, both can now be supplied upstream of any astronomical target catalogue.

The screen supplies the dimensional anchor:

  L_star = R_CMB.

The low-l tidal ratio supplies the continuous shell selector:

  n_cont = log2(3/r_23),

where

  r_23 = |g_3/g_2|.

No target black-hole mass, radius, redshift or sky position appears.

## 2. Exact conditional chain

Interior Green geometry:

  q = d/R_CMB,
  0<q<1.

Axis-contracted tidal Hessian:

  t_l proportional to l(l-1) q^(l-2).

Therefore

  r_23 = |t_3/t_2| = 3q.

Hence

  q = r_23/3,

and the dimensional centre displacement is

  d_cont = R_CMB r_23/3.

The dyadic phase/log-scale law gives

  q = 2^{-n}
    = exp(-n ln2)
    = exp[-kappa_I (24*pi*n)],

with

  kappa_I = ln2/(24*pi).

Therefore

  r_23 = 3 exp[-kappa_I Phi_n],

  Phi_n = 24*pi*n,

and the continuous winding estimator is

  n_cont
  = -log2 q
  = log2(3/r_23)
  = Phi_cont/(24*pi).

Equivalently,

  Phi_cont = (24*pi/ln2) ln(3/r_23).

## 3. Integer closure test

The dyadic sub-hypothesis is not enforced by rounding. It predicts

  n_cont in positive integers

within propagated uncertainty.

For a candidate integer n,

  r_23(pred;n) = 3*2^{-n},
  d_pred(n) = R_CMB*2^{-n}.

The first shells are therefore fixed before any target search:

  n=1: r_23=1.5,   d=R_CMB/2
  n=2: r_23=0.75,  d=R_CMB/4
  n=3: r_23=0.375, d=R_CMB/8
  n=4: r_23=0.1875,d=R_CMB/16

and so on.

## 4. Direction and full 3D prediction

Let a be the frozen unoriented AoE axis. After the CMB low-l test selects q, the candidate centre is restricted to the antipodal pair

  x_c = +/- d_cont a.

If integer dyadic closure is supported,

  x_c(n) = +/- R_CMB 2^{-n} a.

The sign ambiguity is not broken by this model and must remain explicit until an independent odd-parity/directional observable resolves it.

## 5. Uncertainty propagation

Let

  X=g_2,
  Y=g_3,
  r=|Y/X|.

Away from X=0 and Y=0,

  Var(ln r)
  ~= Var(Y)/Y^2 + Var(X)/X^2 - 2 Cov(X,Y)/(XY).

Thus

  sigma_n ~= sigma_ln_r/ln2.

For the continuous radial estimate

  d=R_CMB*r/3,

if the screen-radius estimate is treated independently from the low-l map extraction,

  (sigma_d/d)^2
  ~= (sigma_R/R_CMB)^2 + Var(ln r).

A production analysis must replace this linear approximation with the frozen map/mask simulation covariance when required.

## 6. Held-out target embargo

Once a new independent CMB map yields a frozen posterior for

  a, q, n_cont, d_cont,

the following quantities become predictions BEFORE target-catalog inspection:

- two antipodal sky directions;
- radial comoving distance d_cont;
- if dyadic closure passes, discrete radial shell d_n;
- higher-multipole tidal ratios r_34 and r_45.

Only after that freeze may a catalogue of massive structures, black holes, lensing centres or other source candidates be opened.

## 7. Evidential status

EXACT CONDITIONAL:
- r_23=3q for the declared interior tidal Green model;
- n_cont=log2(3/r_23);
- d_cont=R_CMB*r_23/3;
- phase relation Phi_cont=24*pi*n_cont.

EXTERNAL FROZEN ANCHOR:
- R_CMB from Planck last-scattering transverse comoving distance.

OPEN EMPIRICAL:
- independent PR3/PR4/NPIPE/WMAP low-l coefficient extraction;
- integer consistency of n_cont;
- higher-l held-out ratios;
- astronomical target comparison.

FORBIDDEN:
- selecting n from a target catalogue;
- changing the AoE axis after opening new coefficients;
- choosing a source because it is close to one of the predicted shells and then calling the shell predicted.
