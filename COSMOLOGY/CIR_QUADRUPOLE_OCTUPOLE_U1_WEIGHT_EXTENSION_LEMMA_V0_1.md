# CIR Quadrupole-to-Octupole U(1) Weight-Extension Lemma v0.1

Status: EXACT REPRESENTATION LEMMA / TIR-LABEL CROSSWALK CANDIDATE
Date: 2026-09-26

## 1. SO(3) harmonic carriers

Let H_l be the complex irreducible SO(3) carrier of angular momentum l.

Its dimension is

  dim H_l = 2l+1.

After choosing a common physical axis a, restrict SO(3) to the axial subgroup U(1)_a. Then

  H_l |_{U(1)}
  = direct_sum_{m=-l}^{l} C_m,

where C_m is the one-dimensional weight-m carrier.

## 2. Adjacent-l extension

For every l>=0,

  H_{l+1}|_{U(1)}
  = H_l|_{U(1)}
    direct_sum C_{+(l+1)}
    direct_sum C_{-(l+1)}.

Hence

  dim H_{l+1} - dim H_l = 2.

For the CMB quadrupole and octupole,

  dim H_2 = 5,
  dim H_3 = 7,

and

  H_3|_{U(1)}
  = H_2|_{U(1)}
    direct_sum C_{+3}
    direct_sum C_{-3}.

The two added weights are precisely the extremal planar octupole modes m=+/-3.

This is an exact U(1)-restricted representation identity. It is not an SO(3)-equivariant decomposition H_3 = H_2 + 2 because H_2 and H_3 are inequivalent SO(3) irreps.

## 3. D3 refinement of the edge pair

Under the C3 rotation

  phi -> phi + 2*pi/3,

the edge weights satisfy

  exp(+/- i 3*2*pi/3)=1.

A reflection exchanges m=+3 and m=-3.

Therefore the two-dimensional edge space

  E_edge = span{C_{+3},C_{-3}}

splits into the real one-dimensional D3 sectors

  A1 ~ cos(3 phi),
  A2 ~ sin(3 phi).

Thus the exact new degrees of freedom appearing when moving from l=2 to l=3 are also exactly the pair from which the D3 one-dimensional planar octupole sectors are built.

## 4. TIR structural-label arithmetic crosswalk

Canonical TIR v12 structural labels include

  L3 = 7,
  L4 = 2,
  L5 = 5.

Therefore

  L3 = dim H_3,
  L5 = dim H_2,
  L4 = dim H_3 - dim H_2,

and

  L3 = L5 + L4
     = 5 + 2
     = 7.

This is an exact arithmetic crosswalk between existing TIR labels and the low-l harmonic carrier dimensions.

## 5. SUSY-like pairing interpretation — representation level only

Define a frame-restricted pairing map Q on the shared U(1) weights by

  Q: |2,m> -> |3,m>,  m=-2,-1,0,1,2.

The octupole edge states |3,+3>, |3,-3> are unpaired.

Hence the paired core has dimension five and the unpaired edge has dimension two.

This resembles a supersymmetric/index-type paired-plus-unpaired structure, but no physical supersymmetry algebra is claimed unless nilpotent supercharges, Hamiltonian closure and the physical state space are independently derived.

## 6. Physical-binding firewall

The exact identities above do NOT imply:

- that TIR L3/L4/L5 physically generate the CMB multipoles;
- that the two unpaired edge states cause the Axis of Evil;
- that the dyadic shell index n equals L4=2;
- that a Witten index has been physically established.

Those are separate bridge claims.

## 7. Relevance to the corrected AoE geometry

Unlike the retired m=0 model, this crosswalk singles out the correct planar/high-|m| octupole edge pair.

A viable physical model may now be organized as

  paired quadrupole/octupole core
  + unpaired planar octupole edge
  + D3 reflection split A1/A2
  + radial transfer K_l(q).

The remaining scale problem is entirely in K_l(q) and its boundary normalization, not in the angular carrier count.
