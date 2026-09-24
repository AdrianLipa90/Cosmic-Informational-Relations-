# CIR Observational Falsification Contract v0.1

Status: `OBSERVABLE_CONTRACT / NO_PREDICTIONS_FROZEN / LOCAL_PPN_LENSING_GW_OPEN`

Parent TIR commit: `853032e019824b836de43634d949da5566396153`

## 1. Purpose

CIR may not promote a cosmological mechanism because it reproduces one background equation or resembles one observed pattern.

A physical CIR branch must generate a common source-consistent prediction packet spanning the observables relevant to that branch, without re-fitting separate parameters after each observable is inspected.

The parent TIR frontier explicitly retains local PPN/lensing/GW validation as OPEN after physical source binding.

## 2. Observable hierarchy

The observational sequence is

\[
\boxed{
\text{source law}
\to
g_{\mu\nu}\ \text{and matter fields}
\to
\text{background}
\to
\text{null/timelike propagation}
\to
\text{perturbations}
\to
\text{measured observables}.
}
\]

An observable cannot be used as an upstream definition of the source parameter that is then claimed to predict the same observable.

## 3. Background-expansion packet

A homogeneous/isotropic branch must export at minimum

\[
H(z),
\qquad
q(z)
=
-\frac{\ddot a\,a}{\dot a^2},
\]

with all source parameters already declared.

On a spatially flat metric branch with standard metric photon propagation,

\[
\chi(z)
=
c\int_0^z\frac{dz'}{H(z')},
\]

\[
D_A(z)
=
\frac{\chi(z)}{1+z},
\qquad
D_L(z)
=
(1+z)\chi(z).
\]

Hence, under the usual reciprocity assumptions,

\[
\boxed{
D_L=(1+z)^2D_A.
}
\]

If CIR modifies photon propagation or violates the assumptions of distance duality, the modified transport law must be derived explicitly; the standard relation may not be silently reused.

## 4. Null propagation and lensing packet

For a metric realization, a null ray obeys

\[
k^\mu k_\mu=0,
\qquad
k^\nu\nabla_\nu k^\mu=0.
\]

The screen-space Jacobi map \(\mathcal D^A{}_B\) obeys the optical tidal equation

\[
\boxed{
\frac{d^2\mathcal D^A{}_B}{d\lambda^2}
=
\mathcal T^A{}_C
\mathcal D^C{}_B,
}
\]

where the optical tidal matrix is determined by the spacetime curvature projected onto the null screen.

Therefore lensing must be computed from the **same admitted metric/source realization** used for the background dynamics.

Required lensing outputs depend on regime and may include:

```text
weak lensing:
  convergence kappa_lens
  shear gamma
  angular power/correlation functions

strong lensing:
  image positions
  relative magnifications
  time delays
  extended-arc morphology

compact-object / small-scale tests:
  caustic structure
  astrometric perturbations
  temporal variability where predicted
```

A match to image positions alone is not sufficient to identify a microscopic source mechanism.

## 5. Matter and structure-growth packet

If the candidate modifies the stress ledger, it must also propagate that change into perturbations.

At minimum, a cosmological branch must declare the equations controlling:

- scalar metric perturbations;
- matter density perturbations;
- any additional CIR source perturbation;
- anisotropic stress, if present;
- initial conditions and normalization.

Relevant comparison outputs may include

\[
P(k,z),
\qquad
f(z),
\qquad
f\sigma_8(z),
\]

or source-specific substitutes.

A background-only fit does not close the cosmological branch.

## 6. Local gravity and gravitational-wave packet

A physical source-to-metric binding must remain compatible with the local sector.

The parent TIR frontier explicitly retains

```text
LOCAL_PPN_LENSING_GW_VALIDATION_AFTER_BINDING = OPEN
```

so CIR requires, where applicable:

- weak-field/post-Newtonian limits;
- local light deflection and Shapiro-delay consistency;
- compact-object metric controls;
- gravitational-wave propagation speed and polarization content;
- propagation damping/dispersion if the source law modifies it.

Recovering Schwarzschild in one conditional slicing does not by itself close these tests.

## 7. Cross-observable consistency rule

One frozen parameter packet must generate all observables assigned to the same physical branch.

Forbidden workflow:

```text
fit H(z)
-> alter source parameters
fit lensing
-> alter source parameters
fit growth
-> call all three predictions
```

Required workflow:

```text
derive source law
-> freeze source parameters and nuisance policy
-> generate background + lensing + growth + local/GW outputs
-> evaluate held-out data
-> PASS / TENSION / FAIL without hidden retuning
```

## 8. Lensing-mechanism discriminator

CIR must distinguish between at least three logically different ways to produce a lensing anomaly:

1. **source-density structure:** additional or redistributed stress-energy changes the metric;
2. **connection/metric-response structure:** a derived geometric response changes the metric/source equations;
3. **propagation-law modification:** photon/null transport differs from the standard metric-geodesic route.

These mechanisms can produce superficially similar image perturbations.

Therefore

\[
\boxed{
\text{similar lensing morphology}\neq\text{same microscopic mechanism}.
}
\]

For any claimed wave/interference origin, CIR must additionally freeze the predicted coherence scale, spatial spectrum, time evolution and correlations before comparing them with a competing wave-dark-matter or substructure model.

## 9. Prediction-freeze contract

Every prospective prediction must record:

- exact Git commit;
- exact source/provenance pins;
- physical branch and equations;
- parameter values and units;
- which values are derived, external, calibrated or nuisance;
- observables to be tested;
- data embargo/cutoff timestamp if applicable;
- no-refit rule;
- PASS/TENSION/FAIL thresholds where meaningful.

The machine-readable template is

`schemas/CIR_PREDICTION_FREEZE_V0_1.json`.

At foundation v0.1,

\[
\boxed{
\text{CIR prospective cosmological predictions frozen}=0.
}
\]

## 10. Immediate falsification priorities

Once the open source bindings close, the first high-value tests are:

```text
1. local/weak-field metric consistency
2. background H(z) and distance consistency
3. perturbation/growth consistency
4. lensing from the same realization
5. gravitational-wave propagation
6. cross-observable no-retune audit
```

## 11. Current status

```text
BACKGROUND_OBSERVABLE_CONTRACT          DEFINED
DISTANCE_DUALITY_CONTROL                STANDARD CONDITIONAL
LENSING_JACOBI_ROUTE                    STANDARD CONDITIONAL
PERTURBATION_GROWTH_CONTRACT            DEFINED
LOCAL_PPN_TEST                          OPEN AFTER SOURCE BINDING
LENSING_TEST                            OPEN AFTER SOURCE BINDING
GW_TEST                                 OPEN AFTER SOURCE BINDING
CROSS_OBSERVABLE_NO_RETUNE_RULE         ACTIVE
PROSPECTIVE_PREDICTION_FREEZE           NONE
EMPIRICAL_CIR_COSMOLOGY_VERDICT         NOT YET AVAILABLE
```

## 12. Parent provenance

Pinned TIR sources:

- `TIR/TIR_COMPLETION_FRONTIER_V0_7.md`
- `TIR/foundations/TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_V0_1.md`
- `TIR/integration/TIR_IDT_RFC_INFORMATION_HOLONOMY_COSMOLOGICAL_ACCELERATION_V0_1.md`
- `TIR/integration/TIR_IDT_RFC_TEMPORAL_U1_METRIC_RESPONSE_COSMOLOGY_V0_1.md`
