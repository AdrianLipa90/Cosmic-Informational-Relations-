# CIR AB matter-mediated stress diagnostic v0.2

Date: 2026-11-15

Status: CONDITIONAL MATHEMATICAL TOY / REGRESSION VALIDATED LOCALLY / PHYSICAL SOURCE OPEN

Parent: CIR_LAMBDA0_RDSS_AB_VARIATIONAL_BRIDGE_CANDIDATE_V0_1.md
Preserve CIR_COSMOLOGICAL_SOURCE_LEDGER_V0_1.md no-go results and CLAIM_STATUS.

## Charged phase matter on a ring

Consider a ring of circumference \(L>0\), transverse area \(A>0\), positive scalar-phase stiffness \(f^2\), and dimensionless electromagnetic Wilson angle \(\varphi\).

\[
W_\gamma=e^{i\varphi},\qquad
\varphi=\frac q\hbar\oint_\gamma A_\mu dx^\mu,\qquad
F_{\mu\nu}|_{\rm accessible\ path}=0.
\]

A charged constant-modulus phase matter field has integer winding \(m\) and gauge-covariant mismatch \(\delta_m=2\pi m-\varphi\).

\[
E_m=\frac{f^2 A}{2L}\delta_m^2,\qquad
\rho_m=\frac{E_m}{AL}=\frac{f^2\delta_m^2}{2L^2}.
\]

The phase-dependent matter energy is nonzero at nontrivial Wilson phase even if the local electromagnetic curvature vanishes along the accessible path. It is the dynamical *charged field* that supplies stress; an isolated Wilson factor is not itself a local gravitational source. The inaccessible flux core and boundary conditions must be included for a complete physical device.

For \(N\) lattice nodes with \(\psi_j\) complex and link angle \(a_j\),

\[
E_N=\frac{f^2 A N}{2L}\sum_{j=0}^{N-1}
|\psi_{j+1}-e^{ia_j}\psi_j|^2.
\]

Gauge transformation \(\psi_j\to e^{i\chi_j}\psi_j\), \(a_j\to a_j+\chi_{j+1}-\chi_j\) leaves \(E_N\) and the closed Wilson factor invariant. For uniform winding and flux,

\[
E_N=\frac{f^2 A N^2}{L}
[1-\cos((2\pi m-\varphi)/N)]\xrightarrow{N\to\infty} E_m.
\]

The minimizing winding changes at half-integral flux quanta. Derivatives of the minimum energy are not defined at such degeneracy points; all derivative tests choose a fixed winding branch away from a cusp.

## Stress is anisotropic, not a cosmological constant

In a flat \((-+++)\) local frame for the restricted static scalar-phase kinetic action \(\mathcal L=-\frac12 f^2 g^{\mu\nu}v_\mu v_\nu\) and \(v_\mu=(0,\delta_m/L,0,0)\),

\[
T_{\mu\nu}=\mathrm{diag}(\rho,\rho,-\rho,-\rho),\quad
T^\mu{}_\nu=\mathrm{diag}(-\rho,\rho,-\rho,-\rho).
\]

Mechanical derivatives agree with the tensor:

\[
p_\parallel=-\frac1A\frac{\partial E_m}{\partial L}=\rho,\qquad
p_\perp=-\frac1L\frac{\partial E_m}{\partial A}=-\rho.
\]

The active combination \(\rho+p_\parallel+2p_\perp=0\), and an isotropic arithmetic average gives \(w=-1/3\), not \(w=-1\). This is a *restricted toy*, not a homogeneous-isotropic Einstein solution, not dark energy and not an empirical gravity prediction.

## Regression and physical gates

Test code:
- validation/cir_lambda0_ab_ring_v0_2.py
- validation/test_cir_lambda0_ab_ring_v0_2.py
- validation/cir_lambda0_ab_reference_v0_1.py
- validation/test_cir_lambda0_ab_reference_v0_1.py

Run from repository root: python -m unittest discover -s validation -p 'test_cir_lambda0_ab_*py' -v

The expected new ring suite consists of 22 tests and the earlier reference suite of 27 tests: 49 total. Additional reference algebra controls are separately tracked. The tests establish algebra and discretization properties only; production source identity, Einstein backreaction, complete electromagnetic/core stress, global boundaries, coupled Bianchi conservation, action-scale calibration and observations remain OPEN.

Do not identify EM U(1) with Berry U(1), spatial SU(2) or Lorentz spin holonomy without a typed map and source evidence; do not double count Maxwell contributions.
