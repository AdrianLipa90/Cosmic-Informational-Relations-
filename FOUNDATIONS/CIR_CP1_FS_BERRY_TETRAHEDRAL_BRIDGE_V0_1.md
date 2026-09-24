# CIR CP1 / Fubini--Study / Berry / Tetrahedral Bridge v0.1

Status: `EXACT_STATE_GEOMETRY / EXACT_TETRAHEDRAL_CROSSWALK / PHYSICAL_SPATIAL_PROMOTION_OPEN`

Parent TIR commit: `853032e019824b836de43634d949da5566396153`

## 1. Purpose

This file isolates the exact mathematical chain from the pure two-state quantum carrier to the tetrahedral relational seed. It does not identify state-space curvature with physical spacetime curvature.

The typed chain is

\[
\mathbb C^2
\longrightarrow
\mathbb{CP}^1
\cong
S^2_{\rm Bloch}
\longrightarrow
(g_{\rm FS},F_{\rm B})
\longrightarrow
\{\mathbf n_a\}_{a=1}^4
\longrightarrow
{\rm Herm}_0(2)\cong\mathbb R^3.
\]

The last arrow is the Bloch/Pauli coefficient representation. Promotion of this internal relational carrier to physical tangent geometry is a separate gate.

## 2. Pure-state coordinate and Bloch map

For a normalized pure qubit state

\[
|\psi(\theta,\phi)\rangle
=
\cos\frac{\theta}{2}|0\rangle
+
e^{i\phi}\sin\frac{\theta}{2}|1\rangle,
\]

the ray determines

\[
\rho=|\psi\rangle\langle\psi|
=
\frac12\left(I+\mathbf n\cdot\boldsymbol\sigma\right),
\]

with

\[
\mathbf n
=
(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),
\qquad
\|\mathbf n\|=1.
\]

Hence

\[
\boxed{
2\rho-I=\mathbf n\cdot\boldsymbol\sigma
\in{\rm Herm}_0(2).
}
\]

The Hilbert--Schmidt metric on the traceless Hermitian carrier satisfies

\[
\boxed{
\frac12{\rm Tr}\left[
(\mathbf n\cdot\boldsymbol\sigma)
(\mathbf m\cdot\boldsymbol\sigma)
\right]
=
\mathbf n\cdot\mathbf m.
}
\]

Thus the Bloch coefficient vector and the real three-dimensional Pauli carrier carry the same normalized Euclidean inner product.

## 3. Fubini--Study geometry

With the standard qubit normalization,

\[
\boxed{
ds_{\rm FS}^2
=
\frac14
\left(
d\theta^2+\sin^2\theta\,d\phi^2
\right).
}
\]

Therefore the Fubini--Study area form is

\[
\boxed{
\omega_{\rm FS}
=
\frac14\sin\theta\,d\theta\wedge d\phi.
}
\]

The total Fubini--Study area of \(\mathbb{CP}^1\) is

\[
\int_{\mathbb{CP}^1}\omega_{\rm FS}=\pi.
\]

This is projective state-space geometry.

## 4. Berry curvature

For the displayed spinor gauge one may take

\[
A_{\rm B}
=
-\sin^2\frac{\theta}{2}\,d\phi,
\]

so

\[
\boxed{
F_{\rm B}
=
dA_{\rm B}
=
-\frac12\sin\theta\,d\theta\wedge d\phi
=
-2\omega_{\rm FS}.
}
\]

The overall sign changes with state/orientation convention. The invariant magnitude relation is

\[
\boxed{
|F_{\rm B}|=2\,\omega_{\rm FS}
}
\]

in this normalization.

For a closed loop enclosing Bloch-sphere solid angle \(\Omega\),

\[
\boxed{
\gamma_{\rm B}=-\frac{\Omega}{2}\pmod{2\pi}.
}
\]

The full sphere carries Berry flux magnitude \(2\pi\), corresponding to first Chern number magnitude one.

## 5. Qubit SIC tetrahedron

Let four unit Bloch vectors satisfy

\[
\boxed{
\mathbf n_a\cdot\mathbf n_b=-\frac13
\quad(a\neq b),
\qquad
\sum_{a=1}^4\mathbf n_a=0.
}
\]

A canonical realization is

\[
\mathbf n_1=\frac1{\sqrt3}(1,1,1),\quad
\mathbf n_2=\frac1{\sqrt3}(1,-1,-1),
\]

\[
\mathbf n_3=\frac1{\sqrt3}(-1,1,-1),\quad
\mathbf n_4=\frac1{\sqrt3}(-1,-1,1).
\]

These are the four Bloch directions of a qubit SIC and a regular tetrahedral frame in the Pauli coefficient carrier.

The Euclidean edge length is

