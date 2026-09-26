# CIR C6-Regular ARPL Refinement Scale Theorem Candidate v0.1

Status: CONDITIONAL EXACT REPRESENTATION THEOREM / PHYSICAL IDENTIFICATION OPEN
Date: 2026-09-27

## 1. Exact upstream ingredients

### ARPL refinement

At a strict refinement step,

  L_{N+1}=b_N L_N,

with b_N positive integer child labels

  c in Z_{b_N}.

The exact ARPL ultrametric scales satisfy

  epsilon_{N+1}/epsilon_N = 1/b_N.

### C6 grading

The existing TIR supersymmetry/IDT crosswalk supplies a cyclic grading

  C6 = <G_6>,

with six eigensectors

  H_q, q in Z_6,

and generator action

  q -> q+1 mod 6

on the regular C6 label set.

The 48-dimensional carrier is

  H_ext ~= 8 C[C6],

so the six grades are all present with equal multiplicity.

## 2. Regular grading-refinement identification

Introduce the following bridge condition:

  REGULAR_C6_CHILD_BINDING:

1. one ARPL refinement fibre is identified with the C6 grade set;
2. every child carries exactly one grade q in Z_6;
3. the ARPL child shift c->c+1 is intertwined with the C6 generator q->q+1;
4. the action is free and transitive on child labels;
5. no grade is duplicated or omitted inside one refinement fibre.

Under these conditions the child set is a regular C6-set.

Every free transitive finite G-set has cardinality |G|. Therefore

  boxed[b_N = |C6| = 6].

This conclusion is exact once REGULAR_C6_CHILD_BINDING is admitted.

## 3. Scale consequence

The exact ARPL ultrametric refinement law then gives

  boxed[
  epsilon_{N+1}/epsilon_N = 1/6
  ].

Define the inward scale ratio

  q_C6 := 1/6.

Then after k identical regular-C6 refinement steps,

  epsilon_{N+k}
  = epsilon_N 6^{-k}.

This is a six-adic/hexadic refinement ladder, distinct from the previously tested dyadic 2^{-n} shell law.

## 4. Information increment

Because each parent splits into six equiprobable children,

  Delta H = ln 6.

Using the exact factorization

  6 = 3*2,

this increment decomposes additively as

  ln6 = ln3 + ln2,

matching the product structure

  C6 ~= C3 x Z2

at the level of cardinality/entropy.

This is an exact arithmetic compatibility. It does not by itself prove that the information functional, supersymmetry grading and physical radial scale are the same object.

## 5. Relation to the earlier kappa dyadic cell

The existing information normalization

  kappa = ln2/(24pi)

maps a full declared 24pi block to ln2.

The C6-regular ARPL refinement instead yields ln6 per six-child refinement.

These are different structures and must not be conflated.

In particular, this theorem does NOT replace

  T: nu -> nu+ln2

by a fundamental ln6 translation in the previously defined local-dihedral representation.

Rather, if both structures are physically admitted, a six-child refinement step contains

  ln6/ln2 = log2 6

dyadic-information units.

That value is generally non-integer.

## 6. Frozen candidate radial prediction

If a physical domain identifies one ARPL strict refinement with one radial parent-to-child scale transition, then the prospective candidate is

  boxed[q = 1/6].

With the already frozen CMB last-scattering screen anchor

  R_CMB = 13,873 Mpc,

the corresponding first inward shell is

  d_C6 = R_CMB/6
       = 2312.166666666667 Mpc.

This numerical prediction is fixed by the conditional bridge above and the existing screen anchor.

## 7. Provenance firewall

The bridge REGULAR_C6_CHILD_BINDING is NEW on 2026-09-27.

Therefore every CMB amplitude dataset inspected before this theorem is contaminated for its validation, including the 2026 ELC C2/C3 result.

ELC may be used only as a post-hoc diagnostic.

A new independent observable/dataset is required for prospective validation.

## 8. What is exact and what is open

EXACT:
- ARPL epsilon_{N+1}/epsilon_N=1/b_N;
- existence and order of the C6 grading in the cited TIR branch;
- free transitive C6 child action => b_N=6;
- conditional q=1/6;
- d=R_CMB/6 after the CMB-screen anchor is admitted.

OPEN:
- physical identification of ARPL refinement children with C6 grades;
- proof that one such refinement equals the radial parent-to-child transition relevant to the AoE;
- independent cosmological source/boundary realization;
- new held-out validation.

FORBIDDEN:
- citing pre-theorem ELC agreement as prospective confirmation;
- changing 6 to the value preferred by CMB amplitudes;
- identifying C6 group order with ARPL branching without the regular-action bridge.
