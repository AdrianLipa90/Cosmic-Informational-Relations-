# CIR Relational Bundle, Coframe and Invariant Geometry v0.1

Status: `TIR_DERIVED_GEOMETRIC_ARCHITECTURE / COFRAME_PROMOTION_EXPLICIT / LOCAL_LC_CHAIN_CONDITIONAL`

Parent TIR commit: `853032e019824b836de43634d949da5566396153`

## 1. Purpose

This file continues the exact internal relation carrier into the typed TIR bundle/connection/coframe architecture. It states precisely where an internal relational geometry becomes a candidate physical spatial geometry and where gauge-invariant curvature begins.

The dependency chain is

\[
{\rm Herm}_0(2)
\to
E_{\rm rel}
\to
W_{ij}^{X}
\to
R_{ij}\in SO(3)
\to
\omega
\to
\Omega
\]

together with the independent soldering gate

\[
E_{\rm rel}
\xrightarrow{\ e\ }
T\Sigma
\to
h.
\]

Only after these structures are joined can the spatial GR sector be selected.

## 2. Local relation bundle

At each admitted local patch \(U_\alpha\),

\[
\mathfrak g_\alpha
\cong
{\rm Herm}_0(2)
\cong
\mathbb R^3.
\]

Using

\[
T_i=-\frac{i}{2}\sigma_i,
\]

one has

\[
[T_i,T_j]=\varepsilon_{ijk}T_k,
\]

so the real Lie-algebra bridge is

\[
\boxed{
\mathfrak{su}(2)\cong\mathfrak{so}(3).
}
\]

On overlaps, a spin-frame change

\[
U_{\alpha\beta}\in SU(2)
\]

induces

\[
\boxed{
R_{\alpha\beta}
=
{\rm Ad}_{U_{\alpha\beta}}
\in SO(3).
}
\]

The adjoint action preserves the Hilbert--Schmidt/Euclidean metric.

An exact \(SO(3)\) cocycle therefore defines an oriented metric rank-three relation bundle

\[
\boxed{
E_{\rm rel}\to\Sigma.
}
\]

At this point \(E_{\rm rel}\) is still an internal relational bundle.

## 3. Connection and rotational holonomy

A local \(su(2)\)-valued connection one-form is

\[
\mathcal A=\mathcal A^iT_i,
\]

with curvature

\[
\boxed{
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.
}
\]

Under the adjoint map this gives an \(so(3)\) connection \(\omega\) and curvature two-form

\[
\boxed{
\Omega^a{}_b
=
d\omega^a{}_b
+
\omega^a{}_c\wedge\omega^c{}_b.
}
\]

For a path \(\gamma_{ij}\), TIR types the spatial transporter as

\[
\boxed{
W_{ij}^{X}
=
\mathcal P\exp\left(\int_{\gamma_{ij}}\mathcal A\right)
\in SU(2),
}
\]

with

\[
R_{ij}={\rm Ad}_{W_{ij}^{X}}\in SO(3).
\]

For a closed loop,

\[
W_\gamma=\prod W_{ij}^{X}.
\]

Its conjugacy class is the gauge-covariant finite holonomy datum.

## 4. Pure-atlas firewall

An ordinary change of anchored affine charts has

\[
G_{ba}^{\rm atlas}
=
(R_{ba},t_{ba})
\in SE(3)
\]

with exact cocycle closure. Around a closed pure-atlas loop,

\[
\boxed{
G_C^{\rm atlas}=e_{SE(3)}.
}
\]

Therefore a non-trivial loop witness cannot be manufactured solely by coordinate/frame relabeling.

A physical/non-trivial holonomy candidate requires path-dependent connection transport, a genuine gluing obstruction, or another separately source-bound departure from pure-atlas transport.

## 5. Connection-lifted affine edge

The TIR affine relation vector is

\[
\mathbf e_{xy}
=
{\rm vec}(\mathcal E_{xy}).
\]

The connection-lifted edge is

\[
\boxed{
G_{xy}^{\nabla}
=
(R_{xy},\mathbf e_{xy})
\in SE(3).
}
\]

For a rotationally consistent triangle,

\[
R_{xz}=R_{xy}R_{yz},
\]

the endpoint defect is

\[
\mathbf c_{xyz}
=
\mathbf e_{xz}
-
(\mathbf e_{xy}+R_{xy}\mathbf e_{yz}).
\]

The closed affine loop then obeys

\[
\boxed{
R_C=I,
\qquad
\mathbf t_C=-\mathbf c_{xyz}.
}
\]

The discrete relational solder object satisfies

\[
\boxed{
\mathcal T_{xyz}=-\mathcal C_{xyz},
}
\]

so

\[
\boxed{
\mathbf t_C
=
{\rm vec}(\mathcal T_{xyz}).
}
\]

This is an exact finite-cell TIR identity on the declared rotationally consistent sector.

## 6. Solder/coframe promotion gate

The internal bundle becomes candidate spatial tangent geometry only after the explicit promotion

\[
\boxed{
E_{\rm rel}\;\widehat{=}\;T\Sigma.
}
\]

A coframe

\[
\boxed{
e^a=e^a{}_i\,dx^i
}
\]

solders the internal relation directions to coordinate tangent directions.

The induced spatial metric is

\[
\boxed{
h_{ij}
=
\delta_{ab}e^a{}_i e^b{}_j.
}
\]

A full-rank coframe is required:

