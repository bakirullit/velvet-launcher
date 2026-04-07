# launcher/app.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from launcher.pages import home, settings, containers
from launcher.state import LauncherState

from launcher.ui import build_sidebar
class VelvetLauncher(toga.App):
    def _create_impl(self):
        factory_app = self.factory.App
        factory_app.create_menus = lambda _: None
        return []
    
    def startup(self):
        self.state = LauncherState()

        self.content_area = toga.Box(style=Pack(flex=1))

        sidebar = build_sidebar(self)

        root = toga.Box(
            children=[sidebar, self.content_area],
            style=Pack(direction=ROW, flex=1)
        )

        self.main_window = toga.MainWindow(
            title="Velvet Launcher",
            size=(1400, 900)
        )

        self.main_window.content = root
        self.show_home()
        self.main_window.show()

    def show_home(self, widget=None):
        self.set_page(home.build_page(self.state))

    def show_containers(self, widget=None):
        self.set_page(containers.build_page(self.state))

    def show_settings(self, widget=None):
        self.set_page(settings.build_page(self.state))

    def set_page(self, page):
        self.content_area.clear()
        self.content_area.add(page)


def run_launcher():
    app = VelvetLauncher(
        "Velvet Launcher",
        "org.velvet.launcher"
    )
    app.main_loop()
