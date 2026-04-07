# home.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

def build_page(state):
    return toga.Box(
        children=[toga.Label("Welcome to Velvet Launcher!")],
        style=Pack(flex=1, margin=20, direction=COLUMN)
    )