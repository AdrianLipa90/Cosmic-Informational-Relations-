# CIR AoE Green-Shadow ALM Inversion Lemma v0.1

Status: EXACT HARMONIC NORMALIZATION LEMMA / PHYSICAL MODEL CANDIDATE
Date: 2026-09-26

## Setup

Fix an unoriented sky axis a and rotate coordinates so that a is the +z axis. Let the real temperature field have spherical-harmonic coefficients a_{ell m}^{(a)} in this rotated frame.

The azimuthal average around the fixed axis is

  Tbar(mu) = (1/2pi) integral_0^{2pi} T(mu,phi) dphi,

with mu=cos(theta).

Only m=0 survives azimuthal averaging, so

  Tbar(mu)
  = sum_ell a_{ell 0}^{(a)} Y_{ell 0}(theta)
  = sum_ell a_{ell 0}^{(a)} sqrt[(2ell+1)/(4pi)] P_ell(mu).

If the Legendre coefficients are defined by

  Tbar(mu) = sum_ell g_ell P_ell(mu),

then exactly

  g_ell = sqrt[(2ell+1)/(4pi)] a_{ell 0}^{(a)}.

## Quadrupole/octupole inversion

For the linear Green-shadow model

  g_ell = A q^ell,

with 0<q<1. Therefore

  q = |g_3/g_2|
    = sqrt(7/5) |a_{30}^{(a)}/a_{20}^{(a)}|,

provided a_{20}^{(a)} != 0.

The absolute value makes q invariant under reversal of the unoriented axis because

  a_{ell 0}^{(-a)} = (-1)^ell a_{ell 0}^{(a)}.

Hence the ratio changes sign but |q| does not.

## Dyadic index

For the candidate shell law q=2^{-n},

  n_cont = -log_2 q
         = -log_2[ sqrt(7/5) |a_{30}^{(a)}/a_{20}^{(a)}| ].

This quantity is computable from the CMB low-l field alone, before any black-hole/source catalog is opened.

## Local uncertainty propagation

Away from a_{20}=0 and a_{30}=0, let X=a_{20}^{(a)} and Y=a_{30}^{(a)}. Then

  ln q = const + ln|Y| - ln|X|.

For covariance matrix entries Var(X), Var(Y), Cov(X,Y),

  Var(ln q)
  ~= Var(Y)/Y^2 + Var(X)/X^2 - 2 Cov(X,Y)/(XY).

Thus

  sigma_n ~= sigma_{ln q}/ln 2.

The final analysis must use map/mask simulations or an equivalent full covariance treatment when the Gaussian linear approximation is inadequate.

## Cross-multipole prediction

Once q is inferred from ell=2,3, the same Green kernel makes held-out harmonic predictions

  g_4/g_3 = q,
  g_5/g_4 = q,
  ...

or equivalently

  a_{(ell+1)0}^{(a)} / a_{ell 0}^{(a)}
  = q sqrt[(2ell+1)/(2ell+3)]

up to the sign convention fixed by the oriented representative of a.

These higher-ell ratios are not needed to infer q and can therefore be held out as a prospective validation layer.

## Epistemic boundary

EXACT:
- m=0 survival under azimuthal averaging;
- g_ell = sqrt[(2ell+1)/(4pi)] a_{ell0}^{(a)};
- the algebraic q formula conditional on g_ell=A q^ell.

CANDIDATE:
- the AoE contains a Green-shadow component whose coefficients follow A q^ell;
- q is dyadic.

OPEN:
- the physical parent/source geometry;
- the observation-sphere anchor R_S;
- the reciprocal radial branch.
