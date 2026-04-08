# Velvet Launcher

A modular Minecraft launcher built with Python and Toga, designed for managing multiple isolated Minecraft containers (environments) with support for modpacks, multi-version play, and server-specific configurations.

## Features

- **Isolated Containers**: Each container is a fully isolated Minecraft environment with its own mods, resources, and settings
- **One-Click Container Switching**: Fixed sidebar navigation; switch containers instantly
- **Container Sharing**: Share containers with others including mods, resources, and optional custom login
- **Multi-Version Support**: Manage multiple Minecraft versions simultaneously
- **Modded Server Support**: Full support for Forge, Fabric, and other mod loaders
- **Scalable Architecture**: Clean separation of concerns with modular design
- **Cross-Platform**: Built with Toga for native UI on Windows, macOS, and Linux

## Project Structure

```
velvet-launcher/
├── main.py                 # Entry point
├── launcher/
│   ├── __init__.py        # Package initialization
│   ├── app.py             # Main Toga application
│   ├── state.py           # Global state management with persistence
│   ├── auth.py            # Profile/account management
│   ├── minecraft.py       # Minecraft launcher integration
│   ├── container.py       # Container management utilities
│   ├── init.py            # Initialization and setup
│   ├── ui/
│   │   ├── __init__.py    # UI utilities and sidebar builder
│   │   ├── pages/         # Page implementations
│   │   │   ├── home.py    # Home page with current container info
│   │   │   ├── containers.py # Container management page
│   │   │   └── settings.py   # Settings page
│   │   └── components/    # Reusable UI components
│   │       ├── container_card.py # Container card component
│   │       └── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── svg_helper.py  # SVG to PNG conversion
│       └── path_helper.py # Path and directory utilities
├── assets/
│   └── icons/             # SVG icons (dynamically converted to PNG)
│       └── .cache/        # Generated PNG cache
├── config/
│   └── default_profile.json
└── README.md
```

## Installation & Setup

### Requirements

- Python 3.9+
- Toga (GUI framework)
- cairosvg (for SVG conversion)
- minecraft_launcher_lib (for Minecraft integration)

### Install Dependencies

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install toga cairosvg minecraft_launcher_lib
```

### Run the Launcher

```bash
python main.py
```

## Architecture

### State Management (`launcher/state.py`)

- `LauncherState` manages containers, settings, and current selection
- All data persists to JSON files in `~/.velvet/`
- Containers stored in `~/.velvet/containers.json`
- Settings stored in `~/.velvet/settings.json`

**Key Methods:**
- `add_container()` - Create a new container
- `update_container()` - Modify container data
- `delete_container()` - Remove a container
- `select_container()` - Switch active container
- `save_containers()` / `save_settings()` - Persist to disk

### Containers

Each container is an isolated environment stored in `~/.velvet/<container_id>/`:

```
container_id/
├── mods/              # Installed mods
├── resourcepacks/     # Resource packs
├── shaderpacks/       # Shaders
├── config/            # Mod configs
├── logs/              # Game logs
├── versions/          # Minecraft versions
├── libraries/         # Libraries cache
├── assets/            # Game assets
└── metadata.json      # Container metadata
```

### UI Components

**Pages:**
- **Home**: Shows current container, launch button, mod management quick access
- **Containers**: List all containers with create/edit/delete options, container cards with stats
- **Settings**: Configure Java path, memory, theme, and launcher preferences

**Reusable Components** (`launcher/ui/components/`):
- `ContainerCard` - Displays container info and action buttons
- `StyledButton` - Pre-styled buttons (primary, secondary, danger)
- `DialogBox` - Base modal dialog component

### Minecraft Integration (`launcher/minecraft.py`)

`MinecraftLauncher` class provides:
- `launch()` - Launch Minecraft in a container with isolated environment
- `stop()` - Gracefully stop running instance
- `install_mods()` - Install mods into container

**TODO**: Integrate with `minecraft_launcher_lib` for actual launcher command building.

## Container Management

### Creating Containers

```python
from launcher.container import ContainerManager

manager = ContainerManager()
container = manager.create_container(
    container_id="modpack_1_20",
    name="My Modpack 1.20",
    version="1.20",
    description="Custom modpack for survival"
)
```

### Container Sharing

Containers can be packaged and shared as `.zip` files including:
- All mods in `mods/`
- Resource packs in `resourcepacks/`
- Configuration files in `config/`
- Optional: Custom launcher profile

## Configuration

Default settings stored in `config/default_profile.json`:

```json
{
  "java_path": "java",
  "memory_min": 512,
  "memory_max": 2048,
  "theme": "dark",
  "auto_update": true
}
```

## Authentication

Manage multiple Minecraft profiles:

```python
from launcher.auth import ProfileManager

pm = ProfileManager()
pm.add_profile("username", {
    "login_type": "microsoft",  # or "offline"
    "email": "user@example.com"
})
```

## Asset Management

- All launcher icons are stored as SVG in `assets/icons/`
- SVG files are automatically converted to PNG at runtime
- Generated PNGs are cached in `assets/icons/.cache/` to avoid repeated conversions
- Original SVG files are never modified

## Development

### Adding a New Page

1. Create file in `launcher/ui/pages/your_page.py`
2. Implement `build_page(state)` function
3. Add navigation button in `launcher/ui/__init__.py` `build_sidebar()`
4. Add page handler in `launcher/app.py` (e.g., `show_your_page()`)

### Adding UI Components

1. Create component class in `launcher/ui/components/`
2. Export in `launcher/ui/components/__init__.py`
3. Use in pages

## Future Enhancements

- [ ] Complete minecraft_launcher_lib integration
- [ ] Container import/export functionality
- [ ] Mod manager UI with CurseForge/Modrinth integration
- [ ] Profile/account authentication (Microsoft, offline)
- [ ] Auto-update functionality
- [ ] Container sync to cloud storage
- [ ] Multiplayer server quick-join
- [ ] Advanced logging and diagnostics
- [ ] Performance profiling integration

## Contributing

Contributions welcome! Please ensure:
- Code follows existing style and structure
- All new features include documentation
- UI components are reusable and well-styled
- State changes persist to disk

## License

[Add your license here]

## Troubleshooting

### SVG Conversion Issues

If icons don't appear, check:
```bash
# Verify cairosvg is installed
python -c "import cairosvg; print(cairosvg.__version__)"

# Check cache directory
ls -la assets/icons/.cache/
```

### Container Loading Issues

Containers are stored in `~/.velvet/containers.json`. Check:
```bash
cat ~/.velvet/containers.json
```

### State Persistence

All state changes are automatically saved. To reset:
```bash
rm -rf ~/.velvet/
```

## Support

For issues and questions, please open an issue on the repository.
