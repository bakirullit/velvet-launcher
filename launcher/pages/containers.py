# containers.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

def build_page(state):
    box = toga.Box(style=Pack(flex=1, margin=10, direction=COLUMN))
    for c in state.containers:
        btn = toga.Button(
            c["name"],
            on_press=lambda widget, cont=c: select_container(cont, state),
            style=Pack(margin=5, width=200)
        )
        box.add(btn)
    return box

def select_container(container, state):
    state.current_container = container
    print(f"Selected container: {container['name']}")