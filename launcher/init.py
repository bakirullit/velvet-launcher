# launcher/init.py
"""
Initialization utilities for setting up the launcher environment.
"""

import json
from pathlib import Path


def init_launcher():
    """Initialize launcher directories and configuration."""
    from launcher.states import LauncherState
    
    # Create main directory
    LauncherState.VELVET_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create default config if it doesn't exist
    config_template = {
        "version": "1.0",
        "created_at": "2024-01-01",
        "settings": {
            "java_path": "java",
            "memory_min": 512,
            "memory_max": 2048,
            "theme": "dark",
            "auto_update": True
        }
    }
    
    config_file = Path(__file__).parent.parent / "config" / "default_profile.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    
    if not config_file.exists():
        with open(config_file, 'w') as f:
            json.dump(config_template, f, indent=2)


def migrate_legacy_containers():
    """Migrate containers from old format to new format."""
    # TODO: Implement migration logic if upgrading from older versions
    pass
