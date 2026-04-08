# Development Guide

## Project Overview

Velvet Launcher is a modular Minecraft launcher built with Python and Toga. The codebase is organized to be scalable and maintainable with clear separation of concerns.

## Code Organization

### Core Modules

**`launcher/state.py`** - Global Application State
- Manages containers, settings, and profiles
- Handles persistence to JSON files
- Provides callbacks for UI updates
- Entry point: `LauncherState` class

**`launcher/app.py`** - Toga Application
- Main application class `VelvetLauncher`
- Page routing and navigation
- UI lifecycle management

**`launcher/container.py`** - Container Management
- `ContainerManager` class for CRUD operations
- Container creation, duplication, deletion
- Metadata persistence

**`launcher/minecraft.py`** - Minecraft Integration
- `MinecraftLauncher` class
- Launch management, mod installation
- Environment variable setup

**`launcher/auth.py`** - Account Management
- `ProfileManager` for user accounts
- Multiple profile support
- Profile persistence

### UI Structure

```
launcher/ui/
├── __init__.py           # build_sidebar() and icon() helpers
├── pages/                # Full page implementations
│   ├── home.py          # Landing page
│   ├── containers.py    # Container management
│   └── settings.py      # Launcher settings
└── components/          # Reusable UI widgets
    └── container_card.py # Card components
```

### Utilities

**`launcher/utils/svg_helper.py`** - SVG Processing
- Converts SVG icons to PNG
- Caches generated PNGs

**`launcher/utils/path_helper.py`** - Path Management
- Container directory structure helpers
- Cross-platform path handling

**`launcher/state/containers.py`** - Container Filtering
- `ContainerFilter` for advanced queries
- Sorting and filtering operations

## Adding Features

### Adding a New Page

1. **Create page file** in `launcher/ui/pages/your_page.py`:

```python
# launcher/ui/pages/your_page.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def build_page(state):
    """Build your page UI."""
    main_box = toga.Box(style=Pack(direction=COLUMN, flex=1, padding=20))
    
    # Add widgets to main_box
    main_box.add(toga.Label("Your Page"))
    
    return main_box
```

2. **Add page method** to `VelvetLauncher` in `launcher/app.py`:

```python
def show_your_page(self, widget=None):
    self.set_page(your_page.build_page(self.state))
```

3. **Add import** at top of `launcher/app.py`:

```python
from launcher.ui.pages import your_page
```

4. **Add sidebar button** in `launcher/ui/__init__.py` `build_sidebar()`:

```python
nav.add(toga.Button(icon=icon("your-icon-name"), on_press=self.show_your_page))
```

### Adding a Reusable Component

1. **Create component** in `launcher/ui/components/your_component.py`:

```python
# launcher/ui/components/your_component.py
import toga
from toga.style import Pack

class YourComponent(toga.Box):
    def __init__(self, **kwargs):
        super().__init__(style=Pack(padding=10))
        # Component implementation
```

2. **Export in** `launcher/ui/components/__init__.py`:

```python
from .your_component import YourComponent

__all__ = ["YourComponent", ...]
```

3. **Use in pages**:

```python
from launcher.ui.components import YourComponent

your_component = YourComponent()
main_box.add(your_component)
```

### Adding State Functionality

Extend `LauncherState` in `launcher/state.py`:

```python
class LauncherState:
    def new_method(self):
        """Your new method."""
        pass
    
    def save_state(self):
        """Always call save when modifying state."""
        self.save_containers()
        self.save_settings()
```

State changes are automatically persisted to:
- `~/.velvet/containers.json` - Container data
- `~/.velvet/settings.json` - Launcher settings
- `~/.velvet/profiles.json` - User profiles

## Styling Patterns

### Consistent Padding

```python
# Outer containers
Pack(padding=20)

# Component sections
Pack(padding=15, background_color="#f8f9fa")

# Individual items
Pack(padding=(top, right, bottom, left))
```

### Color Scheme

- **Primary**: `#007acc` (blue)
- **Danger**: `#dc3545` (red)
- **Background**: `#f8f9fa` (light gray)
- **Text**: `#333`, `#555` (dark), `#999` (muted)

### Layouts

Always use:
```python
Pack(direction=COLUMN, flex=1)      # Vertical layout
Pack(direction=ROW, flex=1)         # Horizontal layout
```

`flex=1` makes the widget expand to fill available space.

## Container File Structure

When creating containers, always create these directories:

