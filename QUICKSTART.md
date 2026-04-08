# Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies

```bash
# Navigate to project
cd /home/bakirullit/Desktop/velvet-launcher

# Create virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install required packages
pip install toga cairosvg
```

### 2. Run the Launcher

```bash
python main.py
```

## What You'll See

### Home Page
- Welcome message
- Current container info (if selected)
- Launch button placeholder
- Quick access to container management

### Containers Page
- List of available containers
- Create new container button
- Container cards showing:
  - Name and version
  - Description
  - Number of mods and resources
  - Select/Edit/Delete buttons

### Settings Page
- Java path configuration
- Memory settings (min/max)
- Theme selection
- Auto-update toggle
- Save button

## First Steps

### 1. Create a Container

1. Navigate to **Containers** page (click folder icon in sidebar)
2. Click **"+ New Container"** button
3. Enter container details
4. Click **Create**

### 2. Select a Container

1. On **Containers** page, find your container
2. Click the **Select** button
3. Navigate to **Home** - you'll see your container selected

### 3. Configure Settings

1. Click settings icon (⚙) in sidebar
2. Update Java path if needed
3. Adjust memory settings
4. Choose your theme
5. Click **Save Settings**

## Project Structure Quick Reference

```
velvet-launcher/
├── main.py                    # START HERE - Entry point
├── launcher/
│   ├── app.py                 # Main Toga app
│   ├── state.py               # Data management
│   ├── minecraft.py           # Launch integration
│   ├── container.py           # Container management
│   ├── auth.py                # Account profiles
│   ├── ui/pages/              # Page implementations
│   │   ├── home.py
│   │   ├── containers.py
│   │   └── settings.py
│   └── ui/components/         # Reusable widgets
│       └── container_card.py
├── config/                    # Configuration files
├── assets/icons/              # SVG icons
└── README.md                  # Full documentation
```

## Key Concepts

### Containers
- **Isolated Minecraft environments** - Each container has its own mods, resources, settings
- **Persistent** - Stored in `~/.velvet/` on your computer
- **Shareable** - Can be packaged and shared with others

### State Management
- **Automatic saving** - All changes persist to disk
- **Global state** - Accessible from any page
- **Callbacks** - Pages can respond to state changes

### UI Architecture
- **Fixed sidebar** - Navigation icons always visible
- **Dynamic content area** - Changes when you select a page
- **Reusable components** - Cards, buttons, dialogs can be used anywhere

## Common Tasks

### Add More Containers

Edit `~/.velvet/containers.json`:
```json
{
  "id": "vanilla_1_20",
  "name": "Vanilla 1.20",
  "version": "1.20",
  ...
}
```

### View Stored Data

```bash
# See all containers
cat ~/.velvet/containers.json

# See all settings
cat ~/.velvet/settings.json

# See all profiles
cat ~/.velvet/profiles.json
```

### Reset Everything

```bash
# Remove all launcher data (keeps installed Minecraft)
rm -rf ~/.velvet/containers.json ~/.velvet/settings.json

# The app will regenerate defaults on next start
```

## Troubleshooting

### App won't start

```bash
# Check Python version (need 3.9+)
python --version

# Check if packages installed
pip list | grep -E "toga|cairosvg"

# Try reinstalling
pip install --upgrade toga cairosvg
```

### Icons not showing

```bash
# Check if cairosvg works
python -c "import cairosvg; print('OK')"

# Check cache directory
ls -la launcher/ui/components/icons/.cache/
```

### Containers not saving

```bash
# Check if directory exists
ls -la ~/.velvet/

# Check file permissions
ls -la ~/.velvet/containers.json

# Check file contents
cat ~/.velvet/containers.json
```

## Next Steps

- 📖 Read [DEVELOPMENT.md](DEVELOPMENT.md) for detailed architecture
- 📚 Read [README.md](README.md) for full documentation
- 🔧 Explore the `launcher/` directory to understand the code
- ✨ Start customizing and adding features!

## Keyboard Shortcuts

Currently implemented shortcuts:
- *Tab* - Navigate between buttons and fields
- *Enter* - Activate buttons and dialogs
- *Ctrl+Q* - Quit application (OS dependent)

## Performance Tips

- Keep the number of containers reasonable (50+ may slow UI)
- Large mod files will take time to process
- Use SSDs for better container loading
- Keep `~/.velvet/` on local drive (not network)

## Getting Help

1. Check [DEVELOPMENT.md](DEVELOPMENT.md) for architecture details
2. Look at existing pages and components for patterns
3. Check console output for error messages
4. Review state persistence files in `~/.velvet/`

## What's Next?

The launcher provides a solid foundation. You can:

1. **Integrate Minecraft** - Add minecraft_launcher_lib integration
2. **Add Mod Manager** - Search and install mods from CurseForge/Modrinth
3. **Cloud Sync** - Sync containers to cloud storage
4. **Authentication** - Add Microsoft account login
5. **Advanced Features** - Performance profiling, cloud backups, etc.

Happy launching! 🚀
