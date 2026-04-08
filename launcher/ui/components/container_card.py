# launcher/ui/components/container_card.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ContainerCard(toga.Box):
    """Reusable container card component for displaying container info."""
    
    def __init__(self, container: dict, on_select=None, on_edit=None, on_delete=None):
        self.container = container
        self.on_select = on_select
        self.on_edit = on_edit
        self.on_delete = on_delete
        
        # Create card layout
        super().__init__(style=Pack(
            direction=COLUMN,
            padding=15,
            background_color="#f0f0f0",
            flex=1
        ))
        
        # Header with name and version
        header = toga.Box(style=Pack(direction=ROW, padding=(0, 0, 10, 0)))
        header.add(toga.Label(
            container["name"],
            style=Pack(font_size=14, font_weight="bold", flex=1)
        ))
        header.add(toga.Label(
            f"v{container['version']}",
            style=Pack(font_size=10, color="#666")
        ))
        self.add(header)
        
        # Description
        self.add(toga.Label(
            container.get("description", "No description"),
            style=Pack(font_size=10, color="#555", padding=(0, 0, 10, 0), flex=1)
        ))
        
        # Stats row
        stats = toga.Box(style=Pack(direction=ROW, padding=(0, 0, 10, 0)))
        stats.add(toga.Label(
            f"Mods: {len(container.get('mods', []))}",
            style=Pack(font_size=9, color="#777")
        ))
        stats.add(toga.Divider(style=Pack(width=1, padding=(0, 5))))
        stats.add(toga.Label(
            f"Resources: {len(container.get('resources', []))}",
            style=Pack(font_size=9, color="#777")
        ))
        self.add(stats)
        
        # Action buttons
        buttons = toga.Box(style=Pack(direction=ROW, padding_top=10))
        
        if on_select:
            buttons.add(toga.Button(
                "Select",
                on_press=lambda w: on_select(container),
                style=Pack(flex=1, padding_right=5)
            ))
        
        if on_edit:
            buttons.add(toga.Button(
                "Edit",
                on_press=lambda w: on_edit(container),
                style=Pack(flex=1, padding_right=5, padding_left=5)
            ))
        
        if on_delete:
            buttons.add(toga.Button(
                "Delete",
                on_press=lambda w: on_delete(container),
                style=Pack(flex=1, padding_left=5)
            ))
        
        self.add(buttons)


class StyledButton(toga.Button):
    """Reusable styled button component."""
    
    STYLE_PRIMARY = "primary"
    STYLE_SECONDARY = "secondary"
    STYLE_DANGER = "danger"
    
    def __init__(self, label: str, on_press=None, style_type: str = STYLE_PRIMARY, **kwargs):
        style_map = {
            self.STYLE_PRIMARY: Pack(padding=10, background_color="#007acc"),
            self.STYLE_SECONDARY: Pack(padding=10, background_color="#6c757d"),
            self.STYLE_DANGER: Pack(padding=10, background_color="#dc3545"),
        }
        
        super().__init__(
            label,
            on_press=on_press,
            style=style_map.get(style_type, style_map[self.STYLE_PRIMARY]),
            **kwargs
        )


class DialogBox(toga.Box):
    """Base dialog component for modals."""
    
    def __init__(self, title: str, content_widget: toga.Widget, buttons: list = None):
        super().__init__(style=Pack(direction=COLUMN, padding=20))
        
        # Title
        self.add(toga.Label(
            title,
            style=Pack(font_size=16, font_weight="bold", padding_bottom=15)
        ))
        
        # Content
        self.add(content_widget)
        
        # Buttons
        if buttons:
            button_box = toga.Box(style=Pack(direction=ROW, padding_top=20))
            for btn in buttons:
                button_box.add(btn)
            self.add(button_box)
