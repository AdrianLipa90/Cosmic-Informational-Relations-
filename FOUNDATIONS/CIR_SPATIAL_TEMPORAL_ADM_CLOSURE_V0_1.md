# CIR Spatial × Temporal ADM Closure v0.1

Status: `EXACT_CONDITIONAL_LORENTZIAN_RECONSTRUCTION / STANDARD_ADM_CLOSURE / PRODUCTION_EVENT_SPATIAL_INPUT_OPEN`

Parent TIR commit: `853032e019824b836de43634d949da5566396153`

## 1. Purpose

This file is the first four-dimensional CIR foundation layer. It joins the admitted TIR spatial geometry packet to an independently typed temporal packet without collapsing structural dependency into temporal order.

The inputs are

\[
\mathfrak S_X
=
(\Sigma,h_{ij},D_i,{}^{(3)}R^i{}_{jkl})
\]

and

\[
\mathfrak T
=
(\Theta,N_\Theta,\mathcal K_{ij};\beta^i_{\rm match}).
\]

The matching field \(\beta^i\) is foliation/coordinate interface data, not a standalone physical source.

## 2. ADM reconstruction

For positive lapse

\[
N_\Theta>0
\]

and positive-definite spatial metric \(h_{ij}\), define

\[
\boxed{
ds^2
=
-N_\Theta^2d\Theta^2
+
h_{ij}(dx^i+\beta^i d\Theta)(dx^j+\beta^j d\Theta).
}
\]

Thus

\[
g_{00}
=
-N_\Theta^2+h_{ij}\beta^i\beta^j,
\qquad
g_{0i}=h_{ij}\beta^j,
\qquad
g_{ij}=h_{ij}.
\]

The Schur complement of the spatial block is exactly

\[
\boxed{
g_{00}-g_{0i}h^{ij}g_{0j}
=
-N_\Theta^2<0.
}
\]

Hence

\[
\boxed{
\det g=-N_\Theta^2\det h<0
}
\]

and the block metric has Lorentzian signature \((-+++)\).

The inverse metric is

\[
\boxed{
g^{00}=-\frac1{N_\Theta^2},
\qquad
g^{0i}=\frac{\beta^i}{N_\Theta^2},
\qquad
g^{ij}=h^{ij}-\frac{\beta^i\beta^j}{N_\Theta^2}.
}
\]

This is exact conditional geometry; it is not yet a dynamical Einstein solution.

## 3. Normal and deformation tensor

The future-directed unit normal to the leaf may be written

\[
n_\mu=(-N_\Theta,0,0,0),
\]

\[
\boxed{
n^\mu
=
\left(
\frac1{N_\Theta},
-\frac{\beta^i}{N_\Theta}
\right).
}
\]

Using the sign convention pinned by TIR, the extrinsic-curvature/deformation tensor is

\[
\boxed{
\mathcal K_{ij}
=
\frac1{2N_\Theta}
\left(
D_i\beta_j+D_j\beta_i-\partial_\Theta h_{ij}
\right).
}
\]

No second definition of \(\mathcal K_{ij}\) is introduced in CIR.

## 4. ADM closure conditions

Let

\[
K=h^{ij}\mathcal K_{ij}.
\]

The Hamiltonian constraint is

\[
\boxed{
{}^{(3)}R+K^2-\mathcal K_{ij}\mathcal K^{ij}
=
16\pi G\,\rho
}
\]

in the convention used by the parent interface.

The momentum constraint is

\[
\boxed{
D_j
\left(
\mathcal K^{ij}-h^{ij}K
\right)
=
8\pi G\,j^i.
}
\]

These are closure tests after the geometry/time/matter packets have been supplied. CIR does not count writing these equations down as deriving their sources.

## 5. Preferred source route for metric time evolution

The preferred TIR production architecture does not identify a NOEMA/PhaseNav runtime state with physical spacetime.

Instead, one source envelope must bind

\[
\boxed{
\text{IDT realized event}
\longleftrightarrow
\text{TIR spatial snapshot}
}
\]

under the same:

- physical realization ID;
- immutable physical realization receipt;
- clock identity;
- source lineage.

For an edge \(u\to v\),

\[
\Delta x^0_{uv}
=
\alpha(\Theta_v-\Theta_u),
\qquad
\alpha>0,
\]

and the source-backed metric-rate estimator is

\[
\boxed{
\mathcal D_{ij}^{(uv)}
=
\frac{h_{ij}(v)-h_{ij}(u)}
{\Delta x^0_{uv}}.
}
\]

Under regular refinement,

\[
\mathcal D_{ij}^{(uv)}
\to
\partial_0h_{ij}.
\]

The existing RF-E9 operator remains the unique extrinsic-curvature authority:

\[
\boxed{
K_{ij}
=
\frac1{2N}
\left(
-\partial_0h_{ij}
+
D_ib_j+D_jb_i
\right).
}
\]