```
container_id/
├── mods/              # Mod files (.jar)
├── resourcepacks/     # Resource pack files (.zip)
├── shaderpacks/       # Shader files
├── config/            # Mod configuration files
├── logs/              # Game log files
├── versions/          # Game versions
├── libraries/         # Library files
├── assets/            # Game assets
└── metadata.json      # Container metadata
```

Use `launcher/utils/path_helper.py` helpers:

```python
from launcher.utils.path_helper import ensure_container_dirs, get_mods_dir

ensure_container_dirs(container_path)
mods_dir = get_mods_dir(container_path)
```

## State Management Patterns

### Updating State with Callbacks

```python
# Register callbacks for state changes
def on_container_changed(container):
    print(f"Container changed to {container['name']}")

state.on_container_changed(on_container_changed)

# Select a container (triggers callback)
state.select_container("container_id")
```

### Modifying Containers

```python
# Add container
state.add_container({
    "id": "my_container",
    "name": "My Container",
    "version": "1.20"
})

# Update container
state.update_container("my_container", {
    "description": "Updated description"
})

# Delete container
state.delete_container("my_container")

# Always save after modifications
state.save_containers()
```

## Testing Guidelines

### Manual Testing Checklist

1. **Container Operations**
   - Create container ✓
   - Select container ✓
   - Update container ✓
   - Delete container ✓
   - Verify persistence ✓

2. **UI Navigation**
   - Navigate between pages ✓
   - Sidebar icons responsive ✓
   - Content area updates ✓

3. **Data Persistence**
   - Create container → close app → reopen → data persists ✓
   - Change settings → close app → reopen → settings persisted ✓

## Common Patterns

### Dialog/Modal Pattern

```python
from launcher.ui.components import DialogBox

dialog = DialogBox(
    title="Confirm Action",
    content_widget=toga.Label("Are you sure?"),
    buttons=[
        toga.Button("Yes", on_press=on_yes),
        toga.Button("No", on_press=on_no)
    ]
)
```

### Async Operations Pattern

For long operations (downloading, launching):

```python
import threading

def long_operation():
    # Do work here
    pass

thread = threading.Thread(target=long_operation, daemon=True)
thread.start()
```

### Error Handling

```python
try:
    # Operation
    pass
except Exception as e:
    print(f"Error occurred: {e}")
    # Show error dialog to user
```

## Performance Considerations

### Lazy Loading

Load containers and data only when needed:

```python
# Don't: Load all containers on startup
containers = state.get_all_containers()

# Do: Load filtered/paginated containers
containers = state.get_containers_by_version("1.20")
```

### Caching

SVG to PNG conversion is automatically cached. Don't re-convert.

### Threading

- Long operations (Minecraft launch, downloads) should run in background threads
- UI updates from threads must use proper Toga threading patterns

## Troubleshooting

### Import Errors

Ensure all `__init__.py` files are present in packages:
- `launcher/__init__.py`
- `launcher/ui/__init__.py`
- `launcher/ui/pages/__init__.py`
- `launcher/ui/components/__init__.py`
- `launcher/utils/__init__.py`
- `launcher/state/__init__.py`

### State Persistence Issues

Check `~/.velvet/` directory:
```bash
ls -la ~/.velvet/
cat ~/.velvet/containers.json
```

### SVG Icon Issues

```bash
python -c "import cairosvg; print('OK')"
ls launcher/ui/components/icons/.cache/
```

## Future Development

### High Priority

- [ ] minecraft_launcher_lib integration
- [ ] Container import/export UI
- [ ] Mod manager with mod search
- [ ] Minecraft account authentication

### Medium Priority

- [ ] Cloud container sync
- [ ] Performance profiling
- [ ] Advanced logging
- [ ] Plugin system

### Low Priority

- [ ] Theme customization
- [ ] Launcher skinning
- [ ] Multiplayer quick-join
- [ ] Rich analytics

## Code Style

- Follow PEP 8 Python style guide
- Use type hints for function parameters and returns
- Add docstrings to all public methods
- Keep functions focused and under 50 lines when possible
- Use descriptive variable names

## Contributing

When contributing:

1. Create a feature branch
2. Make atomic commits with clear messages
3. Follow code style guidelines
4. Test thoroughly
5. Update README if adding features
6. Create pull request with description

## Resources

- [Toga Documentation](https://toga.readthedocs.io/)
- [minecraft_launcher_lib](https://github.com/minecraft-launcher-lib/minecraft-launcher-lib)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [SVG Best Practices](https://developer.mozilla.org/en-US/docs/Web/SVG)
