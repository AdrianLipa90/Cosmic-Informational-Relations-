# CIR Conditional Semantic-Centre 3D Locus v0.1

Status: DOUBLY-CONDITIONAL PREDICTION LOCUS / NO CATALOG OPENED
Date: 2026-09-27

## 1. Inputs frozen upstream

Radial branch:
- conditional regular-C6/ARPL bridge;
- q = 1/6;
- frozen CMB last-scattering screen radius R_CMB = 13,873 Mpc.

Directional branch:
- frozen unoriented CIR low-l axis
  (l,b) = (239.9881633256477 deg, 68.5117419161366 deg).

The direction was derived before the present locus construction.

## 2. Conditional radius

  d_star = R_CMB/6
         = 2312.1666666666665 Mpc
         = 2.3121666666666665 Gpc.

Using a flat Planck-like reference cosmology only for coordinate intuition

  H0=67.4 km/s/Mpc,
  Omega_m=0.315,

this comoving distance corresponds to approximately

  z_ref = 0.6109.

The redshift is not a new model parameter and must not replace the comoving
distance definition.

## 3. Conditional sky positions

Primary Galactic axis:

  P_plus:
    l = 239.9881633256477 deg
    b = +68.5117419161366 deg
    d = 2312.1666666666665 Mpc

Antipode:

  P_minus:
    l = 59.9881633256477 deg
    b = -68.5117419161366 deg
    d = 2312.1666666666665 Mpc

Equivalent ICRS representatives:

  P_plus:
    RA  = 173.01886567517522 deg
        = 11.534591045011682 h
    Dec = +16.021504653218 deg

  P_minus:
    RA  = 353.0188656751752 deg
    Dec = -16.021504653218 deg.

Galactic Cartesian comoving coordinates for P_plus, with x toward l=0,b=0,
y toward l=90,b=0 and z toward the north Galactic pole:

  (x,y,z)
  = (-423.6370, -733.4109, +2151.4541) Mpc.

P_minus is the negative of this vector.

## 4. Directional resolution from the frozen input-axis ensemble

The frozen common axis was constructed from eight Planck-2013 low-l axis
measurements:

  C-R_o, C-R_q,
  NILC_o, NILC_q,
  SEVEM_o, SEVEM_q,
  SMICA_o, SMICA_q.

Their unoriented angular separations from the frozen common axis are:

  3.4455, 9.6263,
  4.3656, 8.7962,
  4.3231, 5.3442,
  4.2301, 8.0999 degrees.

Descriptive spread:
- mean angular separation = 6.0289 deg;
- RMS angular separation  = 6.4394 deg;
- maximum                 = 9.6263 deg.

These are not formal statistical confidence intervals.

At d_star the corresponding transverse scales are approximately:
- RMS-spread transverse scale: 259 Mpc;
- max-spread transverse scale: 387 Mpc.

Therefore the current model does NOT localize a physical centre to a small
astrophysical volume. The present directional uncertainty is cosmological in
size.

## 5. Radial anchor uncertainty

The previously frozen Planck screen anchor used approximately

  sigma_R_CMB = 25 Mpc.

If the q=1/6 bridge were exact, this contribution alone would give

  sigma_d,anchor = 25/6 Mpc
                 = 4.1667 Mpc.

This is much smaller than the current transverse directional spread, but it is
not the total model uncertainty because the physical C6-child binding itself
has not been empirically established.

## 6. Search firewall

No astronomical target catalogue was opened to construct this locus.

Before any target search, a separate search protocol must freeze:
- target population/catalogue;
- angular statistic;
- radial statistic;
- object property used as "mass" or source relevance;
- null/randomization procedure;
- treatment of the antipodal degeneracy.

Forbidden:
- expanding the cone because a desired object lies just outside it;
- moving d_star to a catalog peak;
- selecting a catalog after inspecting which one produces an attractive hit;
- calling the locus a measured centre of the Universe.

## 7. Current status

EXACT GIVEN BRIDGE CONDITIONS:
- coordinate transforms;
- d_star=R_CMB/6;
- input-axis spread arithmetic.

OPEN PHYSICAL CONDITIONS:
- REGULAR_C6_CHILD_BINDING;
- internal-C3 to sky-C3 charged transfer;
- identification of this locus with a physical source/centre.

The locus is therefore a preregisterable target for future tests, not a
detection.
