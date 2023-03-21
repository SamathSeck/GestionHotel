import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LoginForm(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Login Form")
        self.set_border_width(10)

        # Create Grid
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(10)
        grid.set_property("expand", True)
        self.add(grid)

        # Add Logo
        logo_image = Gtk.Image.new_from_file("logo.png")
        grid.attach(logo_image, 0, 0, 2, 1)

        # Add Username Label
        username_label = Gtk.Label(label="Username:")
        grid.attach(username_label, 0, 1, 1, 1)

        # Add Username Entry
        self.username_entry = Gtk.Entry()
        grid.attach(self.username_entry, 1, 1, 1, 1)

        # Add Password Label
        password_label = Gtk.Label(label="Password:")
        grid.attach(password_label, 0, 2, 1, 1)

        # Add Password Entry
        self.password_entry = Gtk.Entry()
        self.password_entry.set_visibility(False)
        grid.attach(self.password_entry, 1, 2, 1, 1)

        # Add Login Button
        login_button = Gtk.Button(label="Login")
        login_button.connect("clicked", self.on_login_button_clicked)
        grid.attach(login_button, 1, 3, 1, 1)

        # Center Window
        self.set_position(Gtk.WindowPosition.CENTER)

        # Set Window Size
        self.set_size_request(400, 250)

    def on_login_button_clicked(self, button):
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()

        # Code to authenticate user with given username and password

        print("Username: %s\nPassword: %s" % (username, password))

window = LoginForm()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
