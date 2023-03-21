import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ReservationForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire de Réservation")

        # Layout
        grid = Gtk.Grid()
        self.add(grid)

        # Numéro de la chambre
        numero_label = Gtk.Label("Numéro de la chambre:")
        self.numero_entry = Gtk.Entry()
        grid.attach(numero_label, 0, 0, 1, 1)
        grid.attach(self.numero_entry, 1, 0, 1, 1)

        # Type de chambre
        type_label = Gtk.Label("Type de chambre:")
        self.type_combo = Gtk.ComboBoxText()
        self.type_combo.insert(0, "0", "Simple")
        self.type_combo.insert(1, "1", "Occupé")
        grid.attach(type_label, 0, 1, 1, 1)
        grid.attach(self.type_combo, 1, 1, 1, 1)

        # Date de réservation
        date_res_label = Gtk.Label("Date de réservation:")
        self.date_res_entry = Gtk.Entry()
        grid.attach(date_res_label, 0, 2, 1, 1)
        grid.attach(self.date_res_entry, 1, 2, 1, 1)

        # Date d'entrée
        date_entree_label = Gtk.Label("Date d'entrée:")
        self.date_entree_entry = Gtk.Entry()
        grid.attach(date_entree_label, 0, 3, 1, 1)
        grid.attach(self.date_entree_entry, 1, 3, 1, 1)
        
         # Date de sortie
        date_entree_label = Gtk.Label("Date de sortie:")
        self.date_entree_entry = Gtk.Entry()
        grid.attach(date_entree_label, 1, 3, 1, 1)
        grid.attach(self.date_entree_entry, 1, 3, 1, 1)

        # Bouton de soumission
        submit_button = Gtk.Button(label="Soumettre")
        submit_button.connect("clicked", self.submit_form)
        grid.attach(submit_button, 1, 4, 1, 1)

    def submit_form(self, button):
        # Récupération des valeurs entrées par l'utilisateur
        numero = self.numero_entry.get_text()
        type = self.type_combo.get_active_text()
        date_res = self.date_res_entry.get_text()
        date_entree = self.date_entree_entry.get_text()

        # Traitement des données (à compléter)

        # Affichage des données soumises
        print("Numéro de chambre:", numero)
        print("Type de chambre:", type)
        print("Date de réservation:", date_res)
        print("Date d'entrée:", date_entree)


win = ReservationForm()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()