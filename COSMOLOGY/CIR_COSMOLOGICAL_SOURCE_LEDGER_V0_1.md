# CIR Cosmological Source Ledger v0.1

Status: `SOURCE_LEDGER / EXACT_ACCELERATION_CRITERIA / RETAINED_NO_GO_RESULTS / PHYSICAL_NORMALIZATION_AND_LOCAL_RESPONSE_OPEN`

Parent TIR commit: `853032e019824b836de43634d949da5566396153`

## 1. Purpose

CIR enters cosmology only after the spatial, coframe and ADM layers have been typed. This ledger records what the current TIR/IDT/RFC stack actually permits, what it exactly excludes, and which source bindings remain open.

The ledger does not identify a mathematical acceleration criterion with observed dark energy.

## 2. Base FLRW active-source condition

On the flat homogeneous/isotropic Einstein branch with \(x^0=ct\),

\[
3H_0^2=\kappa_E\rho,
\qquad
H_0'=-\frac{\kappa_E}{2}(\rho+p),
\]

so

\[
\boxed{
\frac{a''}{a}
=
-\frac{\kappa_E}{6}(\rho+3p).
}
\]

In physical time,

\[
\boxed{
\frac{\ddot a}{a}
=
-\frac{\kappa_Ec^2}{6}(\rho+3p).
}
\]

Therefore

\[
\boxed{
\ddot a>0
\iff
\rho+3p<0
}
\]

on this base branch.

A metric-rate measurement or ADM shift does not by itself supply the required negative active source.

## 3. Canonical information-scalar route

For the homogeneous canonical information field,

