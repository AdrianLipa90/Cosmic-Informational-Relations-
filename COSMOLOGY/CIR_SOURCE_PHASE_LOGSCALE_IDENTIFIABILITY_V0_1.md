# CIR Source–Phase–Log-Scale Identifiability v0.1

Status: CONDITIONAL EXACT BRIDGE / IDENTIFIABILITY FIREWALL / PHYSICAL COSMOLOGICAL BINDING OPEN  
Date: 2026-10-04

## 1. Scope

This note separates three objects that must not be collapsed:

1. the exact CIR log-scale representation,
2. the QHTRI dynamical phase law,
3. the GREMLIN/RFC source-density carrier.

The objective is to determine exactly what follows when they are connected, and exactly which physical bindings are still missing.

No value of (H_0), no cosmological distance datum, and no target redshift is used to fix any coefficient in this note.

## 2. Exact CIR log-scale identity

Let (D(t)>0) be a declared dimensionless multiplicative scale coordinate and define

[

u_D(t):=ln D(t).
]

On the CIR representation branch, let

[

u_D=kappaPhi_D,
qquad
kappa=rac{ln 2}{24pi}.
]

Then

[
D=e^{kappaPhi_D}.
]

For differentiable (D,Phi_D),

[
oxed{
H_D
:=rac{dln D}{dt}
=rac{dot D}{D}
=kappadotPhi_D.
}
]

This is an exact differential identity on the declared representation.

### Firewall

(H_D) is a relational log-scale rate. It is **not** automatically the FLRW Hubble parameter.

The further identification

[
H_D=H_{m FLRW}=dot a/a
]

requires an independent physical map such as (D=a/a_star), or another declared observable/metric binding. The present CIR repository does not yet close that gate.

## 3. Phase-type firewall

QHTRI supplies a phase-mechanics law

[
dotPhi_Q=-rac{U}{eta_phi}.
]

The scale phase (Phi_D) and the QHTRI phase (Phi_Q) are provenance-distinct until a transfer map is supplied.

The minimal affine phase-transfer candidate is

[
oxed{
Phi_D=lambda_PhiPhi_Q+Phi_0
}
]

with dimensionless (lambda_Phi), fixed independently of cosmological target data.

If (lambda_Phi) and (Phi_0) are constant, then

[
oxed{
H_D
=-rac{kappalambda_Phi}{eta_phi}U.
}
]

The special case (lambda_Phi=1) is admissible only after an exact same-phase registry is proven. It must not be assumed by symbol reuse.

## 4. GREMLIN/RFC source-density carrier

The GREMLIN RFC source-density branch defines

[
Q
:=rac{Bomegamathcal N}{AR},
qquad
AR=A,R,
]

and

[
ho_E
=
Q(	ildephi+kappa).
]

The parent typing is

[
V_R:=AR,
qquad
n_R:=rac{mathcal N}{AR},
qquad
epsilon_Psi:=Bomega(	ildephi+kappa),
qquad
ho_E=n_Repsilon_Psi.
]

Therefore (Q) is a source-density prefactor. It is not a dimensionless radial coordinate.

### Dimensional firewall for the hyperbolic-disk candidate

A Poincare-disk coordinate of the form

[
z=	anh(chi/2)e^{i	heta}
]

requires dimensionless (chi).

Accordingly the raw assignment

[
chi=Q=rac{Bomegamathcal N}{AR}
]

is not dimensionally closed on the current typed source branch.

An admissible form is instead

[
oxed{
hatchi:=rac{Q}{Q_star},
qquad
z=	anh(hatchi/2)e^{i	heta},
}
]

where (Q_star>0) is an independently derived source-density scale. (Q_star) may not be fitted to (H_0) or chosen after inspecting the target cosmological observable.

## 5. Carrier identifiability theorem

Assume (B,omega,mathcal N,A,R>0), and assume an observable depends on these five source variables only through

[
Q=rac{Bomegamathcal N}{AR}.
]

Define logarithmic coordinates

[
x=
(ln B,lnomega,lnmathcal N,ln A,ln R)^T.
]

Then

[
ln Q
=
c^T x,
qquad
c=(1,1,1,-1,-1)^T.
]

Hence

[

abla_xln Q=c,
]

so the source-to-carrier Jacobian has rank one.

Therefore its nullspace has dimension four:

[
oxed{
operatorname{rank}J_Q=1,
qquad
dimker J_Q=4.
}
]

Equivalently, for any (vinmathbb R^5) satisfying

[
v_B+v_omega+v_N-v_A-v_R=0,
]

the transformation

[
(B,omega,mathcal N,A,R)
mapsto
(e^{v_B}B,e^{v_omega}omega,e^{v_N}mathcal N,e^{v_A}A,e^{v_R}R)
]

leaves (Q) invariant.

### Consequence

No collection of observables of the form

[
y_i=F_i(Q)
]

can locally identify the five factors separately without additional independent source constraints.

If

[
dotPhi_D=mathcal F(Q)
]

or

[
H_D=mathcal H(Q),
]

the same four-dimensional carrier degeneracy remains.

This extends the GREMLIN v0.8 source/coupling identifiability principle from the two-factor orbital invariant

[
K_{m orb}=mu_{m source}eta_G
]

to the five-factor RFC source-density carrier.

## 6. Density-to-phase bridge: two distinct physical branches

The QHTRI law uses a potential energy (U), whereas GREMLIN/RFC supplies an energy-density-like source (ho_E). They cannot be equated without a volume/kernel map.

