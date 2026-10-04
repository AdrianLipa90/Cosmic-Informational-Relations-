# CIR Density-to-Potential / Carrier-Energy Gate v0.1

Status: EXACT TYPE SEPARATION / EXACT CELL-INTEGRATION IDENTITY / PHYSICAL QHTRI ACTION BINDING OPEN  
Date: 2026-10-04

## 1. Purpose

The source-density branch and the QHTRI phase-action branch use different typed objects.

RFC/GREMLIN carries a local source density

\[
\rho_G
=
\frac{B\omega\mathcal N}{V_R}
(\phi+\kappa),
\qquad
V_R=AR,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

QHTRI phase mechanics uses an action phase

\[
\Phi_Q=\frac{S_Q}{\eta_\phi}.
\]

For an ordinary action scale \(\eta_\phi\), the local rate law

\[
\dot\Phi_Q=-\frac{E_Q}{\eta_\phi}
\]

requires an extensive energy \(E_Q\), not an energy density.

This gate derives the admissible density-to-energy map and separates it from a distinct local action-density phase law.

## 2. RFC current-factorized source density

RF-S16 gives the exact finite-cell occupation/current binding

\[
j_{Q,a}=q_0\frac{\mathcal N_a}{V_a},
\]

and the energy per conserved carrier charge

\[
\epsilon_{Q,a}
=
\frac{B_a\omega_a}{q_0}
(\phi_a+\kappa).
\]

Therefore

\[
\boxed{
\rho_{G,a}
=
\epsilon_{Q,a}j_{Q,a}
=
\frac{B_a\omega_a\mathcal N_a}{V_a}
(\phi_a+\kappa).
}
\]

This is an exact source-density identity on the admitted RFC cell.

## 3. Cell-integration theorem

Multiply the local density by the same cell volume:

\[
E_a:=V_a\rho_{G,a}.
\]

Substitution gives

\[
\begin{aligned}
E_a
&=
V_a
\frac{B_a\omega_a\mathcal N_a}{V_a}
(\phi_a+\kappa)\\
&=
\boxed{
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\end{aligned}
\]

Equivalently through the current representation,

\[
E_a
=
V_a\epsilon_{Q,a}j_{Q,a}
=
V_a
\frac{B_a\omega_a}{q_0}(\phi_a+\kappa)
q_0\frac{\mathcal N_a}{V_a},
\]

so both \(V_a\) and \(q_0\) cancel:

\[
\boxed{
E_a
=
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

This cancellation is cellwise. It does not require all cells to be homogeneous or to share the same \(B,\omega,\mathcal N,\phi\).

## 4. Multi-cell extensive source

For a finite admitted cell set \(\mathcal C\),

\[
E_\Sigma:=\sum_{a\in\mathcal C}V_a\rho_{G,a}.
\]

Hence

\[
\boxed{
E_\Sigma
=
\sum_{a\in\mathcal C}
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

A weighted or partial response may be represented by fixed source-owned dimensionless weights \(c_a\):

\[
\boxed{
E_{\rm eff}
=
\sum_{a\in\mathcal C}
c_aV_a\rho_{G,a}
=
\sum_{a\in\mathcal C}
c_aB_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

The weights must be determined by the physical support/kernel before evaluating a cosmological target. They are not fit coefficients.

## 5. Independent RFC confirmation

RF-I1 and RF-E17 already use the same typed pattern for the information-scalar action sector:

\[
U_{\rm clk}
=
\frac{\alpha_{\rm clk}}{\kappa_E}
\Xi_{\rm phase},
\]

followed, on a homogeneous cell, by

\[
\boxed{
H_{\rm clk}
=
V_{\rm cell}U_{\rm clk}.
}
\]

Thus RFC itself distinguishes the local scalar-potential density appearing in the action density from the integrated cell-energy coordinate.

RF-L2 likewise places \(U_L\) inside a spacetime Lagrangian density and obtains

\[
T^{\rm pot}_{\mu\nu}=-U_Lg_{\mu\nu}.
\]

Therefore a local RFC \(U_I\) or \(\rho_G\) must not be silently inserted into a single-carrier action-phase law whose denominator is an ordinary action.

## 6. QHTRI carrier-action branch

QHTRI defines

\[
S_Q[C]=-\int_CE_Q(t)\,dt,
\qquad
\Phi_Q=\frac{S_Q}{\eta_\phi}.
\]

Hence

\[
\boxed{
\dot\Phi_Q=-\frac{E_Q}{\eta_\phi}.
}
\]

If the physically admitted QHTRI source energy is the RFC extensive source over support \(\mathcal C\),

\[
E_Q=E_{\rm eff},
\]

then

\[
\boxed{
\dot\Phi_Q
=
-\frac1{\eta_\phi}
\sum_a
c_aB_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

For the unweighted exact same-cell sum \(c_a=1\),

\[
\boxed{
\dot\Phi_Q
=
-\frac1{\eta_\phi}
\sum_a
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

The disappearance of \(AR\) is therefore not an assumption. It follows from integrating the same local density over the same RFC source cell.

## 7. Composition with the CIR phase registry

The phase-registry gate gives

\[
\dot\Phi_D=m\dot\Phi_Q,
\qquad
m\in\mathbb Z
\]

for a continuous \(U(1)\) homomorphism, and \(m=1\) on the orientation-preserving isomorphism branch.

Because

\[
H_D:=\frac{d\ln D}{dt}=\kappa\dot\Phi_D,
\]

the extensive-source branch gives

\[
\boxed{
H_D
=
-\frac{\kappa m}{\eta_\phi}
\sum_a
c_aB_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

For the orientation-preserving same-phase registry and unweighted same-cell support,

\[
\boxed{
H_D
=
-\frac{\kappa}{\eta_\phi}
\sum_a
B_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

This is a conditional source-to-log-scale equation. It contains no fitted \(H_0\).

## 8. Local field-phase branch is a different theory object

A genuinely local phase field may instead be postulated with an action-density scale \(\eta_\phi^{(V)}\):

\[
\boxed{
\partial_t\Phi_Q(x)
=
-\frac{\rho_G(x)}{\eta_\phi^{(V)}}.
}
\]

This is dimensionally distinct from

\[
\dot\Phi_Q=-E_Q/\eta_\phi.
\]

The two laws coincide only after a declared support-volume relation, for example

\[
\eta_\phi^{(V)}
=
\frac{\eta_\phi}{V_{\rm eff}}
\]

under the corresponding homogeneous-support assumptions.

Therefore the following substitution is forbidden without retyping:

\[
U_{\rm QHTRI}\leftarrow\rho_G.
\]

A density can drive a local phase only with a density-compatible action scale or after explicit integration to an energy.

## 9. Geometry/support kernel

The most general finite-cell bridge needed at this stage is

\[
E_Q
=
\sum_a
c_aV_a\rho_{G,a}.
\]

Here \(c_a\) may encode a source-owned support fraction, response kernel, orientation projection, or other dimensionless admission factor.

This preserves the source-volume role:

- \(V_a\) matters locally in \(\rho_{G,a}\);
- the same \(V_a\) cancels for complete integration of that cell;
- incomplete or weighted support survives only through independently defined \(c_a\), not through an arbitrary replacement of \(AR\).

## 10. Relation to the information-scalar potential

RFC separately provides

\[
U_I
=
\frac{\alpha_I}{\kappa_E}\Xi_I.
\]

On a physical support \(\Omega\), the corresponding extensive information-potential energy is

\[
\boxed{
E_I[\Omega]
=
\int_\Omega U_I\,dV
=
\frac{\alpha_I}{\kappa_E}
\int_\Omega\Xi_I\,dV.
}
\]

Therefore the QHTRI phase-action interface may consume either:

1. a source-generator extensive energy \(E_\Sigma=\int\rho_GdV\), if that source is physically admitted; or
2. an information-scalar extensive energy \(E_I=\int U_IdV\), if that action sector is physically admitted.

These are separate source routes. Their equality is not assumed.

## 11. Identifiability consequence

Integrating the source density removes the explicit volume denominator but does not identify the remaining factors.

For one cell,

\[
E_a
=
B_a\omega_a\mathcal N_aX_a,
\qquad
X_a:=\phi_a+\kappa.
\]

In positive logarithmic coordinates for \(|X_a|>0\),

\[
\ln|E_a|
=
\ln B_a+\ln|\omega_a|+\ln\mathcal N_a+\ln|X_a|.
\]

Thus an \(E_a\)-only observable still identifies only one product unless independent source receipts fix the constituent coordinates.

The volume cancellation is a type conversion, not an identifiability miracle.

## 12. Physical promotion gates

The following remain OPEN:

1. **QHTRI_SOURCE_ENERGY_BINDING** — prove which RFC extensive source, if any, enters the QHTRI carrier action.
2. **SUPPORT_KERNEL_SELECTION** — fix \(\mathcal C\) and \(c_a\) from source geometry/physics.
3. **ACTION_SCALE_CALIBRATION** — derive or independently calibrate \(\eta_\phi\).
4. **PHASE_REGISTRY_SELECTION** — physically select the \(U(1)\) registry degree/orientation.
5. **CIR_METRIC_OBSERVABLE_BINDING** — bind \(D\) to a cosmological metric/observable before interpreting \(H_D\) as a measured Hubble-like rate.

## 13. No-fit firewall

Forbidden:

- using \(H_0\) to determine \(\eta_\phi\);
- using a target redshift to choose \(c_a\) or the support region;
- inserting \(\rho_G\) into an ordinary action-phase law without integration/retyping;
- interpreting cancellation of \(AR\) as proof that physical geometry is irrelevant;
- identifying \(E_\Sigma\) with the QHTRI action energy merely because their dimensions agree.

## 14. Verdict

EXACT ON DECLARED RFC CELLS:

\[
\rho_{G,a}
=
\frac{B_a\omega_a\mathcal N_a}{V_a}(\phi_a+\kappa),
\]

\[
\boxed{
V_a\rho_{G,a}
=
B_a\omega_a\mathcal N_a(\phi_a+\kappa),
}
\]

\[
\boxed{
E_\Sigma
=
\sum_aB_a\omega_a\mathcal N_a(\phi_a+\kappa).
}
\]

CONDITIONAL EXACT AFTER QHTRI ACTION ADMISSION:

\[
\boxed{
H_D=-\frac{\kappa m}{\eta_\phi}E_Q.
}
\]

OPEN:

\[
E_Q
\stackrel{?}{=}
E_\Sigma
\quad\text{or}\quad
E_I[\Omega]
\quad\text{or another independently derived source energy}.
\]

That open equality is now the precise physical density-to-potential gate.

## 15. Parent provenance

- CIR phase/log-scale branch: \`formalize/source-phase-logscale-identifiability-v0.1-20261004\`.
- RFC source/current parent: \`closure/scale/RF_S16_OCCUPATION_NOETHER_CURRENT_BINDING.md\`.
- RFC common-action parent: \`formalism/RF_F13_VARIATIONAL_INTEGRABILITY_COMMON_ACTION.md\`.
- RFC information-potential parent: \`closure/lambda0/RF_L3_INFORMATION_SCALAR_POTENTIAL_RECONSTRUCTION.md\`.
- RFC explicit cell-integration parent: \`closure/einstein/RF_E17_CLOCK_INFORMATION_SCALAR_ACTION_POTENTIAL.md\` and \`closure/information/RF_I1_PHASE_RATE_INFORMATION_CURVATURE_BINDING.md\`.
- QHTRI action-phase parent: \`docs/PHASE_MECHANICS_GREMLIN_ORBITAL_EB_BRIDGE.md\`.