This prevents a second hidden gravitational dynamics from being introduced at the CIR interface.

## 6. Production firewall

The following are not production substitutes for a physical event-spatial realization:

```text
NOEMA runtime vectors
PhaseNav / Terminal36D phase states
synthetic event graphs
reference fixtures
inferred event IDs without source receipts
```

They may validate software or mathematics, but not the physical source binding.

## 7. Spherical vacuum control

On the admitted stationary, spherically symmetric, unit-lapse, intrinsically flat spatial slicing, use

\[
ds^2
=
-c^2dt^2
+
(dr-V(r)dt)^2
+
r^2d\Omega^2.
\]

Then

\[
{}^{(3)}R=0
\]

and, up to one overall sign convention,

\[
K^r{}_r=\frac{V'}c,
\qquad
K^\theta{}_\theta=K^\phi{}_\phi=\frac{V}{cr}.
\]

The vacuum Hamiltonian constraint gives

\[
\boxed{
\frac{2}{c^2}\frac Vr
\left(
2V'+\frac Vr
\right)
=
0.
}
\]

On the non-trivial branch,

\[
2V'+\frac Vr=0,
\]

hence

\[
\boxed{
\frac{d}{dr}(rV^2)=0
}
\]

and

\[
\boxed{
V^2(r)=\frac Cr.
}
\]

Weak-field/ADM mass normalization then gives

\[
\boxed{
C=2GM.
}
\]

This is a conditional GR control after the ADM/Einstein gate is admitted. It does not derive the microscopic TIR source of the coframe.

## 8. Flat-FLRW control

For

\[
\mathbf V=H(t)\mathbf R
\]

on flat spatial slices,

\[
K^i{}_j=\frac Hc\delta^i{}_j
\]

up to sign, so

\[
\boxed{
K^2-K_{ij}K^{ij}
=
\frac{6H^2}{c^2}.
}
\]

The Hamiltonian equation gives

\[
\boxed{
H^2
=
\frac{8\pi G}{3c^2}\varepsilon
+
\frac{\Lambda c^2}{3}.
}
\]

For \(\varepsilon=\rho_m c^2\),

\[
\boxed{
H^2
=
\frac{8\pi G}{3}\rho_m
+
\frac{\Lambda c^2}{3}.
}
\]

The kinematic identity

\[
\frac{D\mathbf V}{Dt}
=
(\dot H+H^2)\mathbf R
=
\frac{\ddot a}{a}\mathbf R
\]

does not determine the sign of \(\ddot a\). Acceleration requires a source/equation-of-state or a derived geometric modification.

## 9. First 4D invariant layer

After a physical spacetime carrier is admitted, CIR may evaluate coordinate/frame-invariant quantities appropriate to the sector, including:

- four-dimensional Riemann/Ricci/scalar curvature;
- Einstein tensor and constraint residuals;
- Weyl invariants where non-zero;
- geodesic deviation / optical tidal invariants;
- symmetry-specific quasi-local masses, including Misner--Sharp mass in spherical symmetry;
- closed-loop holonomy conjugacy data.

The ADM shift itself remains gauge/slicing dependent.

## 10. Status ledger

```text
ADM block reconstruction                         PASS STANDARD EXACT CONDITIONAL
Schur complement = -N^2                          PASS EXACT
det(g) = -N^2 det(h)                             PASS EXACT
Lorentzian signature for h>0,N>0                 PASS EXACT CONDITIONAL
inverse ADM metric                               PASS EXACT
K_ij kinematic seam                              PASS STANDARD
Hamiltonian/momentum constraints                 PASS STANDARD GR CONDITIONS
event-spatial metric-rate contract               PASS EXECUTABLE CONTRACT
same-realization/same-clock production firewall  PASS CONTRACT
production physical event-spatial bundle         OPEN INPUT
spherical vacuum V^2=C/r                         PASS CONDITIONAL GR DERIVATION
C=2GM                                            PASS CONDITIONAL MASS NORMALIZATION
flat-FLRW Hamiltonian crosswalk                  PASS STANDARD/CONDITIONAL
late-time acceleration source                    OPEN
microscopic TIR source -> physical coframe       OPEN
```

## 11. Parent provenance

Pinned TIR sources:

- `TIR/foundations/TIR_SPATIAL_TEMPORAL_CLOSURE_INTERFACE_V0_1.md`
- `TIR/foundations/TIR_FLOW_COFRAME_ADM_CONSTRAINT_GRAVITY_V0_1.md`
- `TIR/integration/TIR_IDT_EXTRINSIC_CURVATURE_SOURCE_BRIDGE_V0_1.md`
- `TIR/integration/TIR_IDT_EVENT_SPATIAL_STATE_BINDING_V0_1.md`
- `TIR/foundations/TIR_GRAVITY_DERIVATION_SPINE_V0_1.md`
