# CIR Source–Phase–Log-Scale Identifiability v0.1

Status: CONDITIONAL EXACT BRIDGE / IDENTIFIABILITY FIREWALL / PHYSICAL COSMOLOGICAL BINDING OPEN  
Date: 2026-10-04

## 1. Scope

This note separates the exact CIR log-scale representation, the QHTRI dynamical phase law, and the GREMLIN/RFC source-density carrier.

No value of \(H_0\), no cosmological distance datum, and no target redshift is used to fix a coefficient.

Two follow-on gates now sharpen the original bridge:

- \`CIR_PHASE_REGISTRY_GATE_V0_1.md\`;
- \`CIR_DENSITY_TO_POTENTIAL_GATE_V0_1.md\`.

They supersede the earlier use of an arbitrary continuous phase slope \(\lambda_\Phi\) whenever the registry is required to be a genuine \(U(1)\) homomorphism, and they resolve the density-versus-extensive-energy typing.

## 2. Exact CIR log-scale identity

Let \(D(t)>0\) be a dimensionless multiplicative scale coordinate,

\[
\nu_D(t):=\ln D(t).
\]

On the declared CIR representation branch,

\[
\boxed{
\nu_D=\kappa\Phi_D,
\qquad
\kappa=\frac{\ln2}{24\pi}.
}
\]

Therefore

\[
D=e^{\kappa\Phi_D}
\]

and, wherever differentiable,

\[
\boxed{
H_D
:=
\frac{d\ln D}{dt}
=
\frac{\dot D}{D}
=
\kappa\dot\Phi_D.
}
\]

This is exact on the declared representation.

### Firewall

\(H_D\) is a relational log-scale rate. It is not automatically the FLRW Hubble parameter.

The identification

\[
H_D=H_{\rm FLRW}=\frac{\dot a}{a}
\]

requires an independent metric/observable map such as \(D=a/a_\star\), or another source-backed cosmological scale binding.

## 3. Phase registry

QHTRI carries a phase-action law

\[
\Phi_Q=\frac{S_Q}{\eta_\phi},
\qquad
\dot\Phi_Q=-\frac{E_Q}{\eta_\phi},
\]

after a carrier action scale and source energy have been admitted.

The CIR phase \(\Phi_D\) and QHTRI phase \(\Phi_Q\) remain provenance-distinct until a registry is supplied.

For a general real-coordinate map one could write

\[
\Phi_D=\lambda_\Phi\Phi_Q+\Phi_0.
\]

However, the dedicated phase-registry gate proves that if the physical map is required to be a continuous group homomorphism

\[
U(1)\to U(1),
\]

then

\[
\boxed{
\lambda_\Phi=m\in\mathbb Z.
}
\]

For a strict group homomorphism, the identity is preserved and a lifted branch has

\[
\Phi_D=m\Phi_Q+2\pi k,
\qquad
\dot\Phi_D=m\dot\Phi_Q.
\]

A constant \(\Phi_0\) is admissible only when the phases are treated as torsors with independently chosen origins; the affine torsor map

\[
\Phi_D=m\Phi_Q+\Phi_0+2\pi k
\]

is not a group homomorphism unless \(\Phi_0=0\pmod{2\pi}\).

If the registry is an isomorphism, \(m=\pm1\). If it is additionally orientation-preserving,

\[
\boxed{m=1.}
\]

Hence the registry slope is not a cosmological fit parameter on the same-phase branch.

## 4. GREMLIN/RFC source-density carrier

The RFC/GREMLIN branch defines

\[
\boxed{
\rho_G
=
\frac{B\omega\mathcal N}{AR}
(\tilde\phi+\kappa),
\qquad
AR=A\,R.
}
\]

Equivalently,

\[
V_R:=AR,
\qquad
n_R:=\frac{\mathcal N}{V_R},
\]

\[
\epsilon_\Psi:=B\omega(\tilde\phi+\kappa),
\qquad
\rho_G=n_R\epsilon_\Psi.
\]

Thus

\[
Q:=\frac{B\omega\mathcal N}{AR}
\]

is a source-density prefactor, not a dimensionless radial coordinate.

### Hyperbolic-coordinate firewall

A coordinate such as

\[
z=\tanh(\chi/2)e^{i\theta}
\]

requires dimensionless \(\chi\).

Therefore

\[
\chi=Q
\]

is not typed on the current source branch. A dimensionally admissible candidate is

\[
\boxed{
\hat\chi=\frac{Q}{Q_\star},
\qquad
z=\tanh(\hat\chi/2)e^{i\theta},
}
\]

where \(Q_\star\) must be fixed independently of cosmological targets.

## 5. Five-factor carrier identifiability theorem

Assume \(B,\omega,\mathcal N,A,R>0\) and that an observable depends on those variables only through

\[
Q=\frac{B\omega\mathcal N}{AR}.
\]

Use logarithmic coordinates

\[
x=
(\ln B,\ln\omega,\ln\mathcal N,\ln A,\ln R)^T.
\]

Then

\[
\ln Q=c^Tx,
\qquad
c=(1,1,1,-1,-1)^T.
\]

Hence

\[
\boxed{
\operatorname{rank}J_Q=1,
\qquad
\dim\ker J_Q=4.
}
\]

For any \(v\in\mathbb R^5\) satisfying

\[
v_B+v_\omega+v_N-v_A-v_R=0,
\]

the positive multiplicative rescaling

\[
(B,\omega,\mathcal N,A,R)
\mapsto
(e^{v_B}B,e^{v_\omega}\omega,e^{v_N}\mathcal N,e^{v_A}A,e^{v_R}R)
\]

leaves \(Q\) invariant.

Therefore \(Q\)-only observations cannot identify all five factors separately without additional independent source constraints.

This is the five-factor counterpart of the GREMLIN v0.8 product-identifiability firewall.

## 6. Exact cell-integration identity

RFC RF-S16 supplies

\[
j_{Q,a}=q_0\frac{\mathcal N_a}{V_a},
\qquad
\epsilon_{Q,a}
=
\frac{B_a\omega_a}{q_0}
(\phi_a+\kappa),
\]

so

\[
\rho_{G,a}
=
\epsilon_{Q,a}j_{Q,a}.
\]

Multiplying by the same cell volume gives

\[
\boxed{
E_a
=
V_a\rho_{G,a}
=
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

Both \(V_a\) and the carrier bookkeeping quantum \(q_0\) cancel.

For multiple cells,

\[
\boxed{
E_\Sigma
=
\sum_aV_a\rho_{G,a}
=
\sum_aB_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

This cancellation is cellwise and does not require a homogeneous multi-cell state.

## 7. Density and carrier energy are distinct typed objects

RF-L2 places \(U_L\) in the scalar-field Lagrangian density and gives

\[
T^{\rm pot}_{\mu\nu}=-U_Lg_{\mu\nu}.
\]

RF-I1/RF-E17 explicitly distinguish the local scalar-potential density from an integrated cell energy:

\[
\boxed{
H_{\rm clk}=V_{\rm cell}U_{\rm clk}.
}
\]

Therefore the QHTRI action-phase law with an ordinary action scale must consume an extensive energy coordinate,

\[
\boxed{
\dot\Phi_Q=-\frac{E_Q}{\eta_\phi},
}
\]

not a raw energy density, unless a separate action-density scale is declared.

The physical identification

\[
E_Q
\stackrel{?}{=}
E_\Sigma
\]

remains a source-binding gate.

## 8. Conditional source-to-log-scale equation

Compose:

\[
H_D=\kappa\dot\Phi_D,
\]

\[
\dot\Phi_D=m\dot\Phi_Q,
\]

\[
\dot\Phi_Q=-\frac{E_Q}{\eta_\phi}.
\]

Then

\[
\boxed{
H_D
=
-\frac{\kappa m}{\eta_\phi}E_Q.
}
\]

If the QHTRI action source is physically admitted as the same RFC extensive source,

\[
E_Q=E_\Sigma,
\]

then

\[
\boxed{
H_D
=
-\frac{\kappa m}{\eta_\phi}
\sum_a
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

For the orientation-preserving isomorphic registry \(m=1\),

\[
\boxed{
H_D
=
-\frac{\kappa}{\eta_\phi}
\sum_a
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

This equation contains no \(H_0\) fit.

It remains conditional because the QHTRI source-energy binding, support selection, action-scale calibration, and cosmological interpretation of \(D\) are not yet physically closed.

## 9. Local-density alternative

A local phase-field law could instead use an action-density scale \(\eta_\phi^{(V)}\):

\[
\partial_t\Phi_Q(x)
=
-\frac{\rho_G(x)}{\eta_\phi^{(V)}}.
\]

This is not the same interface as

\[
\dot\Phi_Q=-E_Q/\eta_\phi.
\]

The two may be related only after a declared support-volume map.

Thus the earlier ambiguity “does \(AR\) remain or cancel?” is now type-resolved:

- \(AR\) remains in the **local density** \(\rho_G\);
- \(AR\) cancels in the **complete same-cell extensive energy** \(V_R\rho_G\);
- a partial/nonlocal response is represented by an independently sourced support kernel, not by silently changing the volume factor.

## 10. Dyadic representation consequence

The CIR representation satisfies

\[
\Delta\Phi_D=24\pi
\Longrightarrow
\Delta\nu_D=\ln2
\Longrightarrow
D\mapsto2D.
\]

Under a degree-\(m\) U(1) registry,

\[
\Delta\Phi_Q=\frac{24\pi}{m}.
\]

For the orientation-preserving isomorphism,

\[
\boxed{
\Delta\Phi_Q=\Delta\Phi_D=24\pi.
}
\]

No physical claim follows until a real carrier is shown to instantiate this registry.

## 11. No-fit and type firewalls

Forbidden:

- \(Q=H\);
- raw dimensionful \(Q\) used directly as a \(\tanh\) argument;
- same symbol \(\Phi\) used as proof of same physical phase;
- fitting registry degree \(m\) or a continuous \(\lambda_\Phi\) to cosmological data;
- fitting \(Q_\star\), \(\eta_\phi\), support weights, or a support volume to \(H_0\);
- inserting \(\rho_G\) into an ordinary action-phase law without integration or action-density retyping;
- identifying \(H_D\) with \(H_{\rm FLRW}\) before a metric/observable map for \(D\) is derived.

## 12. Current gates

Closed mathematically / structurally:

- \(H_D=d\ln D/dt=\kappa\dot\Phi_D\);
- integer-degree \(U(1)\) registry classification;
- orientation-preserving isomorphism implies \(m=1\);
- five-factor \(Q\)-identifiability rank \(1\), nullity \(4\);
- same-cell source integration \(V\rho_G=B\omega\mathcal N(\phi+\kappa)\);
- multi-cell extensive sum.

Open physically:

1. **QHTRI_SOURCE_ENERGY_BINDING** — which RFC extensive source enters the QHTRI action?
2. **SUPPORT_KERNEL_SELECTION** — which cells/weights constitute that source?
3. **ACTION_SCALE_CALIBRATION** — what fixes \(\eta_\phi\)?
4. **PHASE_REGISTRY_SELECTION** — do CIR and QHTRI instantiate the same \(U(1)\) bundle and orientation?
5. **SOURCE_NORMALIZATION_GATE** — what independently fixes \(Q_\star\) for any hyperbolic radial coordinate?
6. **CIR_METRIC_OBSERVABLE_BINDING** — what exactly is \(D\) physically?
7. **PROSPECTIVE_TEST_GATE** — only after the above, freeze a no-refit cosmological prediction.

## 13. Parent provenance

- CIR base at branch creation: \`cbe7cb292d6f164b656ba38a051b7914c40fbad2\`.
- TIR parent pinned by CIR: \`853032e019824b836de43634d949da5566396153\`.
- GREMLIN main used for source-density and source/coupling identifiability: \`b0000828238e0cd244f5eb1fb679155315df372f\`.
- RFC main inspected for the present refinement: \`664349e2f16b57ee23bf6f5f21f5fe8ada17c5a5\`.
- QHTRI current main inspected for the present refinement: \`f95589ff1c7e5e7cee6b1bcaf079c3c3eb4fc500\`.
- QHTRI phase-mechanics construction commit: \`6a454f6daf6a225978ea00482d83b298187437f6\`.

No parent source is promoted beyond its own declared authority.
