#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

OPEN={"OPEN_PHYSICAL_BINDING","OPEN_INPUT","OPEN_EMPIRICAL","NONE_FROZEN"}
PHYSICAL_SCOPES={"physical_realization","empirical","prospective_evidence"}

def main():
    dag=json.loads((ROOT/"dependency"/"CIR_DEPENDENCY_DAG_V0_1.json").read_text("utf-8"))
    nodes={n["id"]:n for n in dag["nodes"]}
    failures=[]

    # Referential integrity.
    for a,b in dag["edges"]:
        if a not in nodes or b not in nodes:
            failures.append(f"missing_node:{a}->{b}")

    # DAG acyclicity.
    adj={k:[] for k in nodes}
    indeg={k:0 for k in nodes}
    for a,b in dag["edges"]:
        if a in nodes and b in nodes:
            adj[a].append(b); indeg[b]+=1
    q=[k for k,v in indeg.items() if v==0]
    seen=[]
    while q:
        x=q.pop()
        seen.append(x)
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    if len(seen)!=len(nodes): failures.append("cycle")

    # Required frontier nodes must remain open/unfrozen.
    for node_id in ["P0","P1","P2","C1","C3","C4","O1","O2"]:
        if nodes[node_id]["status"] not in OPEN:
            failures.append("premature_promotion:"+node_id)

    # Retained no-go nodes cannot be re-labelled PASS.
    for node_id in ["N0","N1","N2"]:
        if nodes[node_id]["status"]!="NO_GO":
            failures.append("nogo_lost:"+node_id)

    # No empirical PASS while prediction is not frozen.
    if nodes["O1"]["status"]=="NONE_FROZEN" and nodes["O2"]["status"] not in OPEN:
        failures.append("empirical_before_freeze")

    out={
      "schema":"CIR_DEPENDENCY_DAG_VALIDATION_V0_1",
      "node_count":len(nodes),
      "edge_count":len(dag["edges"]),
      "checks":{
        "referential_integrity":not any(x.startswith("missing_node") for x in failures),
        "acyclic":"cycle" not in failures,
        "physical_frontier_not_prematurely_promoted":not any(x.startswith("premature_promotion") for x in failures),
        "retained_no_go_preserved":not any(x.startswith("nogo_lost") for x in failures),
        "no_empirical_verdict_before_freeze":"empirical_before_freeze" not in failures
      },
      "failures":failures,
      "verdict":"PASS" if not failures else "FAIL"
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures else 1)

if __name__=="__main__":
    main()