\[
\boxed{
\hat a=\sqrt{\frac83}.
}
\]

The normalized Euclidean volume is

\[
\boxed{
\hat V_{\Delta^3}=\frac{8}{9\sqrt3}.
}
\]

## 6. Geodesic tetrahedral face

For two distinct vertices the Bloch-sphere central angle \(\chi\) obeys

\[
\cos\chi=-\frac13.
\]

A geodesic spherical face is equilateral. Its interior angle is

\[
\boxed{
\alpha=\frac{2\pi}{3}.
}
\]

Its unit-sphere solid angle is therefore

\[
\boxed{
\Omega_{\rm face}=3\alpha-\pi=\pi.
}
\]

Because the Fubini--Study metric is one quarter of the unit-sphere metric,

\[
\boxed{
A_{\rm FS}^{\rm face}=\frac{\pi}{4}.
}
\]

For the four faces,

\[
\boxed{
A_{\rm FS}^{\rm tet}=\pi.
}
\]

The Berry phase around one consistently oriented face is

\[
\boxed{
\gamma_{\rm B}^{\rm face}
=
-\frac{\pi}{2}
\pmod{2\pi}
}
\]

for the sign convention of Section 4. Reversing orientation reverses the sign.

This gives an exact projective loop-holonomy associated with each tetrahedral face.

## 7. Exact dual-shape coefficient

The parent TIR crosswalk defines

\[
\boxed{
C_{\Delta/{\rm FS}}
=
\frac{\hat V_{\Delta^3}}{A_{\rm FS}^{\rm tet}}
=
\frac{8}{9\sqrt3\,\pi}.
}
\]

This is dimensionless and is not a physical length scale.

## 8. Relation carrier

For two pure-state endpoints \(x,y\),

\[
\boxed{
\mathcal E_{xy}
=
2(\rho_y-\rho_x)
=
(\mathbf n_y-\mathbf n_x)\cdot\boldsymbol\sigma
\in{\rm Herm}_0(2).
}
\]

Thus tetrahedral state data generate a finite set of exact affine relation vectors in the internal real three-dimensional carrier.

This is the correct foundation for the downstream TIR spatial relation graph.

## 9. Two holonomies must remain distinct

The Berry transport belongs to a state-space \(U(1)\) line bundle. Denote it here by

\[
W_{ij}^{\rm B}\in U(1).
\]

The TIR spatial frame transport is instead

\[
W_{ij}^{X}\in SU(2),
\qquad
R_{ij}={\rm Ad}_{W_{ij}^{X}}\in SO(3).
\]

Therefore

\[
\boxed{
W_{ij}^{\rm B}\neq W_{ij}^{X}
\quad\text{by type unless an explicit promotion map is supplied.}
}
\]

A Berry phase is not automatically spatial curvature.

## 10. Poincare firewall

The following geometries are not identical:

\[
\mathbb{CP}^1\simeq SU(2)/U(1)\simeq S^2
\]

and

\[
\mathbb D\simeq SU(1,1)/U(1).
\]

The first is compact projective/Bloch geometry; the second is the non-compact hyperbolic Poincare disk used by the rapidity branch.

Any bridge between them must be explicit. The tetrahedral SIC construction alone does not identify them.

## 11. Promotion ledger

```text
CP1 = Bloch pure-state sphere                 PASS STANDARD
FS metric and area normalization              PASS STANDARD
Berry curvature / half-solid-angle phase      PASS STANDARD
Berry flux Chern-number magnitude one         PASS STANDARD
qubit SIC -> regular tetrahedral frame         PASS STANDARD
tetra edge/volume identities                   PASS EXACT
tetra FS face area = pi/4                      PASS EXACT
tetra Berry face phase magnitude = pi/2        PASS EXACT
rho -> Herm_0(2) Pauli carrier                 PASS STANDARD
E_xy = 2(rho_y-rho_x) relation vector          PASS TIR PARENT
Berry U(1) = spatial SU(2) connection          NOT IDENTIFIED
CP1/Bloch sphere = hyperbolic Poincare disk    FORBIDDEN
internal relation carrier = physical tangent   OPEN PROMOTION GATE
physical length scale                          OPEN
```

## 12. Parent provenance

Pinned TIR sources:

- `TIR/integration/TIR_TETRA_FS_SPATIAL_SHAPE_CROSSWALK_V0_1.md`
- `TIR/foundations/TIR_MOIRE_HYPERLAYER_GRAVITY_BRIDGE_V0_1.md`
- `TIR/foundations/TIR_SPATIAL_BUNDLE_CONNECTION_V0_1.md`
- `TIR/foundations/TIR_WIJ_HOLONOMY_CROSSWALK_V0_1.md`
