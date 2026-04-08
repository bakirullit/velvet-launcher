# launcher/auth.py
"""
Authentication and profile management for Minecraft accounts.
Handles storing and retrieving login credentials securely.
"""

import json
from pathlib import Path
from datetime import datetime


class ProfileManager:
    """Manages Minecraft profiles/accounts for containers."""
    
    PROFILES_FILE = Path.home() / ".velvet" / "profiles.json"
    
    def __init__(self):
        self.profiles = self._load_profiles()
    
    def _load_profiles(self) -> dict:
        """Load profiles from disk."""
        if self.PROFILES_FILE.exists():
            try:
                with open(self.PROFILES_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def save_profiles(self):
        """Save profiles to disk."""
        self.PROFILES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(self.PROFILES_FILE, 'w') as f:
            json.dump(self.profiles, f, indent=2)
    
    def add_profile(self, username: str, profile_data: dict) -> bool:
        """
        Add or update a profile.
        
        Args:
            username: Minecraft username
            profile_data: Profile data dict (can include custom launcher login)
        
        Returns:
            True if successful
        """
        self.profiles[username] = {
            "username": username,
            "created_at": self.profiles.get(username, {}).get("created_at", datetime.now().isoformat()),
            "last_login": datetime.now().isoformat(),
            **profile_data
        }
        self.save_profiles()
        return True
    
    def get_profile(self, username: str) -> dict:
        """Get a specific profile."""
        return self.profiles.get(username)
    
    def list_profiles(self) -> list:
        """List all profiles."""
        return list(self.profiles.keys())
    
    def delete_profile(self, username: str) -> bool:
        """Delete a profile."""
        if username in self.profiles:
            del self.profiles[username]
            self.save_profiles()
            return True
        return False
