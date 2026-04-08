# launcher/ui/pages/home.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def build_page(state):
    """Build the Home page showing current container and launch options."""
    
    main_box = toga.Box(style=Pack(
        direction=COLUMN,
        flex=1,
        padding=30
    ))
    
    # Title
    main_box.add(toga.Label(
        "Velvet Launcher",
        style=Pack(font_size=28, font_weight="bold", padding_bottom=10)
    ))
    
    main_box.add(toga.Label(
        "Modular Minecraft Container Launcher",
        style=Pack(font_size=12, color="#666", padding_bottom=30)
    ))
    
    # Current container section
    if state.current_container:
        container_box = toga.Box(style=Pack(
            direction=COLUMN,
            padding=20,
            background_color="#f8f9fa"
        ))
        
        container_box.add(toga.Label(
            "Current Container",
            style=Pack(font_size=14, font_weight="bold", padding_bottom=10)
        ))
        
        container_box.add(toga.Label(
            state.current_container["name"],
            style=Pack(font_size=18, font_weight="bold", padding_bottom=5)
        ))
        
        container_box.add(toga.Label(
            state.current_container.get("description", ""),
            style=Pack(font_size=11, color="#555", padding_bottom=15)
        ))
        
        # Stats
        stats_text = (
            f"Version: {state.current_container['version']} | "
            f"Mods: {len(state.current_container.get('mods', []))} | "
            f"Resources: {len(state.current_container.get('resources', []))}"
        )
        container_box.add(toga.Label(
            stats_text,
            style=Pack(font_size=10, color="#777", padding_bottom=20)
        ))
        
        # Launch button
        button_box = toga.Box(style=Pack(direction=ROW))
        button_box.add(toga.Button(
            "▶ Launch Minecraft",
            style=Pack(padding=10, font_size=12)
        ))
        button_box.add(toga.Button(
            "⚙ Manage Mods",
            style=Pack(padding=10, font_size=12, padding_left=5)
        ))
        
        container_box.add(button_box)
        main_box.add(container_box)
        
    else:
        # No container selected
        main_box.add(toga.Label(
            "No container selected.",
            style=Pack(font_size=12, color="#999", padding=20)
        ))
        main_box.add(toga.Label(
            "Go to Containers to select or create one.",
            style=Pack(font_size=11, color="#999")
        ))
    
    # Spacer
    main_box.add(toga.Box(style=Pack(flex=1)))
    
    # Footer
    main_box.add(toga.Label(
        "Tip: Switch containers from the Containers page",
        style=Pack(font_size=9, color="#aaa", padding_top=20)
    ))
    
    return main_box
