# launcher/container.py
import os
import json

def load_containers(containers_dir):
    containers = []
    if not os.path.exists(containers_dir):
        os.makedirs(containers_dir)

    for folder in os.listdir(containers_dir):
        path = os.path.join(containers_dir, folder)
        profile_path = os.path.join(path, "profile.json")
        if os.path.isdir(path) and os.path.exists(profile_path):
            try:
                with open(profile_path, "r") as f:
                    profile = json.load(f)
                containers.append({
                    "name": folder,
                    "path": path,
                    "profile": profile
                })
            except Exception as e:
                print(f"Failed to load container {folder}: {e}")
    return containers

# launcher/container.py
def select_container(container, state):
    state.current_container = container
    print(f"Selected container: {container['name']}")

def launch_selected(state, launch_minecraft_fn):
    if state.current_container:
        print(f"Launching Minecraft from {state.current_container['name']}...")
        launch_minecraft_fn(state.current_container)
    else:
        print("No container selected!")