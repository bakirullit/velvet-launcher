# launcher/ui/pages/settings.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def build_page(state):
    """Build the Settings page."""
    
    main_box = toga.Box(style=Pack(
        direction=COLUMN,
        flex=1,
        padding=30
    ))
    
    # Title
    main_box.add(toga.Label(
        "Settings",
        style=Pack(font_size=20, font_weight="bold", padding_bottom=20)
    ))
    
    # Java Settings
    java_group = create_settings_group("Java Settings")
    java_path_input = toga.TextInput(
        value=state.settings.get("java_path", "java"),
        placeholder="Path to Java executable",
        style=Pack(flex=1, padding=10)
    )
    java_group.add(toga.Label("Java Path:", style=Pack(padding_bottom=5)))
    java_group.add(java_path_input)
    main_box.add(java_group)
    
    # Memory Settings
    memory_group = create_settings_group("Memory Settings")
    
    min_memory = toga.NumberInput(
        value=state.settings.get("memory_min", 512),
        style=Pack(padding=10)
    )
    memory_group.add(toga.Label("Minimum Memory (MB):", style=Pack(padding_bottom=5)))
    memory_group.add(min_memory)
    
    max_memory = toga.NumberInput(
        value=state.settings.get("memory_max", 2048),
        style=Pack(padding=10)
    )
    memory_group.add(toga.Label("Maximum Memory (MB):", style=Pack(padding_bottom=5, padding_top=10)))
    memory_group.add(max_memory)
    
    main_box.add(memory_group)
    
    # Theme Settings
    theme_group = create_settings_group("Appearance")
    theme_selection = toga.Selection(
        items=["Dark", "Light", "Auto"],
        value=state.settings.get("theme", "dark"),
        style=Pack(padding=10)
    )
    theme_group.add(toga.Label("Theme:", style=Pack(padding_bottom=5)))
    theme_group.add(theme_selection)
    main_box.add(theme_group)
    
    # Auto-update
    auto_update_group = create_settings_group("Updates")
    auto_update_switch = toga.Switch(
        value=state.settings.get("auto_update", True),
        style=Pack(padding=10)
    )
    auto_update_group.add(toga.Label("Auto-update launcher:", style=Pack(padding_bottom=5)))
    auto_update_group.add(auto_update_switch)
    main_box.add(auto_update_group)
    
    # Spacer
    main_box.add(toga.Box(style=Pack(flex=1)))
    
    # Save button
    save_btn = toga.Button(
        "Save Settings",
        on_press=lambda w: save_settings(state),
        style=Pack(padding=10)
    )
    main_box.add(save_btn)
    
    return main_box


def create_settings_group(title: str) -> toga.Box:
    """Create a styled settings group."""
    group = toga.Box(style=Pack(
        direction=COLUMN,
        padding=15,
        background_color="#f8f9fa",
        padding_bottom=15
    ))
    group.add(toga.Label(
        title,
        style=Pack(font_size=12, font_weight="bold", padding_bottom=10)
    ))
    return group


def save_settings(state):
    """Save settings to state."""
    state.save_settings()
    print("Settings saved!")
