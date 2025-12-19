# backend/services/quantum_nexus.py
"""
Quantum Nexus Lattice Coordinate System
Great Greg Resolver for neurodivergent-aware cognitive mapping
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


@dataclass(frozen=True)
class GreatGreg:
    """Immutable coordinate reference in the Quantum Nexus lattice."""
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
    
    Filing System:
      - Origin: A1 (upper-left)
      - Terminus: Z1 (lower-right / ZA1 Dynamic Expansion)
      - Primary Flow: left_to_right_then_top_to_bottom (lateral, row-major)
      - Secondary Flow: right_to_left_vertical (instruction shaft)
      - Rule: no_bad_input_no_bad_process_no_bad_output
    """

    def __init__(self, blueprint: Dict[str, Any]):
        self.bp = blueprint
        self._rc_map = (blueprint.get("great_greg_coordinates", {}) or {}).get("rc_map", {}) or {}
        self._deps = {d["id"]: d for d in (blueprint.get("dependencies") or []) if isinstance(d, dict) and "id" in d}
        self._nodes = {n["id"]: n for n in (blueprint.get("nodes") or []) if isinstance(n, dict) and "id" in n}

    @classmethod
    def from_yaml(cls, path: str | Path) -> "QuantumNexus":
        """Load blueprint from YAML file."""
        p = Path(path)
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        # Accept either top-level blueprint or nested under "quantum_nexus_blueprint"
        if "quantum_nexus_blueprint" in data:
            data = data["quantum_nexus_blueprint"]
        return cls(data)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QuantumNexus":
        """Load blueprint from dictionary."""
        if "quantum_nexus_blueprint" in data:
            data = data["quantum_nexus_blueprint"]
        return cls(data)

    def dependency(self, dep_id: str) -> Dict[str, Any]:
        """Get dependency configuration by ID."""
        if dep_id not in self._deps:
            raise KeyError(f"Dependency not found: {dep_id}")
        return self._deps[dep_id]

    def node(self, node_id: str) -> Dict[str, Any]:
        """Get node configuration by ID."""
        if node_id not in self._nodes:
            raise KeyError(f"Node not found: {node_id}")
        return self._nodes[node_id]

    def resolve_cell(self, cell: str) -> GreatGreg:
        """Resolve a cell reference (e.g., 'P1') to GreatGreg coordinates."""
        cell = cell.strip().upper()
        info = self._rc_map.get(cell)
        if not info:
            raise KeyError(f"Unknown cell: {cell}")
        return GreatGreg(
            cell=cell,
            r=int(info["r"]),
            c=int(info["c"]),
            node=int(info["node"]),
            label=str(info["label"])
        )

    def resolve(self, ref: str) -> GreatGreg:
        """
        Resolve any coordinate format to GreatGreg.
        
        Accepts:
          - "P1"           → direct cell lookup
          - "Node_3:P1"    → node-prefixed cell
          - "Node_3.R3C4"  → row/column/node triplet
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

    def trace_path(self, dep_id: str) -> List[GreatGreg]:
        """Trace the path of a dependency, returning resolved coordinates."""
        dep = self.dependency(dep_id)
        path = dep.get("path", [])
        
        # Handle nested path structure (row-major)
        if path and isinstance(path[0], list):
            flat_path = [cell for row in path for cell in row]
        else:
            flat_path = path
        
        return [self.resolve_cell(cell) for cell in flat_path]

    def get_node_cells(self, node_id: str) -> List[GreatGreg]:
        """Get all cells belonging to a node."""
        node = self.node(node_id)
        cells = node.get("cells", [])
        return [self.resolve_cell(cell) for cell in cells]

    def diagonal_trace(self) -> List[GreatGreg]:
        """Return the A1 → V1 diagonal dependency path."""
        return self.trace_path("dep_A1_to_V1")

    def lateral_trace(self) -> List[GreatGreg]:
        """Return the full left-to-right row-major path (A1 → Z1)."""
        return self.trace_path("dep_AllFiles_L2R_to_Z1")

    @property
    def origin(self) -> GreatGreg:
        """Return the origin cell (A1 - Prime Truth)."""
        return self.resolve_cell("A1")

    @property
    def terminus(self) -> GreatGreg:
        """Return the terminus cell (Z1 - Dynamic Expansion)."""
        return self.resolve_cell("Z1")

    def to_api_response(self, ref: str) -> Dict[str, Any]:
        """Convert a coordinate reference to API-friendly response."""
        coord = self.resolve(ref)
        return {
            "cell": coord.cell,
            "row": coord.r,
            "column": coord.c,
            "node": coord.node,
            "label": coord.label,
            "node_id": f"Node_{coord.node}"
        }
