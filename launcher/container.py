# launcher/container.py
"""
Container management for isolated Minecraft environments.
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict


class ContainerManager:
    """Manages container creation, deletion, and configuration."""
    
    def __init__(self, base_path: Path = None):
        self.base_path = base_path or Path.home() / ".velvet"
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def create_container(self, container_id: str, name: str, version: str, 
                        description: str = "") -> Dict:
        """
        Create a new container.
        
        Args:
            container_id: Unique identifier for the container
            name: Display name
            version: Minecraft version
            description: Optional description
        
        Returns:
            The created container dict
        """
        container_path = self.base_path / container_id
        container_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        for subdir in ["mods", "resourcepacks", "shaderpacks", "config", "logs", "versions", "libraries", "assets"]:
            (container_path / subdir).mkdir(exist_ok=True)
        
        container = {
            "id": container_id,
            "name": name,
            "version": version,
            "path": str(container_path),
            "description": description,
            "mods": [],
            "resources": [],
            "created_at": datetime.now().isoformat()
        }
        
        # Save metadata
        metadata_file = container_path / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(container, f, indent=2)
        
        return container
    
    def delete_container(self, container_id: str) -> bool:
        """
        Delete a container and all its files.
        
        Args:
            container_id: ID of the container to delete
        
        Returns:
            True if deletion was successful
        """
        container_path = self.base_path / container_id
        if container_path.exists():
            try:
                shutil.rmtree(container_path)
                return True
            except Exception as e:
                print(f"Failed to delete container: {e}")
                return False
        return False
    
    def load_container(self, container_id: str) -> Optional[Dict]:
        """Load container metadata from disk."""
        metadata_file = self.base_path / container_id / "metadata.json"
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Failed to load container: {e}")
        return None
    
    def save_container(self, container: Dict) -> bool:
        """Save container metadata to disk."""
        container_path = Path(container["path"])
        metadata_file = container_path / "metadata.json"
        try:
            with open(metadata_file, 'w') as f:
                json.dump(container, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save container: {e}")
            return False
    
    def duplicate_container(self, source_id: str, new_id: str, new_name: str) -> Optional[Dict]:
        """
        Duplicate a container with all its contents.
        
        Args:
            source_id: ID of source container
            new_id: ID for the new container
            new_name: Display name for new container
        
        Returns:
            The new container dict, or None if failed
        """
        source_path = self.base_path / source_id
        if not source_path.exists():
            return None
        
        new_path = self.base_path / new_id
        try:
            shutil.copytree(source_path, new_path)
            
            # Update metadata
            container = self.load_container(new_id)
            if container:
                container["id"] = new_id
                container["name"] = new_name
                container["path"] = str(new_path)
                self.save_container(container)
                return container
        except Exception as e:
            print(f"Failed to duplicate container: {e}")
        
        return None


def launch_selected(state, launch_minecraft_fn):
    if state.current_container:
        print(f"Launching Minecraft from {state.current_container['name']}...")
        launch_minecraft_fn(state.current_container)
    else:
        print("No container selected!")