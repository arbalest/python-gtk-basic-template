import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root = Gtk.Paned()

        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        sidebar.get_style_context().add_class('view')
        sidebar_title = Gtk.Label(label="Sidebar")
        sidebar_title.get_style_context().add_class('sidebar-title')
        sidebar.pack_start(sidebar_title, True, True, 5)

        workspace = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        workspace.get_style_context().add_class('workspace')
        workspace_title = Gtk.Label(label="Workspace")
        workspace.pack_start(workspace_title, True, True, 5)
        
        self.root.add1(sidebar)
        self.root.add2(workspace)
        self.add(self.root)
        self.show_all()


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.ethanhorger.python-gtk-basic-template", **kwargs)
        self.window = None
        self.load_css()

    def load_css(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('./app.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def do_activate(self):
        if self.window == None:
            self.window = ApplicationWindow(title="Python GTK Basic Template", application=self)
        self.window.show()


if __name__ == '__main__':
    app = Application()
    app.run()