\[
\det(e^a{}_i)\neq0.
\]

This soldering step is the central type-changing gate. It must not be replaced by visual similarity between a Bloch sphere/tetrahedron and physical space.

## 7. Small-cell Cartan limit

For a smooth refining family with cell scale \(\ell\to0\), the TIR parent theorem gives

\[
\boxed{
(T_{\triangle}^{\rm disc})^a
=
\frac12
T^a{}_{\mu\nu}
\Sigma_{\triangle}^{\mu\nu}
+
O(\ell^3),
}
\]

and

\[
\boxed{
R_\triangle
=
I
+
\frac12
\Omega_{\mu\nu}
\Sigma_{\triangle}^{\mu\nu}
+
O(\ell^3).
}
\]

Thus the two finite-loop channels separate:

```text
translation / solder closure -> Cartan torsion T^a
rotation / frame holonomy     -> curvature Omega^a_b
```

This is the precise continuum meaning of the loop data under the declared smooth-refinement assumptions.

## 8. Levi-Civita sector

The TIR primitive same-endpoint admissibility rule selects, on the endpoint-compatible sector,

\[
\mathcal C_{xyz}=0
\quad\Longrightarrow\quad
\mathcal T_{xyz}=0.
\]

Under regular refinement,

\[
\boxed{
T^a
=
de^a+\omega^a{}_b\wedge e^b
=
0.
}
\]

Because the \(SO(3)\) transport preserves the spatial metric,

\[
Dh=0.
\]

Metric compatibility plus zero torsion selects the unique Levi-Civita connection:

\[
\boxed{
D=D^{\rm LC}.
}
\]

Crucially,

\[
\boxed{
T^a=0
\;\not\Rightarrow\;
\Omega^a{}_b=0.
}
\]

The torsion-free GR branch may therefore retain non-zero curvature.

## 9. Representation firewall for torsion

Three statements must remain distinct:

1. Levi-Civita GR sector:
   \[
   T^a(\omega_{\rm LC})=0,\qquad
   R^a{}_b(\omega_{\rm LC})\ \text{may be non-zero};
   \]

2. teleparallel representation:
   \[
   R^a{}_b(\omega_{\rm TP})=0,\qquad
   T^a(\omega_{\rm TP})\ \text{may be non-zero};
   \]

3. broader Cartan/context-lifted TIR sector:
   non-zero torsion defects remain admissible when the primitive same-endpoint identification is not imposed.

These are different connection sectors. They must not be reported as contradictory torsion values for one connection.

## 10. First admissible invariant observables

After coframe promotion and connection selection, CIR may use quantities that do not depend on a mere local frame relabeling, including:

- conjugacy classes/traces of closed-loop holonomies;
- curvature two-form invariants built from \(\Omega\);
- the spatial Riemann/Ricci/scalar curvature derived from \(D^{\rm LC}\);
- metric distances/areas/volumes built from \(h\);
- after the spacetime join, four-dimensional curvature and mass invariants appropriate to the symmetry class.

By contrast, an isolated ADM shift, a chosen rapidity coordinate, a local Lorentz frame, or a pure-gauge connection is not by itself a physical invariant.

## 11. What is closed and what remains open

```text
Herm_0(2) local rank-three carrier             PASS STANDARD/TIR
SU(2) -> SO(3) adjoint frame transport         PASS STANDARD
relation bundle E_rel                          PASS CONDITIONAL ON COCYCLE
connection/curvature typing                    PASS STANDARD
pure-atlas loop identity                       PASS EXACT
connection-lifted SE(3) edge                   PASS TIR EXACT DEFINITION
endpoint defect <-> loop translation           PASS TIR EXACT
discrete solder -> Cartan torsion limit         PASS TIR CONDITIONAL THEOREM
rotational holonomy -> curvature limit          PASS TIR CONDITIONAL THEOREM
metric compatibility + T=0 -> Levi-Civita       PASS STANDARD
T=0 does not force curvature=0                  PASS
E_rel = T Sigma physical solder promotion       OPEN PHYSICAL/GEOMETRIC GATE
global smooth refinement                        OPEN
production physical realization                 OPEN
four-dimensional space-time join                DOWNSTREAM
cosmological source dynamics                    DOWNSTREAM OPEN
```

## 12. CIR consequence

CIR now has a typed geometric foundation in which the route to gravity is not

\[
\text{Berry phase}=\text{gravity}
\]

and not

\[
\text{torsion}=\text{gravity}.
\]

The admitted route is

\[
\boxed{
\text{relational state geometry}
\to
\text{internal relation carrier}
\to
\text{bundle + connection}
\to
\text{solder/coframe}
\to
\text{metric}
\to
\text{Levi-Civita curvature/invariants}
}
\]

with Berry holonomy retained as a distinct state-space parent and with broader torsional/teleparallel representations typed separately.

## 13. Parent provenance

Pinned TIR sources:

- `TIR/foundations/TIR_SPATIAL_BUNDLE_CONNECTION_V0_1.md`
- `TIR/foundations/TIR_WIJ_HOLONOMY_CROSSWALK_V0_1.md`
- `TIR/foundations/TIR_SE3_ANCHOR_SOURCE_BINDING_V0_1.md`
- `TIR/foundations/TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_V0_1.md`
- `TIR/foundations/TIR_CARTAN_CONTINUUM_REFINEMENT_V0_1.md`
- `TIR/foundations/TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.md`
