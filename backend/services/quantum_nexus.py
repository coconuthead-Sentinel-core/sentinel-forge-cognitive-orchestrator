from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


@dataclass(frozen=True)
class GreatGreg:
    cell: str
    r: int
    c: int
    node: int
    label: str


class QuantumNexus:
    """
    Loads the Quantum Nexus YAML blueprint and provides:
      - dependency lookup (dep_AllFiles_L2R_to_Z1, dep_A1_to_V1)
      - Great Greg coordinate resolver (A1, Node_3:P1, Node_3.R3C4)
    """

    def __init__(self, blueprint: Dict[str, Any]):
        self.bp = blueprint
        self._rc_map = (blueprint.get("great_greg_coordinates", {}) or {}).get("rc_map", {}) or {}
        self._deps = {d["id"]: d for d in (blueprint.get("dependencies") or []) if isinstance(d, dict) and "id" in d}

    @classmethod
    def from_yaml(cls, path: str | Path) -> "QuantumNexus":
        p = Path(path)
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        # Accept either top-level blueprint or nested under "quantum_nexus_blueprint"
        if "quantum_nexus_blueprint" in data:
            data = data["quantum_nexus_blueprint"]
        return cls(data)

    def dependency(self, dep_id: str) -> Dict[str, Any]:
        if dep_id not in self._deps:
            raise KeyError(f"Dependency not found: {dep_id}")
        return self._deps[dep_id]

    def resolve_cell(self, cell: str) -> GreatGreg:
        cell = cell.strip()
        info = self._rc_map.get(cell)
        if not info:
            raise KeyError(f"Unknown cell: {cell}")
        return GreatGreg(cell=cell, r=int(info["r"]), c=int(info["c"]), node=int(info["node"]), label=str(info["label"]))

    def resolve(self, ref: str) -> GreatGreg:
        """
        Accepts:
          - "P1"
          - "Node_3:P1"
          - "Node_3.R3C4"  (will map back to the matching cell if possible)
        """
        ref = ref.strip()

        # Node_3:P1 → P1
        if ":" in ref:
            _, cell = ref.split(":", 1)
            return self.resolve_cell(cell)

        # Node_3.R3C4 → find cell by r/c/node
        if ".R" in ref and "C" in ref:
            node_part, rc_part = ref.split(".", 1)
            node = int("".join(ch for ch in node_part if ch.isdigit()))
            rc_part = rc_part.upper().lstrip("R")
            r_str, c_str = rc_part.split("C", 1)
            r, c = int(r_str), int(c_str)

            # scan rc_map for matching triplet
            for cell, info in self._rc_map.items():
                if int(info["node"]) == node and int(info["r"]) == r and int(info["c"]) == c:
                    return GreatGreg(cell=cell, r=r, c=c, node=node, label=str(info["label"]))
            raise KeyError(f"No cell found for {ref} (node={node}, r={r}, c={c})")

        # default: treat as cell
        return self.resolve_cell(ref)