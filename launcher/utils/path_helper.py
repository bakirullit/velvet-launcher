# launcher/utils/path_helper.py
"""
Path and directory helpers for container management.
"""

from pathlib import Path


def get_container_path(container_id: str) -> Path:
    """Get the base directory path for a container."""
    from launcher.state import LauncherState
    return Path(LauncherState.VELVET_DIR) / container_id


def ensure_container_dirs(container_path: Path):
    """Ensure all necessary directories exist in a container."""
    required_dirs = [
        "mods",
        "resourcepacks",
        "shaderpacks",
        "config",
        "logs",
        "versions",
        "libraries",
        "assets"
    ]
    
    for dir_name in required_dirs:
        (container_path / dir_name).mkdir(parents=True, exist_ok=True)


def get_mods_dir(container_path: Path) -> Path:
    """Get the mods directory for a container."""
    mods_dir = container_path / "mods"
    mods_dir.mkdir(parents=True, exist_ok=True)
    return mods_dir


def get_resourcepacks_dir(container_path: Path) -> Path:
    """Get the resourcepacks directory for a container."""
    rp_dir = container_path / "resourcepacks"
    rp_dir.mkdir(parents=True, exist_ok=True)
    return rp_dir


def list_mods(container_path: Path) -> list:
    """List all mods in a container."""
    mods_dir = container_path / "mods"
    if not mods_dir.exists():
        return []
    return [f.name for f in mods_dir.glob("*.jar")]
