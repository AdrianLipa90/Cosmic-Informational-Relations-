# CIR Kerr-Axis / Tetrahedral Vertex Stabilizer Bridge v0.1

Status: EXACT GROUP-THEORY BRIDGE / PHYSICAL AXIS BINDING CANDIDATE
Date: 2026-09-26

## 1. Canonical tetrahedral symmetry

Let the proper rotational symmetry group of the regular tetrahedron be

  T ~= A4.

Let the full orthogonal tetrahedral symmetry group, including reflections, be

  T_d ~= S4.

Choose one tetrahedral vertex v.

## 2. Exact stabilizers

The subgroup of proper tetrahedral rotations that fixes v is the threefold rotation group about the vertex/opposite-face axis:

  boxed[
  Stab_A4(v) ~= C3.
  ]

The subgroup of the full tetrahedral group that fixes v may additionally permute/reflect the three vertices of the opposite face:

  boxed[
  Stab_Td(v) ~= S3 ~= D3.
  ]

Thus selecting one tetrahedral vertex reduces

  A4 -> C3

in the oriented/proper sector, or

  Td -> D3

when parity-reflected face operations are admitted.

## 3. Kerr source axis as the vertex selector

A Kerr source supplies an oriented spin axis

  s_Kerr = J/|J|,

with handedness fixed by sign(a) or equivalently sign(Omega_H).

The candidate source binding is

  boxed[
  s_Kerr <-> selected tetrahedral vertex axis v.
  ]

Once this binding is declared upstream, the tetrahedral vertex is not chosen from CMB data.

The residual exact angular grammar is then C3 around the Kerr spin axis.

## 4. Chirality

Frame dragging distinguishes

  +Omega_H

from

  -Omega_H.

Therefore the oriented source naturally distinguishes the two generators

  C3: phi -> phi + 2pi/3

and

  C3^{-1}: phi -> phi - 2pi/3.

This provides a source-owned chirality bit.

A parity-insensitive observable may lose this handedness and exhibit only the unoriented D3 grammar. The enlargement from oriented C3 to effective D3 is a physical-observable statement and is not claimed from group theory alone.

## 5. Connection to the low-l carrier

In the common-axis spherical-harmonic frame,

  C3: Y_lm -> exp(i 2pi m/3) Y_lm.

Hence:
- the l=3 edge modes m=+/-3 lie in the C3-trivial rotational sector;
- reflection-even/odd real combinations split as A1/A2 under D3;
- the l=2 planar pair m=+/-2 forms an E-type D3 sector.

These are exactly the sectors already isolated in the earlier CIR D3/Weyl(A2) crosswalk.

## 6. What this solves

The bridge supplies a non-CMB mechanism for selecting:

- one tetrahedral vertex;
- the physical axis about which C3 acts;
- an oriented chirality sign from Kerr rotation.

It therefore removes the need to choose a tetrahedral vertex or handedness after inspecting the AoE map, PROVIDED the Kerr parent axis is itself independently sourced.

## 7. What remains open

The bridge does not yet derive:

- the actual sky orientation of s_Kerr for a cosmological parent;
- observer inclination i;
- the critical-curve -> CMB transfer operator;
- the strength of each C3/D3 harmonic sector;
- the physical identification of the cosmological parent with Kerr.

## 8. Firewall

Forbidden:
- rotate the tetrahedron to maximize AoE agreement and then call the selected vertex a Kerr prediction;
- choose sign(Omega_H) from the observed CMB chirality and count the same data as validation;
- infer D3 physical binding from the abstract group isomorphism alone.

Required:
- source-owned spin-axis packet first;
- then fixed tetrahedral vertex binding;
- then forward harmonic prediction;
- only afterward CMB evaluation.