\[
\rho_I
=
\frac12(\phi_I')^2+U_I,
\qquad
p_I
=
\frac12(\phi_I')^2-U_I.
\]

The parent TIR/RFC identifications are

\[
\phi_I=\sqrt{2\Xi_I},
\qquad
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I.
\]

Hence

\[
(\phi_I')^2
=
\frac{(\Xi_I')^2}{2\Xi_I}
\]

and

\[
\boxed{
\frac{a''}{a}\Big|_I
=
\frac{\alpha_I\Xi_I}{3}
-
\frac{\kappa_E}{6\Xi_I}(\Xi_I')^2.
}
\]

For \(\Xi_I>0\) and \(\alpha_I>0\),

\[
\boxed{
\frac{a''}{a}>0
\iff
\left|\partial_0\ln\Xi_I\right|
<
\sqrt{\frac{2\alpha_I}{\kappa_E}}.
}
\]

If

\[
m_I^2=\frac{\alpha_I}{\kappa_E},
\]

then

\[
\boxed{
\left|\partial_0\ln\Xi_I\right|<\sqrt2\,m_I.
}
\]

This is an exact local criterion on the admitted parent action. It is not an absolute prediction because the physical normalization of \(\alpha_I\), equivalently \(m_I\), remains open.

## 4. Information-rate decomposition

The parent projective cell gives

\[
\Xi_I
=
\frac{\mathcal J_\pi}{a_{\rm FS}}
\left(\frac{\omega}{c}\right)^2.
\]

Therefore

\[
\boxed{
\partial_t\ln\Xi_I
=
\partial_t\ln\mathcal J_\pi
-
\partial_t\ln a_{\rm FS}
+
2\partial_t\ln|\omega|.
}
\]

On a constant dimensionless projective-area cell,

\[
\boxed{
\partial_t\ln\Xi_I
=
\frac{\dot{\mathcal J}_\pi}{\mathcal J_\pi}
+
2\frac{\dot\omega}{\omega}.
}
\]

This supplies a measurable/formal decomposition of the acceleration gate once all terms have independently source-backed physical meaning.

Using the same phase observable both to construct \(\Xi_I\) and to calibrate \(m_I\) without an independent receipt is circular and is not a prospective prediction.

## 5. Scalar potential versus dynamic-Lambda bookkeeping

The potential may remain in the scalar stress tensor,

\[
T_{\mu\nu}^{I}
=
T_{\mu\nu}^{\rm kin}
-U_Ig_{\mu\nu},
\]

or be moved to the geometric side through

\[
\boxed{
\Lambda_I
=
\kappa_EU_I
=
\alpha_I\Xi_I.
}
\]

These are algebraically equivalent bookkeeping representations of the same source.

Therefore

\[
\boxed{
U_I\ \text{must not be counted simultaneously in}\ 
T_{\mu\nu}
\ \text{and}\ 
\Lambda_Ig_{\mu\nu}.
}
\]

A separate bare \(\Lambda\) is not mathematically required for this scalar-potential route, but physical normalization and observational validation remain open.

## 6. Current temporal-holonomy spectator no-go

The currently admitted scalar action satisfies

\[
\boxed{
U_I=U_I(\Xi_I),
\qquad
\frac{\partial U_I}{\partial\tau_R}=0.
}
\]

Thus \(\tau_R\) is retained as an oriented holonomy coordinate but is a spectator in the current scalar stress-energy.

Consequently,

\[
\boxed{
\text{the current scalar action does not derive accelerated expansion from }\tau_R.
}
\]

This is a no-go for the current action, not for every possible holonomy-active completion.

## 7. Equal-stress partition no-go

Define

\[
C_h=\cos^2\frac{\tau_R}{2},
\qquad
D_h=\sin^2\frac{\tau_R}{2},
\qquad
C_h+D_h=1.
\]

If

\[
U_C=U_IC_h,
\qquad
U_D=U_ID_h
\]

and both channels carry the same gravitational stress type, then

\[
\boxed{
U_C+U_D
=
U_I(C_h+D_h)
=
U_I.
}
\]

All \(\tau_R\)-dependence cancels from the total potential.

Therefore

\[
\boxed{
\text{naming }D_h\text{ a dark channel does not create dark energy.}
}
\]

A holonomy-dependent gravitational contribution requires new physical structure: different stress attribution, a separately derived action term, an independent dynamical field, or a genuinely nonlocal/topological sector.

## 8. Naive local holonomy-potential stability obstruction

For the diagnostic local potential

\[
U_D(\tau_R)
=
U_I\sin^2\frac{\tau_R}{2},
\qquad
U_I>0,
\]

one finds

\[
\frac{\partial^2U_D}{\partial\tau_R^2}
=
\frac{U_I}{2}\cos\tau_R.
\]

At the maximal \(D_h=1\) point,

\[
\tau_R=\pi,
\]

therefore

\[
\boxed{
\frac{\partial^2U_D}{\partial\tau_R^2}
=
-\frac{U_I}{2}<0.
}
\]

The maximal local \(D\)-sector is a potential maximum in this naive positive-kinetic scalar realization. The simple single-cosine partition does not supply local dynamical stability.

This does not exclude a topologically frozen global holonomy sector, which is a different physical hypothesis and remains open.

## 9. Pure phase-kinetic no-go

The RF-E4 pure homogeneous phase-kinetic sector has

\[
\boxed{
\rho_{\rm phase}=K,
\qquad
p_{\rm phase}=K,
\qquad
w_{\rm phase}=+1.
}
\]

Thus

\[
\rho_{\rm phase}+3p_{\rm phase}=4K>0
\]

and

\[
\boxed{
\frac{a''}{a}\Big|_{\rm phase,kin}
=
-\frac{2\kappa_E}{3}K<0.
}
\]

Pure phase kinetic energy is a stiff decelerating source. It is not a dark-energy mechanism.

## 10. Genuine non-bookkeeping RF-F20 response candidate

The parent RFC action contains the metric-response tensor

\[
\boxed{
\Delta T_{\mu\nu}^{\rm phase}
=
4A^2R_{\mu\nu},
}
\]

with

\[
R_{\mu\nu}
=
g^{\alpha\beta}q_\alpha
\frac{\partial\mathcal A_\beta^{ABE}}
{\partial g^{\mu\nu}}.
\]

Unlike the \(C_h/D_h\) repartition, this term can modify the metric variation of the action and is therefore a genuine candidate additional source term if its local connection response is physically source-bound.

In a homogeneous/isotropic orthonormal frame,

\[
R_{\hat a\hat b}
=
{\rm diag}(R_0,R_s,R_s,R_s),
\]

so

\[
\Delta\rho_R=4A^2R_0,
\qquad
\Delta p_R=4A^2R_s,
\]

and

\[
\boxed{
\Delta(\rho+3p)_R
=
4A^2(R_0+3R_s).
}
\]

The corresponding acceleration correction is

\[
\boxed{
\Delta\left(\frac{a''}{a}\right)_R
=
-\frac{2\kappa_EA^2}{3}(R_0+3R_s).
}
\]

Therefore this contribution is acceleration-producing by itself exactly when

\[
\boxed{
R_0+3R_s<0.
}
\]

The sign and magnitude of \(R_0+3R_s\) are not currently derived from a production temporal holonomy source.

## 11. Global holonomy is not the local metric response

The integrated temporal holonomy

\[
\tau_R
=
{\rm wrap}_\pi\Phi_T(C)
\]

does not determine

\[
\frac{\partial\mathcal A_\beta}{\partial g^{\mu\nu}}.
\]

Two connections can share a loop holonomy and differ in their local off-shell metric response.

The missing local source theorem is

\[
\boxed{
\text{source-bound temporal }U(1)
\to
\mathcal A_\beta^{BE}[g]
\to
\Pi^{BE}_{\beta|\mu\nu}
\to
R_{\mu\nu}^{BE}
\to
\Delta T_{\mu\nu}^{\rm phase}.
}
\]

Only after this bridge is established may \(\tau_R\) be tested as a predictor or sector label for the local response.

## 12. Electromagnetic double-count firewall

The electromagnetic sector already carries Maxwell stress.

Therefore a Berry/Euler/temporal-holonomy cosmology route may not count the same electromagnetic contribution once through the Maxwell tensor and again through a relabelled \(R_{\mu\nu}^{AB}\) phase response.

The intended new source must be independently source-bound and non-duplicative.

## 13. Current strongest source-ledger equation

When both the canonical information scalar and a separately admitted RF-F20 response are present,

\[
\boxed{
\frac{a''}{a}
=
\frac{\alpha_I\Xi_I}{3}
-
\frac{\kappa_E}{6\Xi_I}(\Xi_I')^2
-
\frac{2\kappa_EA^2}{3}(R_0+3R_s)
+
\text{other admitted sources}.
}
\]

This is a source-ledger equation, not a cosmological prediction.

## 14. Observable-side event estimator

For isotropic spatial snapshots,

\[
\det h=a^6,
\qquad
y=\ln a=\frac16\ln\det h.
\]

Then

\[
\frac{a''}{a}=y''+(y')^2.
\]

For three equally spaced source-backed events in \(x^0\),

\[
\boxed{
\mathcal A_n^{\rm event}
=
\frac{y_{n+1}-2y_n+y_{n-1}}{(\Delta x^0)^2}
+
\left(
\frac{y_{n+1}-y_{n-1}}{2\Delta x^0}
\right)^2.
}
\]

On a smooth event refinement this centered estimator is second-order accurate.

This gives an observable-side test that is independent of which source mechanism is proposed.

## 15. Open physical gates

```text
absolute alpha_I / m_I normalization                    OPEN
independent KG/phase spectral identification            OPEN
production event-spatial cosmology realization          OPEN
nontrivial holonomy persistence/stability                OPEN
differential C_h/D_h physical stress attribution         OPEN
Bianchi-compatible complementary-channel ledger          OPEN
same temporal U(1) bundle admission                     OPEN
temporal U(1) -> local A^{BE}[g] response law            OPEN
production R0+3Rs sign and magnitude                    OPEN
electromagnetic non-double-count receipt                 OPEN
dimensionful cosmological scale / rho_crit binding      OPEN
late-time H(z) / distance validation                     OPEN
perturbation and structure-growth validation             OPEN
```

## 16. Current verdict

The current foundation supports:

\[
\boxed{
\text{information-scalar potential: exact local acceleration criterion}
}
\]

and

\[
\boxed{
\text{RF-F20 metric response: exact conditional acceleration sign criterion}.
}
\]

It also supports two retained exclusions:

\[
\boxed{
\text{pure phase kinetic sector is decelerating}
}
\]

and

\[
\boxed{
\text{equal-stress }C_h/D_h\text{ repartition creates no new gravity}.
}
\]

It does **not** yet establish a physical dark-energy source or an empirical fit to cosmic acceleration.

## 17. Parent provenance

Pinned TIR sources:

- `TIR/integration/TIR_IDT_RFC_INFORMATION_HOLONOMY_COSMOLOGICAL_ACCELERATION_V0_1.md`
- `TIR/integration/TIR_IDT_RFC_TEMPORAL_U1_METRIC_RESPONSE_COSMOLOGY_V0_1.md`
- `TIR/foundations/TIR_GRAVITY_DERIVATION_SPINE_V0_1.md`
- `TIR/CURRENT_STATUS.md`
