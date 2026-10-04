# CIR Phase Registry Gate v0.1

Status: EXACT U(1) REGISTRY CLASSIFICATION / SAME-PHASE PHYSICAL IDENTITY CONDITIONAL  
Date: 2026-10-04

## 1. Purpose

CIR uses an unwrapped scale phase (Phi_D) through

[

u_D=ln D=kappaPhi_D,
qquad
kappa=rac{ln2}{24pi}.
]

QHTRI uses a dynamical action phase (Phi_Q) through

[
Phi_Q=rac{S_Q}{eta_phi},
qquad
dotPhi_Q=-rac{E_Q}{eta_phi},
]

where (E_Q) denotes the energy coordinate admitted to the carrier action.

The symbols (Phi_D) and (Phi_Q) are not identified by notation. This gate classifies the admissible registry maps before any cosmological observable is used.

## 2. Lifted phases and the U(1) registry

Let

[
u_Q=e^{iPhi_Q},
qquad
u_D=e^{iPhi_D}
]

be the corresponding wrapped U(1) phases.

Require the physical registry to preserve phase composition:

[
f(u_1u_2)=f(u_1)f(u_2),
]

and require (f:U(1)	o U(1)) to be continuous.

Every continuous group homomorphism of U(1) is of the form

[
oxed{
f(e^{iphi})=e^{imphi},
qquad
minmathbb Z.
}
]

Thus the arbitrary continuous affine slope of the earlier candidate is quantized once a genuine U(1) registry is demanded.

On a fixed lifted branch one may write

[
oxed{
Phi_D
=
mPhi_Q+Phi_0+2pi k,
}
]

where (minmathbb Z), (Phi_0) is a fixed coordinate-origin offset and (kinmathbb Z) is a fixed lift choice on the differentiable segment.

Therefore

[
oxed{
dotPhi_D=mdotPhi_Q.
}
]

The fixed offsets do not affect rates.

## 3. Isomorphism and orientation gates

If the registry is required to be an isomorphism rather than a many-to-one covering map, then

[
oxed{|m|=1.}
]

Hence

[
m=+1
]

for an orientation-preserving registry, and

[
m=-1
]

for an orientation-reversing registry.

Therefore the strongest no-fit same-orientation branch is

[
oxed{
dotPhi_D=dotPhi_Q.
}
]

This result is conditional on the registry axioms. It is not evidence that the CIR scale phase and QHTRI carrier phase are physically the same degree of freedom.

## 4. Log-scale rate consequence

The exact CIR identity gives

[
H_D:=rac{dln D}{dt}=kappadotPhi_D.
]

Combining with the registry classification,

[
oxed{
H_D
=
kappa mdotPhi_Q.
}
]

If the QHTRI carrier phase consumes an admitted extensive energy (E_Q),

[
dotPhi_Q=-rac{E_Q}{eta_phi},
]

then

[
oxed{
H_D
=
-rac{kappa m}{eta_phi}E_Q.
}
]

For the orientation-preserving U(1) isomorphism,

[
oxed{
H_D
=
-rac{kappa}{eta_phi}E_Q.
}
]

No Hubble datum enters this derivation.

## 5. Dyadic block consequence

CIR has the exact representation step

[
DeltaPhi_D=24pi
quadLongrightarrowquad
Delta
u_D=ln2
quadLongrightarrowquad
Dmapsto2D.
]

Under degree (m
eq0),

[
DeltaPhi_Q=rac{24pi}{m}.
]

For the orientation-preserving isomorphism (m=1),

[
oxed{
DeltaPhi_Q
=
DeltaPhi_D
=
24pi,
}
]

so one CIR dyadic block corresponds to twelve full U(1) turns on the same-turn registry.

This is a representation statement. A physical system must still demonstrate that its QHTRI action phase actually traverses that registry.

## 6. Why the integer-degree gate matters

The earlier general affine candidate

[
Phi_D=lambda_PhiPhi_Q+Phi_0
]

is mathematically admissible as a map between two real coordinates.

But if the map is promoted to a phase-group registry, then

[
oxed{lambda_Phi=minmathbb Z.}
]

If it is additionally an orientation-preserving isomorphism,

[
oxed{lambda_Phi=1.}
]

Therefore (lambda_Phi) is not an admissible cosmological fit parameter on the same-phase branch.

## 7. Non-isomorphic covering branches

A degree (|m|>1) map is a legitimate U(1) homomorphism but is not one-to-one. It maps multiple QHTRI phase states to the same CIR wrapped phase.

Such a branch requires an independent physical reason for the covering degree (m). It may not be selected because it improves agreement with (H_0), redshift, BAO, CMB or another target.

The (m=0) homomorphism collapses all phase information and gives

[
dotPhi_D=0.
]

It cannot represent a nontrivial dynamic scale phase.

## 8. Registry firewall

The following implications remain forbidden without additional evidence:

[
Phi_Q=Phi_D
quad	ext{from symbol similarity alone},
]

[
m=1
quad	ext{without the isomorphism + orientation premises},
]

[
H_D=H_{m FLRW}
quad	ext{without a metric/observable binding for }D.
]

The exact result of this gate is the classification of admissible phase registries, not the physical selection of one registry.

## 9. Parent evidence

QHTRI main explicitly carries

[
S_I=-int U_I,dt,
qquad
Phi_I=S_I/eta_phi,
qquad
dotPhi_I=-U_I/eta_phi,
]

after a declared carrier action scale, while keeping physical carrier binding open.

CIR independently carries

[

u_D=kappaPhi_D.
]

The present gate supplies the missing group-theoretic registry classification between those two typed phase coordinates.

## 10. Verdict

EXACT GIVEN REGISTRY AXIOMS:

- continuous U(1) homomorphism (Rightarrow minmathbb Z);
- U(1) isomorphism (Rightarrow m=pm1);
- orientation-preserving isomorphism (Rightarrow m=1);
- fixed registry offsets disappear from (dotPhi);
- (H_D=kappa mdotPhi_Q).

OPEN PHYSICAL BINDING:

- whether CIR and QHTRI instantiate the same U(1) phase bundle;
- whether the physical registry is isomorphic;
- orientation selection;
- the metric/observable interpretation of (D).

FORBIDDEN:

- fitting (m) or (lambda_Phi) to cosmological targets;
- promoting same notation to same physical phase.
