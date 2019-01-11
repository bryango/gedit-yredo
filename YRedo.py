from gi.repository import GObject, Gedit, Gio


class YRedoPluginWindow(GObject.Object, Gedit.WindowActivatable):
    window = GObject.Property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        action = Gio.SimpleAction(name="yredo")
        action.connect('activate', self._yredo_activate)
        self.window.add_action(action)

    def _yredo_activate(self, action, parameter, user_data=None):
        doc = self.window.get_active_document()
        if not doc:
            return
        doc.redo()


class YRedoPlugin(GObject.Object, Gedit.AppActivatable):
    __gtype_name__ = "YRedoPlugin"
    app = GObject.Property(type=Gedit.App)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self.app.set_accels_for_action("win.yredo", [
            "<Control>Y"
        ])
        # self.menu_ext = self.extend_menu("tools-section")
        # item = Gio.MenuItem.new("YRedo", "win.yredo")
        # self.menu_ext.prepend_menu_item(item)

    def do_deactivate(self):
        self.app.set_accels_for_action("win.redo", [])
        # self.menu_ext = None

    def do_update_state(self):
        pass
