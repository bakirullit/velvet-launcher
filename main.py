import flet as ft
from flet import *
import json
servers = ["add_server", "nextgen"]
white_theme = [""]

f = open('config/themes/dark_theme.json')
themes = json.load(f)

tabs = {
    "startup": 0,
    "update": 1,
    "vanilla": 2,
    "profile": 3,
    "settings": 4,
    "add_server": 5,
    "add_run": 6,
    "nextgen": 7,
}

icons = {
        "settings": ft.icons.SETTINGS,
        "profile": ft.icons.PERSON,
        "plus": ft.icons.ADD,
        "servers": ft.icons.ANDROID,
    }

def main(page: ft.Page):
    page.title = 'Velvet Launcher'
    page.window_width = 1200
    page.window_height = 700 
    page.window_resizable = False
    page.update()
    def change_tab(tab_n):
        print(tab_n)
        page.drawer.open = False
        main_content.selected_index=tab_n
        print(tab_n/2-tab_n//2==0.5 and tab_n >= 3)
        if not(tab_n/2-tab_n//2==0.5 and tab_n >= 3):
            page.drawer.selected_index = -1
        page.update()
    def changes(index_ch):
        print("Current route: ", ft.Page.route)
        print("Changing route to: ", servers[index_ch], " - ", index_ch)
        main_content = ft.Text("Nofvsdvsfvvv clickable", color=themes["third-color"])
        ft.Page.route = '/' + servers[index_ch]
        print("Current route: ", ft.Page.route)
        if index_ch == 0:
            print("Opening Dialog - 1")
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            #page.update()
            print(1234)

    page.window_prevent_close = False
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def save_server():
        pass
    messages = ft.Column()
    user = ft.TextField(hint_text="Your name", width=150)
    message = ft.TextField(hint_text="Your message...", expand=True)
    send = ft.ElevatedButton("Send")
    dialog_content=messages, ft.Row(controls=[user, message, send])

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Adding new server"),
        content=dialog_content,

        actions=[
            ft.TextButton("Cancel", on_click=close_dlg),
            ft.TextButton("Save", on_click=save_server),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    main_content = ft.Tabs(
        selected_index=0,
        animation_duration=0,
        tab_alignment=ft.TabAlignment.FILL,
        tabs=[
            ft.Tab(
                content=ft.Text("This is Tab 1"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 4"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 5"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 6"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 7"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 8"),
            ),
        ],
        expand=1,
    )
    page.drawer = ft.NavigationDrawer(
        bgcolor=themes["primary-color"],
        on_change = lambda e: change_tab(7+2*(int(page.drawer.selected_index)-1)),
        selected_index=-1,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                icon=icons["plus"],
                label="Add Server",
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.IconButton(icon=icons["settings"], on_click=lambda _: print("LOOL")),
                label="NextGen",
            ),
        ],
    )

    page.end_drawer = ft.NavigationDrawer(
        bgcolor=themes["primary-color"],
        on_change = lambda e: change_tab(8+2*(int(page.drawer.selected_index)-1)),
        selected_index=-1,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                icon=icons["plus"],
                label="Add New Run",
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.IconButton(icon=icons["settings"], on_click=lambda _: print("LOOL")),
                label="Last Run",
            ),
        ],
    )

    def show_end_drawer(e):
        page.end_drawer.open = True
        page.end_drawer.update()

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()
    
    header = ft.AppBar(
        bgcolor=themes["primary-color"],
        leading=ft.IconButton(icon=icons["plus"], on_click=show_drawer),
        actions=[
            ft.IconButton(icon=icons["servers"], on_click=show_end_drawer),
            ft.IconButton(icon=icons["profile"], on_click=lambda _: change_tab(tabs["profile"])),
            ft.IconButton(icon=icons["settings"], on_click=lambda _: change_tab(tabs["settings"])),
        ],
    )
    main_container = ft.Container(
        content=main_content,
        padding=0,
        width=1170,
        height=700,
        alignment=ft.alignment.center,
        bgcolor=themes["primary-color"],
        border_radius=10,
    )
    
    M_row = ft.Row(
        spacing=0,
        controls=[
            main_container
        ],
    )
                
    
    
    
    
    page.update()
    page.add(header)
    page.add(M_row)
ft.app(target=main)
