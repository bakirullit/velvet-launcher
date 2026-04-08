# launcher/state.py
import json
from pathlib import Path
from datetime import datetime

class LauncherState:
    """Global launcher state with container management and persistence."""
    
    VELVET_DIR = Path.home() / ".velvet"
    CONTAINERS_FILE = VELVET_DIR / "containers.json"
    SETTINGS_FILE = VELVET_DIR / "settings.json"
    
    def __init__(self):
        # Ensure data directory exists
        self.VELVET_DIR.mkdir(parents=True, exist_ok=True)
        
        # Currently selected container
        self.current_container = None
        self.current_container_id = None
        
        # Load containers from disk or use defaults
        self.containers = self._load_containers()
        
        # Profiles (for multiple logins per container)
        self.profiles = {}
        
        # Settings
        self.settings = self._load_settings()
        
        # State callbacks for UI updates
        self._on_container_changed = None
        self._on_containers_modified = None

    def _load_containers(self) -> list:
        """Load containers from JSON file."""
        if self.CONTAINERS_FILE.exists():
            try:
                with open(self.CONTAINERS_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_containers()
        return self._get_default_containers()

    def _get_default_containers(self) -> list:
        """Return default containers for new installations."""
        return [
            {
                "id": "vanilla_1_20",
                "name": "Vanilla 1.20",
                "version": "1.20",
                "path": str(self.VELVET_DIR / "vanilla_1_20"),
                "description": "Vanilla Minecraft 1.20",
                "mods": [],
                "resources": [],
                "created_at": datetime.now().isoformat()
            },
            {
                "id": "forge_1_19_4",
                "name": "Forge 1.19.4",
                "version": "1.19.4",
                "path": str(self.VELVET_DIR / "forge_1_19_4"),
                "description": "Forge modded 1.19.4",
                "mods": [],
                "resources": [],
                "created_at": datetime.now().isoformat()
            }
        ]

    def _load_settings(self) -> dict:
        """Load settings from JSON file."""
        if self.SETTINGS_FILE.exists():
            try:
                with open(self.SETTINGS_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_settings()
        return self._get_default_settings()

    def _get_default_settings(self) -> dict:
        """Return default settings."""
        return {
            "java_path": "java",
            "memory_min": 512,
            "memory_max": 2048,
            "theme": "dark",
            "auto_update": True
        }

    def save_containers(self):
        """Persist containers to disk."""
        with open(self.CONTAINERS_FILE, 'w') as f:
            json.dump(self.containers, f, indent=2)
        if self._on_containers_modified:
            self._on_containers_modified()

    def save_settings(self):
        """Persist settings to disk."""
        with open(self.SETTINGS_FILE, 'w') as f:
            json.dump(self.settings, f, indent=2)

    def add_container(self, container_data: dict):
        """Add a new container."""
        container = {
            "id": container_data.get("id", f"container_{int(datetime.now().timestamp())}"),
            "name": container_data.get("name", "New Container"),
            "version": container_data.get("version", "1.20"),
            "path": container_data.get("path", str(self.VELVET_DIR / container_data.get("id", "new"))),
            "description": container_data.get("description", ""),
            "mods": container_data.get("mods", []),
            "resources": container_data.get("resources", []),
            "created_at": datetime.now().isoformat()
        }
        self.containers.append(container)
        self.save_containers()
        return container

    def update_container(self, container_id: str, updates: dict):
        """Update an existing container."""
        for container in self.containers:
            if container["id"] == container_id:
                container.update(updates)
                self.save_containers()
                return container
        return None

    def delete_container(self, container_id: str):
        """Delete a container."""
        self.containers = [c for c in self.containers if c["id"] != container_id]
        self.save_containers()

    def select_container(self, container_id: str):
        """Select the current container."""
        for container in self.containers:
            if container["id"] == container_id:
                self.current_container = container
                self.current_container_id = container_id
                if self._on_container_changed:
                    self._on_container_changed(container)
                return container
        return None

    def get_container(self, container_id: str) -> dict:
        """Get container by ID."""
        for container in self.containers:
            if container["id"] == container_id:
                return container
        return None

    def on_container_changed(self, callback):
        """Register callback for container selection changes."""
        self._on_container_changed = callback

    def on_containers_modified(self, callback):
        """Register callback for container list modifications."""
        self._on_containers_modified = callback