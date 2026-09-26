# CIR Kerr ADM Source-to-Coframe Gate v0.1

Status: STANDARD-GR SOURCE REFERENCE / CIR PHYSICAL BINDING CANDIDATE
Date: 2026-09-26

## Purpose

Provide an upstream black-hole geometry that determines the ADM lapse, shift and spatial triad before any CMB morphology is inspected.

This is the lawful source route required by the GL(3) identifiability firewall.

Geometric units G=c=1 are used in the formulas below.

## Kerr metric in Boyer-Lindquist coordinates

Define

  Sigma = r^2 + a^2 cos^2(theta),

  Delta = r^2 - 2 M r + a^2,

  A = (r^2+a^2)^2 - a^2 Delta sin^2(theta).

Then

  ds^2
  = -(1-2Mr/Sigma) dt^2
    - (4 M a r sin^2(theta)/Sigma) dt dphi
    + (Sigma/Delta) dr^2
    + Sigma dtheta^2
    + (A sin^2(theta)/Sigma) dphi^2.

Reference: standard Kerr/Boyer-Lindquist form; see e.g. Baines et al. arXiv:2009.01397 and standard 3+1 references.

## Exact ADM split

Using

  ds^2 = -alpha^2 dt^2
         + gamma_ij (dx^i + beta^i dt)(dx^j + beta^j dt),

the Boyer-Lindquist Kerr geometry gives

  alpha = sqrt(Delta Sigma / A),

  beta^r = 0,
  beta^theta = 0,
  beta^phi = - 2 M a r / A,

and diagonal spatial metric

  gamma_rr = Sigma/Delta,

  gamma_thetatheta = Sigma,

  gamma_phiphi = A sin^2(theta)/Sigma.

A positive time-gauge spatial triad may therefore be chosen as

  E_Kerr
  = diag(
      sqrt(Sigma/Delta),
      sqrt(Sigma),
      sin(theta) sqrt(A/Sigma)
    ).

The corresponding coframe is

  e^0 = alpha dt,

  e^1 = sqrt(Sigma/Delta) dr,

  e^2 = sqrt(Sigma) dtheta,

  e^3 = sin(theta) sqrt(A/Sigma)
        (dphi + beta^phi dt).

This is exactly of the existing PhaseNav ADM bridge form

  e^0 = N dt,
  e^a = E^a_i (dx^i + beta^i dt).

## Horizon limit

For the outer horizon

  r_+ = M + sqrt(M^2-a^2),

Delta(r_+)=0.

The frame-dragging angular velocity approaches

  omega_H := - beta^phi(r_+)
           = a/(r_+^2+a^2)
           = a/(2 M r_+),

the standard Kerr horizon angular velocity.

The non-extremal surface gravity is

  kappa_H
  = (r_+ - r_-)/(2(r_+^2+a^2)),

with

  r_- = M - sqrt(M^2-a^2).

Thus the source supplies independent horizon scalars kappa_H and omega_H.

## Slow-rotation ordering

At linear order in a/M:

- the lapse alpha is Schwarzschild plus O(a^2);
- the spatial metric gamma_ij is Schwarzschild plus O(a^2);
- beta^phi is O(a).

Therefore the leading rotational/chiral information is carried by the ADM shift, not by a spatial GL(3) strain.

This has a direct CIR consequence:

  leading Kerr-like AoE orientation selector
  must live in the full 3+1 shift/holonomy sector,

not in an arbitrarily fitted GL(3) shear.

## Spatial deformation relative to a flat spherical triad

Use the flat spherical reference triad

  E_0 = diag(1, r, r sin(theta)).

Then the source-owned relative spatial deformation is

  F_Kerr := E_Kerr E_0^{-1}

  = diag(
      sqrt(Sigma/Delta),
      sqrt(Sigma)/r,
      sqrt(A/Sigma)/r
    ).

This F is diagonal in the Boyer-Lindquist principal spatial frame.

It is source-owned: once M,a,r,theta and the coordinate/reference convention are frozen, F is fixed without CMB data.

## Polar-axis axisymmetric reduction

On the rotation axis theta -> 0, use regular local transverse coordinates rather than the singular azimuthal coordinate. The two transverse scale factors coincide.

Relative to the flat local reference, the anisotropy ratio becomes

  lambda_Kerr
  := lambda_parallel/lambda_perp
  = r/sqrt(Delta).

Thus an axisymmetric source deformation around the centre-observer radial axis has one source parameter

  lambda = r/sqrt(r^2 - 2Mr + a^2).

At large r, lambda -> 1.
Near a non-extremal outer horizon, lambda -> infinity.

## Prediction firewall

The formulas above do NOT provide a numerical F until the parent-domain parameters and evaluation point are fixed independently.

Forbidden:

- infer M,a,r,theta from CMB l=2,3 and then call the resulting F a prediction;
- drop beta^phi while claiming a leading-order Kerr rotational effect;
- fit an arbitrary GL(3) F after viewing the octupole.

Admissible prospective pipeline:

  parent-domain source packet (M,a,r,theta, frame convention)
  -> alpha, beta, E_Kerr
  -> F_Kerr and full coframe
  -> tetrahedral/Moire forward operator
  -> frozen CMB l=2,3 predictions
  -> held-out evaluation.
