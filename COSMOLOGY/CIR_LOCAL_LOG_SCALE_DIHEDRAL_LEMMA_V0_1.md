# CIR Local Log-Scale Dihedral Lemma v0.1

Status: EXACT REPRESENTATION LEMMA / PHYSICAL BINDING OPEN
Date: 2026-09-26

## Inputs already present in the project

1. Canonical TIR normalization

   kappa = ln(2)/(24*pi),

   with one primitive full mixing block Phi_mix = 24*pi and dI = kappa dphi.

2. Mellin/log-scale coordinate for a positive multiplicative ratio D>0

   nu = ln D,

   with reciprocal inversion D -> 1/D acting as

   J(nu) = -nu.

3. Exact ARPL dyadic dilation

   D -> 2 D,

   which in log-scale is

   T(nu) = nu + ln 2.

## Lemma 1 — phase block equals one dyadic log-scale translation

For integer n define the unwrapped phase block

   Phi_n = 24*pi*n.

Then

   kappa Phi_n
   = [ln2/(24*pi)] [24*pi*n]
   = n ln2.

Hence the map

   F : Phi_n -> nu_n := kappa Phi_n

is exactly

   nu_n = n ln2 = ln(2^n).

Equivalently,

   exp(kappa Phi_n) = 2^n.

This is an exact identity in the declared representation. It is not yet a theorem that any physical length ratio equals exp(kappa Phi_n).

## Lemma 2 — reflection and dyadic translation generate D_infinity

Define

   J(nu) = -nu,
   T(nu) = nu + ln2.

Then

   J^2 = id,
   J T J = T^{-1}.

Therefore <J,T> is the standard infinite-dihedral action on the log-scale line.

## Corollary — every dyadic shell has a conjugate self-dual axis

Define the conjugated reflection

   J_n := T^n J T^{-n}.

Then

   J_n(nu) = 2 n ln2 - nu,

so its unique fixed point is

   nu_n = n ln2.

In multiplicative coordinates D=e^nu,

   D_n = 2^n.

Thus every dyadic shell is a translated copy of the same reciprocal self-dual geometry. The zero/fixed-axis structure is local to each shell rather than requiring one privileged global physical length.

## Phase form

Because nu_n = kappa Phi_n,

   J_n(nu) = 2 kappa Phi_n - nu.

A full 24*pi phase-block translation maps one self-dual shell to the next:

   Phi -> Phi + 24*pi
   <=>
   nu -> nu + ln2
   <=>
   D -> 2D.

## Physical-binding boundary

The exact representation lemma does NOT determine a dimensional physical scale. A physical domain S requires an independently derived local anchor L_{*,S}>0 and a source-backed identification

   D_S = L/L_{*,S}.

Only then does the representation imply candidate physical shells

   L_{n,S} = L_{*,S} 2^n.

The failed universal-Hubble-anchor population test shows that setting L_{*,S}=R_H for every black hole is not supported. It must not be rescued by changing q or a phase offset after inspection.

## Falsification consequence

Any future physical binding must derive L_{*,S} upstream from the relational domain (metric/source/boundary data) without using the target black-hole mass or radius. After freezing L_{*,S}, the shell residual is

   eta_S = log2(L/L_{*,S}) - round(log2(L/L_{*,S})).

The no-refit target is eta_S=0 (mod 1), with measurement uncertainty propagated before verdict assignment.
