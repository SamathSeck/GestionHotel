import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ServiceForm(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire de service")
        self.set_border_width(10)

        # Création d'une grille pour organiser les éléments
        grid = Gtk.Grid()
        self.add(grid)

        # Ajout des options pour le café
        coffee_label = Gtk.Label("Café - 2.50$")
        self.coffee_checkbox = Gtk.CheckButton()
        self.coffee_checkbox.connect("toggled", self.on_checkbox_toggled, 2.50)
        grid.attach(coffee_label, 0, 0, 1, 1)
        grid.attach(self.coffee_checkbox, 1, 0, 1, 1)

        # Ajout des options pour le déjeuner
        lunch_label = Gtk.Label("Déjeuner - 12.00$")
        self.lunch_checkbox = Gtk.CheckButton()
        self.lunch_checkbox.connect("toggled", self.on_checkbox_toggled, 12.00)
        grid.attach(lunch_label, 0, 1, 1, 1)
        grid.attach(self.lunch_checkbox, 1, 1, 1, 1)

        # Ajout des options pour le téléphone
        phone_label = Gtk.Label("Téléphone - 5.00$")
        self.phone_checkbox = Gtk.CheckButton()
        self.phone_checkbox.connect("toggled", self.on_checkbox_toggled, 5.00)
        grid.attach(phone_label, 0, 2, 1, 1)
        grid.attach(self.phone_checkbox, 1, 2, 1, 1)

        # Ajout des options pour le bar
        bar_label = Gtk.Label("Bar - 8.00$")
        self.bar_checkbox = Gtk.CheckButton()
        self.bar_checkbox.connect("toggled", self.on_checkbox_toggled, 8.00)
        grid.attach(bar_label, 0, 3, 1, 1)
        grid.attach(self.bar_checkbox, 1, 3, 1, 1)

        # Ajout d'un bouton pour calculer le total
        self.total_button = Gtk.Button(label="Valider")
        self.total_button.connect("clicked", self.on_total_button_clicked)
        grid.attach(self.total_button, 0, 4, 2, 1)

        # Ajout d'un champ de texte pour afficher le total
        self.total_label = Gtk.Label(label="")
        grid.attach(self.total_label, 0, 5, 2, 1)

    def on_checkbox_toggled(self, button, price):
        # Calcule le prix total en fonction des options sélectionnées
        if button.get_active():
            self.total += price
        else:
            self.total -= price

    def on_total_button_clicked(self, button):
        # Affiche le prix total dans le champ de texte
        self.total_label.set_label("Total: " + str(self.total) + "$")

win = ServiceForm()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()