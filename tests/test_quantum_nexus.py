# tests/test_quantum_nexus.py
"""Tests for the Quantum Nexus lattice coordinate system."""
import pytest
from backend.services.quantum_nexus import QuantumNexus, GreatGreg
from backend.core.config import settings
from typing import Type
import yaml
from pathlib import Path



@pytest.fixture
def nexus() -> QuantumNexus:
    """Create a QuantumNexus instance from the blueprint path in settings."""
    return QuantumNexus.from_settings(settings)


class TestGreatGregResolver:
    """Tests for Great Greg coordinate resolution."""

    def test_resolve_cell_direct(self, nexus: QuantumNexus):
        """Test direct cell resolution (e.g., 'O1')."""
        # Using a cell from the actual blueprint
        coord = nexus.resolve("O1")
        assert coord.cell == "O1"
        assert coord.r == 3
        assert coord.c == 3
        assert coord.node == 3
        assert coord.label == "Action Emitter (Diagonal Node 3)"

    def test_resolve_cell_with_node_prefix(self, nexus: QuantumNexus):
        """Test node-prefixed cell resolution (e.g., 'Node_3:O1')."""
        coord = nexus.resolve("Node_3:O1")
        assert coord.cell == "O1"
        assert coord.r == 3
        assert coord.c == 3
        assert coord.node == 3

    def test_resolve_rc_format(self, nexus: QuantumNexus):
        """Test row/column/node triplet resolution (e.g., 'Node_3.R3C3')."""
        coord = nexus.resolve("Node_3.R3C3")
        assert coord.cell == "O1"
        assert coord.r == 3
        assert coord.c == 3
        assert coord.node == 3

    def test_resolve_origin(self, nexus: QuantumNexus):
        """Test origin cell (A1 - Prime Truth)."""
        origin = nexus.resolve("A1")
        assert origin.cell == "A1"
        assert origin.r == 1
        assert origin.c == 1
        assert origin.node == 1

    def test_resolve_terminus(self, nexus: QuantumNexus):
        """Test terminus cell (Z1 - Dynamic Expansion)."""
        terminus = nexus.resolve("Z1")
        assert terminus.cell == "Z1"
        assert terminus.r == 5
        assert terminus.c == 2
        assert terminus.node == 5

    def test_unknown_cell_raises(self, nexus: QuantumNexus):
        """Test that unknown cell raises KeyError."""
        with pytest.raises(KeyError):
            nexus.resolve("X99")

    def test_unknown_rc_format_raises(self, nexus: QuantumNexus):
        """Test that unknown R/C format raises KeyError."""
        with pytest.raises(KeyError):
            nexus.resolve("Node_9.R9C9")

    def test_malformed_ref_raises(self, nexus: QuantumNexus):
        """Test that malformed references raise errors."""
        with pytest.raises(ValueError):
            nexus.resolve("Node_3.R3C")  # Incomplete
        with pytest.raises(KeyError):
            nexus.resolve("Node_3:")  # Incomplete
        with pytest.raises(KeyError):
            nexus.resolve("InvalidCell")


class TestDependencies:
    """Tests for dependency path lookups."""

    def test_get_dependency_path(self, nexus: QuantumNexus):
        """Test retrieving a known dependency path."""
        dep = nexus.dependency("dep_A1_to_V1")
        assert dep["id"] == "dep_A1_to_V1"
        assert dep["from"] == "A1"
        assert dep["to"] == "V1"
        assert dep["path"] == ["A1", "H1", "O1", "V1"]

    def test_get_nested_dependency_path(self, nexus: QuantumNexus):
        """Test retrieving a dependency with nested path structure."""
        dep = nexus.dependency("dep_AllFiles_L2R_to_Z1")
        assert isinstance(dep["path"], list)
        assert isinstance(dep["path"][0], list)
        # This path might differ in the real blueprint, adjust if needed
        # For now, we check the structure.
        assert "A1" in dep["path"][0]

    def test_unknown_dependency_raises(self, nexus: QuantumNexus):
        """Test that unknown dependency raises KeyError."""
        with pytest.raises(KeyError):
            nexus.dependency("dep_nonexistent")


class TestBlueprintLoading:
    """Tests related to loading the blueprint file."""

    def test_from_settings_loads_correctly(self):
        """Ensure from_settings method loads the file specified in config."""
        # This test is implicitly covered by the nexus fixture,
        # but an explicit test makes the behavior clear.
        nexus = QuantumNexus.from_settings(settings)
        # Check a known value from the real blueprint
        assert nexus.resolve("A1").label == "Initiation Point (Prime Truth)"

    def test_from_settings_file_not_found(self):
        """Test that a missing blueprint file raises FileNotFoundError."""
        temp_settings = settings.model_copy()
        temp_settings.QUANTUM_NEXUS_BLUEPRINT_PATH = "/nonexistent/path/blueprint.yaml"
        with pytest.raises(FileNotFoundError):
            QuantumNexus.from_settings(temp_settings)

    def test_from_settings_invalid_yaml(self, tmp_path: Path):
        """Test that an invalid YAML file raises a YAMLError."""
        invalid_yaml_path = tmp_path / "invalid.yaml"
        invalid_yaml_path.write_text("key: value: another_value") # Malformed YAML

        temp_settings = settings.model_copy()
        temp_settings.QUANTUM_NEXUS_BLUEPRINT_PATH = str(invalid_yaml_path)

        with pytest.raises(yaml.YAMLError):
            QuantumNexus.from_settings(temp_settings)
