#!/usr/bin/env python3
import json, math
from pathlib import Path

KAPPA = math.log(2.0)/(24.0*math.pi)
TOL = 1e-14
checks = {}

checks['kappa_block_identity'] = abs(KAPPA*(24.0*math.pi)-math.log(2.0)) < TOL

def J(x): return -x
def T(x): return x + math.log(2.0)
def Tinv(x): return x - math.log(2.0)

probes = [-17.25, -1.0, 0.0, 0.5, 3.0, 41.125]
checks['J2_identity'] = all(abs(J(J(x))-x) < TOL for x in probes)
checks['JTJ_equals_Tinv'] = all(abs(J(T(J(x)))-Tinv(x)) < TOL for x in probes)

def Tn(x,n): return x + n*math.log(2.0)
def Jn(x,n): return Tn(J(Tn(x,-n)),n)

checks['conjugate_fixed_axes'] = all(
    abs(Jn(n*math.log(2.0),n)-n*math.log(2.0)) < TOL
    for n in range(-64,65)
)
checks['phase_shell_map'] = all(
    abs(math.exp(KAPPA*(24.0*math.pi*n))-(2.0**n))
    <= TOL*max(1.0,abs(2.0**n))
    for n in range(-32,33)
)

audit_path = Path(__file__).resolve().parent / 'CIR_DYADIC_AOE_POPULATION_AUDIT_V0_2.json'
audit = json.loads(audit_path.read_text())
checks['audit_direction_fail_preserved'] = (
    audit['direction_test']['verdict'] == 'FAIL_FOR_ALIGNMENT_HYPOTHESIS'
)
checks['audit_scale_fail_preserved'] = (
    audit['scale_test']['verdict'] == 'FAIL_FOR_GLOBAL_DYADIC_MASS_COMB'
)
checks['audit_q_frozen_2'] = audit['scale_test']['q_frozen'] == 2.0

status = 'PASS' if all(checks.values()) else 'FAIL'
receipt = {
    'schema':'CIR_LOCAL_LOG_SCALE_BINDING_VALIDATION_RECEIPT_V0_3',
    'date':'2026-09-26',
    'status':status,
    'checks':checks,
    'epistemic_boundary':{
        'exact':'representation identities and D_infinity action',
        'falsified':'universal Hubble anchor for full SMBH population',
        'open':[
            'physical source theorem for L_star(S)',
            'independent selector n(S->X)',
            'AoE physical binding'
        ]
    }
}
print(json.dumps(receipt,sort_keys=True,indent=2))
if status != 'PASS':
    raise SystemExit(1)
