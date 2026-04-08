# launcher/ui/pages/containers.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from launcher.ui.components import ContainerCard, StyledButton


def build_page(state):
    """Build the Containers page for managing containers."""
    
    main_box = toga.Box(style=Pack(
        direction=COLUMN,
        flex=1,
        padding=20
    ))
    
    # Header
    header = toga.Box(style=Pack(direction=ROW, padding_bottom=20))
    header.add(toga.Label(
        "Containers",
        style=Pack(font_size=20, font_weight="bold", flex=1)
    ))
    
    # Create new container button
    create_btn = toga.Button(
        "+ New Container",
        on_press=lambda w: show_create_container_dialog(state),
        style=Pack(padding=5)
    )
    header.add(create_btn)
    main_box.add(header)
    
    # Search bar (optional enhancement)
    search_box = toga.Box(style=Pack(direction=ROW, padding_bottom=15))
    search_box.add(toga.TextInput(
        placeholder="Search containers...",
        style=Pack(flex=1, padding_right=10)
    ))
    main_box.add(search_box)
    
    # Containers list (scrollable)
    scroll_container = toga.Box(style=Pack(
        direction=COLUMN,
        flex=1
    ))
    
    if state.containers:
        for container in state.containers:
            card = ContainerCard(
                container,
                on_select=lambda c, app_state=state: select_container(c, app_state),
                on_edit=lambda c: show_edit_container_dialog(c, state),
                on_delete=lambda c: delete_container_confirm(c, state)
            )
            scroll_container.add(card)
    else:
        scroll_container.add(toga.Label(
            "No containers yet. Create one to get started!",
            style=Pack(font_size=12, color="#999", padding=20)
        ))
    
    main_box.add(scroll_container)
    
    return main_box


def select_container(container, state):
    """Select a container and update state."""
    state.select_container(container["id"])
    print(f"Selected container: {container['name']}")


def show_create_container_dialog(state):
    """Show dialog to create a new container."""
    print("Create container dialog - not yet implemented")
    # TODO: Implement container creation dialog


def show_edit_container_dialog(container, state):
    """Show dialog to edit a container."""
    print(f"Edit container dialog for {container['name']} - not yet implemented")
    # TODO: Implement container edit dialog


def delete_container_confirm(container, state):
    """Confirm and delete a container."""
    print(f"Delete container {container['name']} - confirmation not yet implemented")
    # TODO: Implement delete confirmation and state update
