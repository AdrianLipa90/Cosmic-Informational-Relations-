#!/usr/bin/env python3
import math
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TIR_COMMIT = "853032e019824b836de43634d949da5566396153"
EXPECTED_CHAIN = [
    "0", "POINT", "FIRST DISTINCTION", "{N,S}", "1/2", "ln2",
    "C^2", "CP^1 / Bloch state geometry", "Herm_0(2) ~= R^3",
    "relational spatial geometry", "tetrahedral closure",
    "typed connection / holonomy", "SE(3) affine lift / solder",
    "Cartan refinement", "Levi-Civita sector",
    "spatial x temporal closure", "spacetime metric / invariant gravity observables",
    "cosmological dynamics", "cosmic observables"
]

def main():
    failures = []

    pin_path = ROOT / "provenance" / "TIR_PARENT_PIN.json"
    pin = json.loads(pin_path.read_text(encoding="utf-8"))
    if pin.get("parent_commit") != EXPECTED_TIR_COMMIT:
        failures.append("parent_commit_mismatch")

    kappa = math.log(2.0) / (24.0 * math.pi)
    if not math.isfinite(kappa) or not (0.009 < kappa < 0.010):
        failures.append("kappa_numeric_sanity")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    pos = -1
    for token in EXPECTED_CHAIN:
        new_pos = readme.find(token, pos + 1)
        if new_pos < 0:
            failures.append(f"missing_or_out_of_order:{token}")
            break
        pos = new_pos

    scope = (ROOT / "FOUNDATIONS" / "CIR_SCOPE_AND_PROMOTION_BOUNDARY_V0_1.md").read_text(encoding="utf-8")
    required_firewalls = [
        "wave structure              != fuzzy dark matter",
        "holonomy                    != physical curvature",
        "software validation         != empirical validation",
        "retrospective fit           != prediction",
    ]
    for line in required_firewalls:
        if line not in scope:
            failures.append(f"missing_firewall:{line}")

    result = {
        "schema": "CIR_FOUNDATION_VALIDATION_V0_1",
        "parent_commit": EXPECTED_TIR_COMMIT,
        "kappa": kappa,
        "checks": {
            "parent_pin": pin.get("parent_commit") == EXPECTED_TIR_COMMIT,
            "ordered_dependency_chain": not any(x.startswith("missing_or_out_of_order:") for x in failures),
            "firewalls_present": not any(x.startswith("missing_firewall:") for x in failures),
            "kappa_numeric_sanity": "kappa_numeric_sanity" not in failures,
        },
        "failures": failures,
        "verdict": "PASS" if not failures else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()
