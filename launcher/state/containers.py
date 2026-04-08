# launcher/state/containers.py
"""
Container state utilities for advanced container management.
Can be extended for complex container operations.
"""

from typing import Dict, List


class ContainerFilter:
    """Filter containers by various criteria."""
    
    def __init__(self, containers: List[Dict]):
        self.containers = containers
    
    def by_version(self, version: str) -> List[Dict]:
        """Filter containers by Minecraft version."""
        return [c for c in self.containers if c.get("version") == version]
    
    def by_name(self, name_fragment: str) -> List[Dict]:
        """Filter containers by name (partial match)."""
        return [c for c in self.containers if name_fragment.lower() in c.get("name", "").lower()]
    
    def with_mods(self) -> List[Dict]:
        """Get containers that have mods installed."""
        return [c for c in self.containers if len(c.get("mods", [])) > 0]
    
    def without_mods(self) -> List[Dict]:
        """Get containers without mods (vanilla)."""
        return [c for c in self.containers if len(c.get("mods", [])) == 0]
    
    def sort_by_created(self, reverse: bool = False) -> List[Dict]:
        """Sort containers by creation date."""
        return sorted(self.containers, key=lambda c: c.get("created_at", ""), reverse=reverse)
