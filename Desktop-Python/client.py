import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire de saisie")

        # Créer une grille pour organiser les widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Ajouter un champ de saisie pour le nom
        name_label = Gtk.Label(label="Nom : ")
        name_entry = Gtk.Entry()
        grid.attach(name_label, 0, 0, 1, 1)
        grid.attach(name_entry, 1, 0, 1, 1)
        
        # Ajouter un champ de saisie pour le prenom
        prenom_label = Gtk.Label(label="Preom : ")
        prenom_entry = Gtk.Entry()
        grid.attach(prenom_label, 0, 1, 1, 1)
        grid.attach(prenom_entry, 1, 1, 1, 1)

        # Ajouter un champ de saisie pour l'adresse e-mail
        email_label = Gtk.Label(label="Adresse e-mail : ")
        email_entry = Gtk.Entry()
        grid.attach(email_label, 1, 1, 1, 1)
        grid.attach(email_entry, 1, 1, 1, 1)

        # Ajouter un champ de saisie pour l'âge
        age_label = Gtk.Label(label="Âge : ")
        age_spinbutton = Gtk.SpinButton()
        age_spinbutton.set_range(0, 120)
        grid.attach(age_label, 0, 2, 1, 1)
        grid.attach(age_spinbutton, 1, 2, 1, 1)

        # Ajouter une liste déroulante pour le sexe
        sex_label = Gtk.Label(label="Sexe : ")
        sex_combo = Gtk.ComboBoxText()
        sex_combo.append_text("Homme")
        sex_combo.append_text("Femme")

        grid.attach(sex_label, 0, 3, 1, 1)
        grid.attach(sex_combo, 1, 3, 1, 1)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()