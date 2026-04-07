# launcher/state.py
class State:
    def __init__(self):
        self.containers = []        # List of dicts: {"name": ..., "path": ..., "profile": {...}}
        self.current_container = None

class LauncherState:
    def __init__(self):
        # Currently selected container
        self.current_container = None

        # Example list of containers
        # In real use, you might load these from disk or a server
        self.containers = [
            {"name": "Vanilla 1.20", "path": "/home/user/.velvet/vanilla_1_20"},
            {"name": "Forge 1.19.4", "path": "/home/user/.velvet/forge_1_19_4"},
        ]

        # Profiles (later for multiple users or logins)
        self.profiles = []

        # Settings
        self.settings = {}