from pyrustic.app import App
from hubway.misc import my_theme
from hubway.view.main_view import MainView


def main():
    # The App
    app = App()
    # Title
    app.title = "Hubway"
    # Geometry
    app.geometry = "900x550+0+0"
    # Resizable
    app.resizable = (False, False)
    # Set theme
    app.theme = my_theme.get_theme()
    # Set view
    app.view = MainView(app)
    # Center the window
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()
