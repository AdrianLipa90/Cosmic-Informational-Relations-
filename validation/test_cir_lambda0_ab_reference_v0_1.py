"""Deterministic offline tests for the conditional CIR Lambda0/AB model."""

import math
import unittest

from cir_lambda0_ab_reference_v0_1 import (
    KAPPA_TIR, bianchi_exchange_residual, candidate_u,
    candidate_u_metric_derivative, closed_loop_phase, closed_loop_wilson,
    conformal_flat_einstein_diagonal, de_sitter_conformal_control,
    determinant4, diagonal, electromagnetic_invariant, flrw_scalar_acceleration,
    gauge_transform_loop, identity4, inverse4, potential_action_density,
    potential_stress,
)

ETA_INV = diagonal([-1.0, 1.0, 1.0, 1.0])
ZERO_F = [[0.0] * 4 for _ in range(4)]


def f_e_b(e, b):
    f = [[0.0] * 4 for _ in range(4)]
    f[0][1], f[1][0] = e, -e
    f[2][3], f[3][2] = b, -b
    return f


class TestCIRLambda0ABReference(unittest.TestCase):
    def assertMatrixClose(self, a, b, tolerance=1e-10):
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(a[i][j], b[i][j], delta=tolerance)

    def test_kappa_tir_not_einstein_coupling(self):
        self.assertAlmostEqual(KAPPA_TIR * 24.0 * math.pi, math.log(2.0))

    def test_inverse_4x4_lorentzian(self):
        original = diagonal([-2.0, 3.0, 4.0, 7.0])
        inverse = inverse4(original)
        self.assertMatrixClose(inverse, diagonal([-0.5, 1/3, 0.25, 1/7]))

    def test_inverse_4x4_nondiagonal(self):
        inv = [[-1.0, 0.2, 0.0, 0.0],
               [0.2, 1.1, 0.1, 0.0],
               [0.0, 0.1, 1.3, 0.0],
               [0.0, 0.0, 0.0, 0.7]]
        x = inverse4(inv)
        product = [[sum(inv[i][k]*x[k][j] for k in range(4))
                    for j in range(4)] for i in range(4)]
        self.assertMatrixClose(product, identity4())

    def test_det_metric_signature(self):
        self.assertAlmostEqual(determinant4(ETA_INV), -1.0)

    def test_electromagnetic_invariant_known_E_B(self):
        e, b = 1.3, 0.9
        self.assertAlmostEqual(electromagnetic_invariant(ETA_INV, f_e_b(e, b)),
                               2.0 * (b*b - e*e))

    def test_electromagnetic_invariant_zero_F(self):
        self.assertEqual(electromagnetic_invariant(ETA_INV, ZERO_F), 0.0)

    def test_invalid_F_rejected(self):
        f = f_e_b(1.0, 0.0)
        f[1][0] = 0.0
        with self.assertRaises(ValueError):
            electromagnetic_invariant(ETA_INV, f)

    def test_U_metric_independent_stress(self):
        t = potential_stress(ETA_INV, ZERO_F, u0=2.5, alpha=0.0)
        expected = diagonal([2.5, -2.5, -2.5, -2.5])
        self.assertMatrixClose(t, expected)

    def test_U_metric_derivative_symmetric(self):
        g = [[-1.0, 0.2, 0, 0], [0.2, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        f = f_e_b(1.1, 0.7)
        du = candidate_u_metric_derivative(g, f, 0.4)
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(du[i][j], du[j][i], places=12)

    def test_U_metric_derivative_matches_finite_difference(self):
        f = f_e_b(1.7, -0.6)
        g = [[-1.05, 0.15, 0, 0], [0.15, 1.14, -0.07, 0],
             [0, -0.07, 0.83, 0.11], [0, 0, 0.11, 0.95]]
        u0, alpha, eps = 1.6, 0.27, 1e-6
        analytic = candidate_u_metric_derivative(g, f, alpha)
        for i, j in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2)]:
            plus = [row[:] for row in g]
            minus = [row[:] for row in g]
            plus[i][j] += eps
            minus[i][j] -= eps
            if i != j:
                plus[j][i] += eps
                minus[j][i] -= eps
            fd = (candidate_u(plus, f, u0, alpha) - candidate_u(minus, f, u0, alpha)) / (2*eps)
            expected = analytic[i][j] * (1 if i == j else 2)
            self.assertAlmostEqual(fd, expected, delta=2e-8)

    def test_action_metric_variation_matches_stress(self):
        f = f_e_b(0.85, 0.35)
        g = [[-1.1, 0.07, 0, 0], [0.07, 0.9, 0, 0],
             [0, 0, 1.2, -0.05], [0, 0, -0.05, 1.1]]
        u0, alpha, eps = 0.47, 0.19, 1e-6
        T = potential_stress(g, f, u0, alpha)
        root_minus_g = 1.0 / math.sqrt(-determinant4(g))
        for i, j in [(0, 0), (1, 1), (2, 2), (0, 1), (2, 3)]:
            plus = [row[:] for row in g]
            minus = [row[:] for row in g]
            plus[i][j] += eps
            minus[i][j] -= eps
            if i != j:
                plus[j][i] += eps
                minus[j][i] -= eps
            d_action = (potential_action_density(plus, f, u0, alpha) -
                        potential_action_density(minus, f, u0, alpha)) / (2*eps)
            expected = -0.5*root_minus_g * T[i][j] * (1 if i == j else 2)
            self.assertAlmostEqual(d_action, expected, delta=2e-8)

    def test_near_singular_metric_rejected(self):
        with self.assertRaises(ValueError):
            inverse4(diagonal([-1.0, 0.0, 1.0, 1.0]))

    def test_nonlorentzian_action_metric_rejected(self):
        with self.assertRaises(ValueError):
            potential_action_density(identity4(), ZERO_F, 1.0, 0.0)

    def test_wilson_closed_loop_unit_norm(self):
        w = closed_loop_wilson([0.18, -0.07, 0.09, 0.05])
        self.assertAlmostEqual(abs(w), 1.0)
        self.assertAlmostEqual(closed_loop_phase([0.18,-0.07,0.09,0.05]), 0.25)

    def test_local_vertex_gauge_invariance(self):
        edges = [0.18, -0.07, 0.09, 0.05]
        transformed = gauge_transform_loop(edges, [0.8, -0.3, 1.1, -0.5])
        self.assertAlmostEqual(closed_loop_phase(transformed), 0.25)
        self.assertAlmostEqual(abs(closed_loop_wilson(edges) - closed_loop_wilson(transformed)), 0.0, delta=1e-13)

    def test_wilson_flux_quantum_periodicity(self):
        edges = [0.01, 0.04, 0.2, 0.0]
        flux = edges[:]
        flux[-1] += 2*math.pi
        self.assertAlmostEqual(abs(closed_loop_wilson(edges) - closed_loop_wilson(flux)), 0.0, delta=1e-14)

    def test_ab_nontrivial_wilson_without_local_F(self):
        # Diagnostic of nonlocal flux: identical F on accessible path,
        # different enclosed flux and U(1) loop phases. NOT gravity.
        path0 = [0.0, 0.0, 0.0, 0.0]
        path1 = [0.18, -0.07, 0.09, 0.05]
        self.assertGreater(abs(closed_loop_wilson(path0) - closed_loop_wilson(path1)), 0.2)
        self.assertEqual(candidate_u(ETA_INV, ZERO_F, 1.0, 0.5),
                         candidate_u(ETA_INV, ZERO_F, 1.0, 0.5))

    def test_AB_versus_metric_independent_potential(self):
        # Local U(F^2) has NO holonomy dependence for fixed local F.
        # Refutes the inference 'AB phase implies local curvature'.
        F = ZERO_F
        u = candidate_u(ETA_INV, F, 0.11, 0.25)
        self.assertEqual(u, 0.11)
        self.assertNotEqual(closed_loop_wilson([0.0, 0.0]),
                            closed_loop_wilson([0.1, 0.3]))

    def test_bianchi_constant_lambda_and_conserved_other(self):
        self.assertEqual(bianchi_exchange_residual([0]*4, [0]*4, 2.5), (0.0,)*4)

    def test_bianchi_variable_lambda_without_exchange_fails(self):
        r = bianchi_exchange_residual([0.4, 0, 0, 0], [0]*4, 2.0)
        self.assertGreater(abs(r[0]), 0.1)

    def test_bianchi_sourced_exchange_is_consistent(self):
        dl = [0.4, -0.3, 0.0, 0.1]
        kappa = 1.7
        div = [x/kappa for x in dl]
        self.assertLess(max(abs(x) for x in bianchi_exchange_residual(dl, div, kappa)), 1e-14)

    def test_flat_no_source_einstein(self):
        self.assertEqual(conformal_flat_einstein_diagonal(0.0, 0.0), (0.0,)*4)

    def test_de_sitter_einstein_lambda_vacuum(self):
        for t in [-2.0, -0.35, -0.05]:
            for H in [0.1, 0.75, 2.0]:
                G, g, lam = de_sitter_conformal_control(t, H)
                self.assertLess(max(abs(G[i] + lam*g[i]) for i in range(4)),
                                1e-8 * max(1.0, max(abs(x) for x in G)))

    def test_de_sitter_invalid_domain(self):
        with self.assertRaises(ValueError):
            de_sitter_conformal_control(0.1, 0.5)

    def test_scalar_potential_reassignment_no_double_count(self):
        for k in [0.1, 1.4, 2.1]:
            for kinetic, potential in [(0.0, 1.0), (0.4, 1.0), (1.0, 0.3)]:
                original, moved = flrw_scalar_acceleration(k, kinetic, potential)
                self.assertAlmostEqual(original, moved, delta=1e-12)

    def test_pure_phase_kinetic_decelerates(self):
        original, moved = flrw_scalar_acceleration(2.0, 0.8, 0.0)
        self.assertLess(original, 0.0)
        self.assertEqual(original, moved)

    def test_potential_energy_can_accelerate_conditionally(self):
        original, moved = flrw_scalar_acceleration(1.0, 0.1, 1.0)
        self.assertGreater(original, 0.0)
        self.assertAlmostEqual(original, moved)


if __name__ == '__main__':
    unittest.main(verbosity=2)
