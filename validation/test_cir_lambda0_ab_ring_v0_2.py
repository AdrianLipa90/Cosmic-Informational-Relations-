"""Regression tests of matter-mediated AB stress, not gravity discovery."""
from __future__ import annotations

import math
import unittest

from cir_lambda0_ab_ring_v0_2 import (
    TWO_PI, box_phase_energy, continuum_ring_energy, finite_ring_energy,
    finite_ring_uniform_energy, matter_flux_current, phase_mismatch,
    phase_stress_covariant, phase_stress_mixed, preferred_winding,
    transform_ring_gauge, uniform_ring_configuration, wilson_real, closed_wilson,
)


class TestCIRABRingV02(unittest.TestCase):
    def test_preferred_winding(self):
        self.assertEqual(preferred_winding(0.25), 0)
        self.assertEqual(preferred_winding(TWO_PI + 0.25), 1)
        self.assertEqual(preferred_winding(-TWO_PI + 0.25), -1)

    def test_half_flux_degenerate_winding(self):
        self.assertAlmostEqual(continuum_ring_energy(math.pi, 3.0, 2.0, 0),
                               continuum_ring_energy(math.pi, 3.0, 2.0, 1))

    def test_phase_mismatch_zero_at_integer_flux(self):
        self.assertAlmostEqual(phase_mismatch(TWO_PI, 1), 0.0)

    def test_ground_energy_periodic_under_large_gauge(self):
        for flux in (-3.01, -1.23, 0.0, 0.15, 1.77, 2.90):
            self.assertAlmostEqual(continuum_ring_energy(flux, 5.0, 3.0),
                                   continuum_ring_energy(flux + TWO_PI, 5.0, 3.0))

    def test_same_m_branch_not_flux_periodic(self):
        # Large gauge transformations must shift m as well.
        self.assertNotAlmostEqual(continuum_ring_energy(0.3, 5.0, 1.0, 0),
                                  continuum_ring_energy(0.3 + TWO_PI, 5.0, 1.0, 0))

    def test_global_wilson_different_flat_connections(self):
        self.assertGreater(abs(closed_wilson([0.0]*4) -
                               closed_wilson([0.15]*4)), 0.2)

    def test_finite_site_gauge_invariance(self):
        psi, link = uniform_ring_configuration(13, 1.15, 1)
        original = finite_ring_energy(psi, link, 3.5, 1.7)
        angles = [0.75*math.sin(3*j) for j in range(13)]
        rotated_psi, rotated_links = transform_ring_gauge(psi, link, angles)
        transformed = finite_ring_energy(rotated_psi, rotated_links, 3.5, 1.7)
        self.assertAlmostEqual(original, transformed, places=12)
        self.assertAlmostEqual(abs(closed_wilson(rotated_links) -
                                   closed_wilson(link)), 0.0, delta=1e-12)

    def test_finite_ring_formula_matches_explicit_sum(self):
        for n in (8, 25, 100):
            psi, link = uniform_ring_configuration(n, 1.4, 0)
            self.assertAlmostEqual(finite_ring_energy(psi, link, 2.7, 3.2),
                                   finite_ring_uniform_energy(n, 1.4, 2.7, 3.2, 0),
                                   delta=1e-10)

    def test_continuum_limit_second_order(self):
        exact = continuum_ring_energy(0.9, 2.5, 1.2, 0)
        e32 = finite_ring_uniform_energy(32, 0.9, 2.5, 1.2, 0)
        e64 = finite_ring_uniform_energy(64, 0.9, 2.5, 1.2, 0)
        self.assertLess(abs(e64-exact), 0.27*abs(e32-exact))

    def test_anisotropic_stress_not_lambda_tensor(self):
        cov = phase_stress_covariant(0.8, 2.0, 1.6, 0)
        self.assertAlmostEqual(cov[0], cov[1])
        self.assertAlmostEqual(cov[0], -cov[2])
        self.assertAlmostEqual(cov[0], -cov[3])
        self.assertGreater(cov[0], 0.0)
        self.assertEqual(phase_stress_mixed(0.8, 2.0, 1.6, 0),
                         (-cov[0], cov[1], cov[2], cov[3]))

    def test_zero_stress_if_no_matter_even_with_wilson(self):
        self.assertNotAlmostEqual(wilson_real(1.2), 1.0)
        self.assertEqual(phase_stress_covariant(1.2, 5.0, 0.0, 0), (0,)*4)

    def test_zero_stress_integer_flux(self):
        self.assertLess(max(abs(x) for x in phase_stress_covariant(TWO_PI, 2.0, 3.0)), 1e-24)

    def test_stress_large_gauge_invariance(self):
        self.assertEqual(phase_stress_covariant(0.5, 2, 0.4),
                         phase_stress_covariant(0.5 + TWO_PI, 2, 0.4))

    def test_stress_integrated_energy_exact(self):
        length, area, f2, phase = 4.0, 2.2, 0.8, 0.9
        rho = phase_stress_covariant(phase, length, f2)[0]
        self.assertAlmostEqual(rho*length*area,
                               box_phase_energy(phase, length, area, f2))

    def test_longitudinal_pressure_from_length_variation(self):
        L, area, f2, phi, eps = 4.3, 2.0, 0.9, 0.75, 1e-5
        eplus = box_phase_energy(phi, L+eps, area, f2)
        eminus = box_phase_energy(phi, L-eps, area, f2)
        pressure = -(eplus-eminus)/(2*eps*area)
        self.assertAlmostEqual(pressure, phase_stress_covariant(phi, L, f2)[1],delta=2e-10)

    def test_transverse_pressure_from_area_variation(self):
        L, area, f2, phi, eps = 3.8, 1.9, 0.8, 1.1, 1e-5
        eplus = box_phase_energy(phi, L, area+eps, f2)
        eminus = box_phase_energy(phi, L, area-eps, f2)
        pressure = -(eplus-eminus)/(2*eps*L)
        self.assertAlmostEqual(pressure, phase_stress_covariant(phi, L, f2)[2],delta=2e-10)

    def test_isotropic_average_is_not_dark_energy(self):
        rho,p_parallel,p_y,p_z = phase_stress_covariant(1.3, 3.0, 1.0)
        self.assertAlmostEqual(rho+p_parallel+p_y+p_z, 0.0, delta=1e-15)
        self.assertAlmostEqual((p_parallel+p_y+p_z)/(3*rho), -1/3)

    def test_flux_current_matches_energy_derivative(self):
        L, stiffness, phi, eps = 3.5, 0.9, 1.2, 1e-6
        deriv = (continuum_ring_energy(phi+eps, L, stiffness) -
                 continuum_ring_energy(phi-eps, L, stiffness))/(2*eps)
        self.assertAlmostEqual(-deriv, matter_flux_current(phi, L, stiffness), delta=1e-9)

    def test_reject_invalid_geometry(self):
        for bad in (0.0, -1.0, math.inf, math.nan):
            with self.assertRaises(ValueError):
                box_phase_energy(0.4, bad, 1, 1)

    def test_reject_invalid_fields(self):
        with self.assertRaises(ValueError):
            phase_stress_covariant(1.2, 2.0, -0.1)
        with self.assertRaises(ValueError):
            continuum_ring_energy(1.2, 2.0, 0.0)

    def test_reject_mismatched_lattice(self):
        with self.assertRaises(ValueError):
            finite_ring_energy([1,1,1],[0.0,0.0],1.0,1.0)
        with self.assertRaises(ValueError):
            transform_ring_gauge([1,1,1],[0,0,0],[0,0])

    def test_connection_not_metric_response(self):
        # Matter stress depends on holonomy + a physical charged field,
        # not on Wilson loop alone and not via an invented Lambda_0.
        flux = 0.75
        self.assertNotAlmostEqual(wilson_real(flux), 1.0)
        self.assertNotEqual(phase_stress_covariant(flux, 2, 1)[0], 0)
        self.assertEqual(phase_stress_covariant(flux, 2, 0)[0], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
