# launcher/__init__.py
"""
Velvet Launcher - Modular Minecraft Container Launcher
A Python/Toga-based launcher for managing isolated Minecraft environments (containers)
with support for multiple versions, mods, and server-specific configurations.
"""

__version__ = "0.1.0"
__author__ = "Velvet Team"

from .app import VelvetLauncher, run_launcher
from .minecraft import MinecraftLauncher
from .auth import ProfileManager
from .container import ContainerManager
from .states import LauncherState


__all__ = [
    "LauncherState",
    "VelvetLauncher",
    "run_launcher",
    "MinecraftLauncher",
    "ProfileManager",
    "ContainerManager"
]
