# launcher/ui/__init__.py
import toga
from toga.style import Pack
from pathlib import Path
from launcher.utils.svg_helper import svg_to_png
from toga.style.pack import COLUMN, ROW

ASSETS = Path(__file__).parent.parent / "assets" / "icons"

def icon(name: str, size: int = 28) -> toga.Icon:
    svg = ASSETS / f"{name}.svg"
    png = svg_to_png(svg, size)
    return toga.Icon(str(png))

def build_sidebar(self):
    nav = toga.Box(style=Pack(direction=COLUMN, flex=1))

    nav.add(toga.Button(icon=icon(
        "door-home-home-page-homepage-house"
    ), on_press=self.show_home))

    nav.add(toga.Button(icon=icon(
        "archive-document-file-folder-format-page"
    ), on_press=self.show_containers))

    spacer = toga.Box(style=Pack(flex=1))
    nav.add(spacer)

    nav.add(toga.Button(icon=icon(
        "configuration-gear-options-preferences-settings-system"
    ), on_press=self.show_settings))

    sidebar = toga.Box(
        children=[nav],
        style=Pack(
            direction=COLUMN,
            width=70,
            margin=5
        )
    )

    return sidebar