Introduce an independently sourced effective support volume (V_{m eff}) and a dimensionless response functional (mathcal C):

[
U_{m eff}
=
V_{m eff},ho_E,mathcal C.
]

Then the conditional bridge is

[
oxed{
H_D
=
-rac{kappalambda_Phi}{eta_phi}
V_{m eff}
rac{Bomegamathcal N}{AR}
(	ildephi+kappa)
mathcal C.
}
]

All factors outside the exact CIR identity remain typed physical bindings.

### Cell-integrated special case

If, and only if, the QHTRI potential is identified with the energy of exactly the same RFC relational cell,

[
V_{m eff}=V_R=AR,
qquad
mathcal C=1,
]

then

[
U_{m cell}
=
ho_E AR
=
Bomegamathcal N(	ildephi+kappa),
]

and therefore

[
oxed{
H_D
=
-rac{kappalambda_Phi}{eta_phi}
Bomegamathcal N(	ildephi+kappa).
}
]

The factor (AR) cancels.

This is important: (Bomegamathcal N/(AR)) controls the **local density** branch, but an integrated same-cell phase-energy branch need not retain (AR).

Therefore the statement “(Bomega N/AR) directly drives the cosmic log-scale rate” is not yet justified. The answer depends on whether the phase responds to a local density, an integrated cell energy, or another nonlocal/source kernel.

## 7. Minimal source-to-scale architecture

The current admissible architecture is

[
(B,omega,mathcal N,A,R,	ildephi)
	o
ho_E
	o
U_{m eff}
	o
Phi_Q
	o
Phi_D
	o

u_D=ln D.
]

In differential form,

[
oxed{
H_D
=
kappadotPhi_D
=
-rac{kappalambda_Phi}{eta_phi}U_{m eff}.
}
]

The unresolved physical content is concentrated in

[
(ho_E,	ext{geometry},	ext{holonomy},	ext{orbit})
longrightarrow
U_{m eff},
]

and in the phase-transfer coefficient/map between (Phi_Q) and (Phi_D).

## 8. No-(H_0)-fit rule

Any dimensionful rate emerging from this bridge must be fixed upstream from source dynamics.

A generic normalized form may be written

[
H_D
=
kappa,Omega_star
f(hatchi,mathcal H,mathcal O,ldots),
]

but both (Omega_star) and the source-density normalizer (Q_star) must be derived from independently specified source/geometry/QHTRI quantities.

Forbidden:

- fitting (Omega_star) to (H_0);
- choosing (Q_star) to reproduce a desired redshift;
- identifying (D) with the FLRW scale factor after inspecting cosmological targets;
- identifying (Phi_D,Phi_Q,	ildephi) merely because all are written as phases.

## 9. Falsifiable next gates

The next work should close these in order:

1. **PHASE_REGISTRY_GATE**  
   Derive the typed map (Phi_Q	oPhi_D), including whether (lambda_Phi=1).

2. **DENSITY_TO_POTENTIAL_GATE**  
   Decide and derive whether (U_{m eff}) is local-density, same-cell integrated energy, or a nonlocal geometric functional.

3. **SOURCE_NORMALIZATION_GATE**  
   Derive (Q_star), (V_{m eff}), and any response coefficient without cosmological target fitting.

4. **METRIC/OBSERVABLE_GATE**  
   Bind the dimensionless (D) to a metric or directly observable cosmological scale variable.

5. **PROSPECTIVE_TEST_GATE**  
   Freeze a no-refit prediction for redshift/distance/time-dilation/BAO or another observable only after gates 1–4 close.

## 10. Epistemic verdict

### EXACT / CONDITIONAL EXACT

- (H_D=dln D/dt=kappadotPhi_D) on the declared CIR representation;
- raw RFC carrier (Q=Bomegamathcal N/(AR)) is a source-density prefactor;
- (Q)-only observation has rank-one source Jacobian and a four-dimensional multiplicative degeneracy;
- (AR) cancels from same-cell integrated energy (ho_E V_R) when (V_R=AR).

### OPEN PHYSICAL BINDING

- (Phi_QleftrightarrowPhi_D);
- (ho_E	o U_{m eff});
- the dimensionless radial normalization (Q_star);
- (Dleftrightarrow) cosmological metric/observable;
- identification of (H_D) with any measured Hubble-like rate.

### FORBIDDEN PROMOTIONS

- (Q=H);
- (Q) used directly as the argument of (	anh) without normalization;
- same symbol (Phi) used as proof of cross-project phase identity;
- fitting any bridge coefficient to (H_0) and calling the result a derivation.

## 11. Parent provenance

- CIR base: `cbe7cb292d6f164b656ba38a051b7914c40fbad2`.
- TIR parent currently pinned by CIR: `853032e019824b836de43634d949da5566396153`.
- GREMLIN main used for the source-density and identifiability crosswalk: `b0000828238e0cd244f5eb1fb679155315df372f`.
- GREMLIN source specs:
  - `spec/GREMLIN_SEMANTIC_ORBITAL_RFC_SOURCE_DENSITY_V0_4.md`;
  - `spec/GREMLIN_ORBIT_SOURCE_COUPLING_IDENTIFIABILITY_V0_8.md`.
- QHTRI phase-mechanics equation is taken from the project monograph ledger reporting QHTRI baseline `d8e07571ef8132bfa1069cff27c9cca8b191853a`.

No parent source is promoted beyond its own declared authority.
