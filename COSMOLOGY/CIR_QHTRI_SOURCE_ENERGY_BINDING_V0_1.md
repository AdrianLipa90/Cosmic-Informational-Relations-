# CIR QHTRI Source-Energy / Hamiltonian Phase Binding v0.1

Status: EXACT RFC MATERIAL-HAMILTONIAN LIFT / QHTRI DYNAMICAL-PHASE SOURCE ADMISSION CONDITIONAL / FULL-ACTION DOUBLE-COUNT FIREWALL  
Date: 2026-10-04

## 1. Purpose

This gate asks one question:

> What energy is allowed to appear in the QHTRI dynamical phase law when the source is imported from the RFC/GREMLIN relational-generator sector?

The answer must distinguish:

1. local generator Hamiltonian per occupation;
2. local energy density;
3. finite-slice extensive energy;
4. Euler/Noether Hamiltonian;
5. QHTRI dynamical phase energy;
6. the full first-order canonical action.

These objects are related, but they are not identical by notation.

No cosmological target is used in this gate.

## 2. RFC local Hamiltonian

RF-F13 defines

\[
X:=\Phi_C+\kappa,
\qquad
P:=BX,
\qquad
\dot X=\omega,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

On the admitted degree-one Hamiltonian surface,

\[
\boxed{
H_G=P\omega=B\omega X.
}
\]

Thus the RFC relational-generator energy per occupied material element is the on-shell material Hamiltonian.

RF-S16 writes the same source density as

\[
\rho_G
=
\frac{\mathcal N}{V_R}
B\omega X.
\]

Therefore

\[
\boxed{
\rho_G
=
\frac{\mathcal N}{V_R}H_G.
}
\]

For cell \(a\),

\[
\boxed{
E_a
:=
V_a\rho_{G,a}
=
\mathcal N_aH_{G,a}.
}
\]

For a finite source slice \(\Sigma\),

\[
\boxed{
E_\Sigma
:=
\sum_aV_a\rho_{G,a}
=
\sum_a\mathcal N_aH_{G,a}.
}
\]

This identity is exact on the admitted RFC source cells. It does not require the RF-S22 matched-H premise.

## 3. RF-S22 matched-H branch

RF-S22 introduces the conditional extensive closure

\[
\boxed{
E_G=H_\Phi^{EB}.
}
\]

On the branch where \(E_G\) is the same integrated relational-generator source as \(E_\Sigma\),

\[
\boxed{
E_\Sigma=H_\Phi^{EB}.
}
\]

This is an exact consequence after the matched-H input is admitted.

It is not an upstream theorem of RF-F13 alone. RF-S22 explicitly retains

\[
\text{physical }H_\Phi^{EB}
\leftrightarrow
\text{generator-source energy}
\]

as an OPEN physical receipt.

Therefore CIR must preserve the status:

\[
E_\Sigma=H_\Phi^{EB}
\quad
\text{CONDITIONAL / MATCHED-H},
\]

not unconditional identity.

## 4. QHTRI dynamical phase

The QHTRI phase-mechanics interface is

\[
S_Q^{\rm dyn}
=
-\int E_Q\,dt,
\qquad
\Phi_Q
=
\frac{S_Q^{\rm dyn}}{\eta_\phi},
\]

hence

\[
\boxed{
\dot\Phi_Q
=
-\frac{E_Q}{\eta_\phi}.
}
\]

Here \(E_Q\) must be the energy of the carrier whose dynamical phase is being computed.

The minimal typed source admission is

\[
\boxed{
\texttt{QHTRI\_DYNAMICAL\_GENERATOR}
=
\texttt{RFC\_MATERIAL\_HAMILTONIAN}.
}
\]

Only after this carrier-identity premise may one set

\[
\boxed{
E_Q=E_\Sigma.
}
\]

Then

\[
\boxed{
\dot\Phi_Q
=
-\frac{E_\Sigma}{\eta_\phi}
=
-\frac1{\eta_\phi}
\sum_a\mathcal N_aH_{G,a}.
}
\]

This is not a fit coefficient. It is a discrete source-selection premise: either QHTRI uses this Hamiltonian or it does not.

## 5. Full-action firewall

RF-F13 uses the first-order material action

\[
S_G^{(1)}
=
\int dt\,
\left(
P\dot X-H_G
\right).
\]

But the same admitted surface has

\[
\dot X=\omega
\]

and

\[
H_G=P\omega.
\]

Therefore on shell,

\[
\boxed{
P\dot X-H_G=0.
}
\]

Hence

\[
\boxed{
S_G^{(1)}\big|_{\rm on-shell}
=0
}
\]

for this degree-one material block.

Therefore the following naive identification is forbidden:

\[
S_Q^{\rm dyn}
=
S_G^{(1)}.
\]

It would erase the nontrivial dynamical phase.

The correct separation is

\[
\boxed{
S_{\rm dyn}
=
-\int H_G\,dt
}
\]

for the dynamical phase channel, while

\[
\boxed{
\Theta_G=P\,dX
}
\]

is the canonical/geometric one-form channel.

A later total phase may contain both dynamical and geometric/holonomic contributions, but they must not be collapsed or counted twice.

## 6. Single-rate phase/action relation

For one occupied element, or a coherent branch on which one common \((P,\omega)\) describes the phase carrier,

\[
E_Q=H_G=P\omega,
\qquad
\dot X=\omega.
\]

Then

\[
\boxed{
\dot\Phi_Q
=
-\frac{P}{\eta_\phi}\dot X.
}
\]

If

\[
r_\eta:=\frac{P}{\eta_\phi}
\]

is constant on the segment, integration gives

\[
\boxed{
\Phi_Q
=
-r_\eta X+\Phi_{Q,0}.
}
\]

Thus the dynamical-phase map is controlled by an action ratio, not by an arbitrary cosmological coefficient.

## 7. U(1) phase-bundle compatibility

Consider the wrapped RFC canonical phase

\[
u_X=e^{iX}
\]

and wrapped QHTRI dynamical phase

\[
u_Q=e^{i\Phi_Q}.
\]

If the map is required to be a continuous group homomorphism \(U(1)\to U(1)\), then

\[
\boxed{
r_\eta\in\mathbb Z.
}
\]

The map has degree

\[
\boxed{
d_{X\to Q}=-r_\eta.
}
\]

If it is required to be an isomorphism and \(\eta_\phi>0\), then

\[
\boxed{
r_\eta=1,
\qquad
\eta_\phi=P,
\qquad
d_{X\to Q}=-1.
}
\]

Therefore the natural same-bundle dynamical-phase isomorphism is orientation reversing because the dynamical phase carries the standard minus sign

\[
S_{\rm dyn}=-\int H\,dt.
\]

This sign is derived from the action convention, not selected from cosmological data.

### Globality firewall

If \(\eta_\phi\) is fixed while \(P(t)\) varies, then \(r_\eta=P/\eta_\phi\) varies and the simple global \(U(1)\) homomorphism above does not exist.

One must then use one of:

- a local/piecewise registry;
- a varying effective action scale with its own physical law;
- a more general bundle connection rather than a fixed-degree phase homomorphism.

## 8. Candidate identification \(\eta_\phi=q_0\)

RF-F14 proves that, on the physical Noether-current binding, \(q_0\) has action type.

Therefore

\[
\eta_\phi=q_0
\]

is dimensionally admissible as a candidate carrier-action identification.

It is not automatic, because RF-S17 retains positive carrier-normalization freedom until a physical branch fixes the absolute carrier unit.

Under this candidate,

\[
r_\eta
=
\frac{P}{q_0}.
\]

RF-F14 supplies the exact sector table:

| sector | \(P/q_0\) | RF-F8 required \(d\ln|P|/d\ln|\omega|\) | direct \(U(1)\) status for \(\eta_\phi=q_0\) |
|---|---:|---:|---|
| normal phase kinetic | \(1/2\) | \(2\) | not a standard integer-degree \(U(1)\) map |
| isotropic null radiation | \(1\) | \(0\) | orientation-reversing isomorphism |
| homogeneous radiation completion | \(3/4\) | \(0\) | not a standard integer-degree \(U(1)\) map |
| homogeneous dust | \(1\) | \(-1\) | pointwise isomorphism; fixed-\(q_0\) global map fails if \(\omega\) varies |
| potential vacuum boundary | degenerate | \(-4\) effective | current-ratio phase map unavailable |

## 9. Conditional branch-selector theorem

Assume all of the following:

1. QHTRI uses the RFC generator Hamiltonian;
2. \(\eta_\phi=q_0\);
3. \(q_0\) is a fixed carrier action unit;
4. the RFC \(X\)-phase and QHTRI dynamical phase are related by one global \(U(1)\) isomorphism;
5. the branch follows the RF-F8 varying-\(\omega\) phase-cell transport law.

A global isomorphism requires

\[
P/q_0=1
\]

and a fixed \(q_0=P\) along the transport branch requires

\[
\frac{d\ln|P|}{d\ln|\omega|}=0.
\]

Among the RF-F14 branch matrix, the unique branch satisfying both is

\[
\boxed{
\text{ISOTROPIC NULL RADIATION}.
}
\]

This is a conditional selector theorem. It does not prove that the physical cosmological carrier occupies that sector.

In particular, the dust branch satisfies \(P/q_0=1\) pointwise but requires

\[
P\propto|\omega|^{-1},
\]

so it cannot retain \(P=q_0=\) constant during nontrivial varying-\(\omega\) transport.

## 10. CIR composition

CIR gives

\[
H_D
=
\kappa\dot\Phi_D.
\]

The CIR/QHTRI phase-registry gate gives, for a degree-\(m\) registry,

\[
\dot\Phi_D
=
m\dot\Phi_Q.
\]

After the RFC material-Hamiltonian source admission,

\[
\boxed{
H_D
=
-\frac{\kappa m}{\eta_\phi}E_\Sigma.
}
\]

On the RF-S22 matched-H branch this becomes

\[
\boxed{
H_D
=
-\frac{\kappa m}{\eta_\phi}H_\Phi^{EB}.
}
\]

Both equations remain conditional on the physical source and phase-bundle admissions.

No identification with \(H_{\rm FLRW}\) follows until \(D\) is physically bound to a cosmological metric or observable.

## 11. What is closed now

### EXACT / STRUCTURAL

\[
H_G=P\omega=B\omega X,
\]

\[
\rho_G=(\mathcal N/V)H_G,
\]

\[
E_\Sigma=\sum_aV_a\rho_{G,a}=\sum_a\mathcal N_aH_{G,a},
\]

\[
P\dot X-H_G=0
\quad\text{on the RF-F13 degree-one shell},
\]

and therefore the full first-order action must not be substituted for the QHTRI dynamical action.

### EXACT CONDITIONAL

\[
E_\Sigma=H_\Phi^{EB}
\]

on RF-S22 matched-H;

\[
E_Q=E_\Sigma
\]

after the typed QHTRI/RFC same-generator admission;

\[
\eta_\phi=P
\]

if a fixed-degree orientation-reversing \(U(1)\) isomorphism between \(X\) and the QHTRI dynamical phase is required on a constant-ratio segment.

### OPEN PHYSICAL BINDING

- whether QHTRI actually uses the RFC material Hamiltonian;
- whether RF-S22 matched-H is physically realized;
- the physical action quantum / normalization behind \(\eta_\phi\);
- whether the relevant phase registry is global \(U(1)\), local, or connection-valued;
- which RF-F14 sector is physically realized;
- \(D\leftrightarrow\) cosmological metric/observable.

## 12. No-fit and no-double-count rules

Forbidden:

- choosing \(E_Q\) after inspecting \(H_0\);
- choosing \(\eta_\phi\) to reproduce a desired cosmic rate;
- setting \(S_Q=S_G^{(1)}\) and simultaneously retaining \(-\int H_Gdt\);
- counting \(P\,dX\) as both a geometric phase and again inside the dynamical phase;
- promoting RF-S22 matched-H to an unconditional identity;
- using a noninteger \(P/\eta_\phi\) as a standard \(U(1)\) homomorphism without an explicitly enlarged covering/bundle structure;
- using the RF-F14 conditional branch selector as evidence that nature realizes the selected sector.

## 13. Parent provenance

- RFC main: \`664349e2f16b57ee23bf6f5f21f5fe8ada17c5a5\`.
- RFC RF-F13: \`formalism/RF_F13_VARIATIONAL_INTEGRABILITY_COMMON_ACTION.md\`.
- RFC RF-S16: \`closure/scale/RF_S16_OCCUPATION_NOETHER_CURRENT_BINDING.md\`.
- RFC RF-S17: \`closure/scale/RF_S17_CARRIER_NORMALIZATION_INVARIANCE.md\`.
- RFC RF-S22: \`closure/scale/RF_S22_NOETHER_HAMILTONIAN_SOURCE_CLOSURE.md\`.
- RFC RF-F14: \`formalism/RF_F14_NOETHER_EOS_SECTOR_COMPATIBILITY.md\`.
- QHTRI current main: \`f95589ff1c7e5e7cee6b1bcaf079c3c3eb4fc500\`.
- QHTRI phase mechanics: \`docs/PHASE_MECHANICS_GREMLIN_ORBITAL_EB_BRIDGE.md\`.
- GREMLIN v0.8/v0.9 preserve source/coupling and physical-realization firewalls.
- CIR parent gates:
  - \`CIR_PHASE_REGISTRY_GATE_V0_1.md\`;
  - \`CIR_DENSITY_TO_POTENTIAL_GATE_V0_1.md\`.

Live GREMLIN/PhaseNav multi-source red-team receipt was generated before this gate was written.
