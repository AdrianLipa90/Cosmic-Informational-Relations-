# CIR Lambda0–RDSS–Aharonov–Bohm Variational Bridge (candidate v0.1)

Date: 2026-11-15  
Status: RESEARCH CANDIDATE / CONDITIONAL MATHEMATICAL CONSTRUCTION / NO PHYSICAL PROMOTION

## 1. Scope and existing parent authority

This candidate integrates the historical Lambda0 manuscript (2025-06-02) with the *existing* CIR source, coframe and ADM contracts. It does **not** establish a new gravitational law, experimental proof of phase-induced gravity, or an equivalence of electromagnetic U(1) transport and the Lorentz connection.

Internal CIR parents:
- FOUNDATIONS/CIR_RELATIONAL_BUNDLE_COFRAME_INVARIANTS_V0_1.md
- FOUNDATIONS/CIR_SPATIAL_TEMPORAL_ADM_CLOSURE_V0_1.md
- COSMOLOGY/CIR_COSMOLOGICAL_SOURCE_LEDGER_V0_1.md
- COSMOLOGY/CIR_SOURCE_PHASE_LOGSCALE_IDENTIFIABILITY_V0_1.md
- CLAIM_STATUS.md

Preserve the canonical information normalization

\[
\kappa=\frac{\ln 2}{24\pi}.
\]

Distinguish \(\kappa\) from the Einstein coupling \(\kappa_E=8\pi G/c^4\). All action equations below are in a declared \(c=1\) geometric-unit convention until physical units are restored.

## 2. Geometric carrier, not a new metric by relabeling

Use the already admitted conditional ADM Lorentzian carrier

\[
ds^2=-N^2d\Theta^2+h_{ij}(dx^i+\beta^i d\Theta)(dx^j+\beta^j d\Theta),
\]

with \(N>0,\ h>0\), giving \(\det g=-N^2\det h\). Physical soldering, a source-backed event/spatial realization, and all upstream promotion gates remain OPEN.

The historical RDSS conformal deformation

\[
g_{\mu\nu}^{\mathrm{diagnostic}}=e^{2\chi}\bar g_{\mu\nu}
\]

is a useful restricted diagnostic subclass; it is not a replacement for the general ADM metric or a derivation of arbitrary spacetime.

## 3. Gauge-covariant phase carrier

Let \(A_\mu\) be an electromagnetic U(1) connection, with

\[
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,\qquad
W_\gamma=\exp\left(\frac{iq}{\hbar}\oint_\gamma A_\mu dx^\mu\right).
\]

Under \(A_\mu\mapsto A_\mu+\partial_\mu\alpha\), the closed-loop Wilson factor is unchanged for a single-valued allowed gauge transform.

For a charged complex carrier \(\psi=R e^{i\theta}\), use

\[
D_\mu\psi=\left(\nabla_\mu-\frac{iq}{\hbar}A_\mu\right)\psi.
\]

The gauge-invariant local phase-gradient channel is \(v_\mu=\partial_\mu\theta-q A_\mu/\hbar\) where \(R\ne0\); the gauge-invariant local energy contains \(R^2g^{\mu\nu}v_\mu v_\nu\).

**Type firewall:** \(W_\gamma\) is global/path-dependent data. It is not identical to \(F_{\mu\nu}\), a local metric source, the spatial SU(2) connection, or the Lorentz spin connection. A nontrivial Wilson loop with \(F=0\) along an accessible path does not by itself demonstrate extra local gravitational stress.

## 4. Minimal variational completion

For a controlled model, take a diffeomorphism- and U(1)-invariant action (in \(c=1\) units)

\[
S=\int d^4x\,\sqrt{-g}\left[
\frac{R-2\Lambda_b}{2\kappa_E}
-\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu}
-\frac12(D_\mu\psi)^*D^\mu\psi
-\frac12 D_\mu\psi(D^\mu\psi)^*
-U(|\psi|^2,\Xi_I)
+\mathcal L_{\rm other}
\right],
\]

where \(\Xi_I\) must be independently typed and source-bound. The two displayed half-kinetic terms sum to the standard real \( -(D_\mu\psi)^*D^\mu\psi\). \(\mathcal L_{\rm other}\) cannot duplicate an already included Maxwell, carrier, or information-scalar source. \(U\) is real and gauge invariant.

A more general historical Lambda0 functional may depend on \(F_{\mu\nu}F^{\mu\nu}\), the phase carrier, and nonlocal holonomy information. Such dependence is a **new action definition** whose full functional variation must be retained; it cannot simply be substituted as an external number in Einstein's equations.

## 5. Exact potential bookkeeping and metric response

If the scalar-potential contribution has no *explicit* metric dependence when its matter fields are held fixed, its stress contribution is

\[
T^{\rm pot}_{\mu\nu}=-U g_{\mu\nu},
\]

and the same source may be placed on the left:

\[
\boxed{G_{\mu\nu}+(\Lambda_b+\Lambda_I)g_{\mu\nu}
=\kappa_E T_{\mu\nu}^{\rm other},\qquad \Lambda_I=\kappa_E U.}
\]

This is an algebraic reassignment only. The potential must NOT simultaneously remain in \(T^{\rm other}_{\mu\nu}\).

If \(U\) depends explicitly on \(g^{\mu\nu}\), its stress acquires \(2\,\partial U/\partial g^{\mu\nu}\), giving

\[
\boxed{G_{\mu\nu}+(\Lambda_b+\kappa_E U)g_{\mu\nu}
-2\kappa_E\frac{\partial U}{\partial g^{\mu\nu}}
=\kappa_E T_{\mu\nu}^{\rm other}.}
\]

For dependence on metric derivatives or nonlocal functionals, replace the simple partial derivative by the **full metric functional derivative**, including integration by parts and boundary data. Do not treat the historical Lambda0 formula as a complete variation in those cases.

## 6. Bianchi compatibility is mandatory

The contracted Bianchi identity yields, for the simple potential-reassigned equation,

\[
\boxed{\partial_\nu(\Lambda_b+\kappa_E U)=
\kappa_E\nabla^\mu T_{\mu\nu}^{\rm other}.}
\]

If the right-hand tensor is separately conserved, \(U\) must be constant on that branch. Variable \(U\) is compatible with total conservation only through exchange with the omitted scalar/phase source terms or another derived modification. On shell, a fully diffeomorphism-invariant total action enforces \(\nabla^\mu T^{\rm total}_{\mu\nu}=0\); no ad hoc source \(S_\nu\) is sufficient without a matching field law.

An intention filter \(I_0\) may be an explicit admissibility constraint for software/experiments. Interpreting it as a physical spacetime source is a separate unverified hypothesis, not a consequence of gauge invariance or the Bianchi identity.

## 7. Relation to the admitted CIR cosmological source ledger

The existing exact, conditional identification is

\[
\Lambda_I=\kappa_E U_I=\alpha_I\Xi_I.
\]

Preserve the source-ledger acceleration criterion and its no-go findings:
- A pure homogeneous phase-kinetic source has \(w=+1\) and does not accelerate expansion.
- Dividing one potential into equal-stress cosine/sine holonomy channels does not add gravitational stress.
- Current temporal holonomy is a spectator of the admitted canonical information-scalar potential.
- The RF-F20 local metric-response candidate requires an independently sourced \(\partial\mathcal A_\beta^{BE}/\partial g^{\mu\nu}\) tensor and sign/scale controls.
- Phase, action scale \(\eta_\phi\), energy-carrier identity, \(D\)-to-metric map and cosmological absolute normalization remain conditional/open.

There is no automatic equation \(\Lambda_0=\Lambda_I\). That historical-to-current identification requires a derived mapping and source accounting.

## 8. Finite falsification and regression controls (proposed, not executed)

1. **Gauge:** compare \(W_\gamma\), \(D_\mu\psi\), and stress before/after a valid U(1) gauge transformation. Invariants must agree.
2. **Flat control:** for vanishing sources, \(U=\Lambda_b=0\), constant carrier, and Minkowski metric, recover \(G_{\mu\nu}=0\).
3. **Constant potential:** recover \(G_{\mu\nu}+\Lambda_I g_{\mu\nu}=\kappa_E T_{\mu\nu}^{\rm other}\) exactly, with no double counting.
4. **Metric-dependent potential:** compare an independently derived variation to the added \(-2\kappa_E\partial U/\partial g^{\mu\nu}\) term.
5. **Conservation:** compute the Bianchi residual \(\mathcal B_\nu:=\partial_\nu\Lambda_{\rm eff}-\kappa_E\nabla^\mu T^{\rm other}_{\mu\nu}\), require zero within declared tolerance on solutions.
6. **Aharonov–Bohm control:** compare equal local \(F\) along two test paths with different enclosed flux / Wilson factors. Predict the known phase difference; do NOT infer curvature unless a separately varied source produces it.
7. **ADM:** evaluate Hamiltonian/momentum constraints for any candidate spacetime metric; retain all upstream physical-source gates.
8. **Existing ledger:** preserve the equal-stress repartition, pure-phase \(w=1\), observational no-retune, and non-double-count no-go results.

No fresh CI/test run or empirical verification is claimed by this note. No change to main CLAIM_STATUS is justified until explicit validation receipts and parent dependencies are added.

## 9. Decision

**Mathematical bridge:** coherent gauge-covariant research construction under the declared action and ADM premises.  
**Metric/dynamical completion:** conditional; requires source-bound variation and Bianchi-compatible evolution.  
**Physical phase-induced gravity:** OPEN / UNVERIFIED.  
**Production/observational promotion:** NOT ADMITTED.

This file is an isolated research candidate on a post-consolidation branch, not a revision of the already validated CIR main foundation.
