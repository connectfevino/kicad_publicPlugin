

from pcbnew import *
import wx


class publicPlugin(ActionPlugin):
    """
    This is a simple plugin that demonstrates how to create a plugin for KiCad.
    It will display a message box when the plugin is executed.
    """

    def defaults(self):
        self.name = "Public Plugin"
        self.category = "Example Plugins"
        self.description = "A simple plugin that demonstrates how to create a plugin for KiCad."
        self.show_toolbar_button = True
        self.icon_file_name = ""

    def Run(self):
        wx.MessageBox("Hello from the Public Plugin!", "Public Plugin", wx.OK | wx.ICON_INFORMATION)


publicPlugin().register()