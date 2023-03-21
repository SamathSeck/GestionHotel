import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HeaderBar(Gtk.HeaderBar):

    def __init__(self):
        Gtk.HeaderBar.__init__(self)
        self.set_title("Hotel 5 Etoiles")
        self.set_show_close_button(True)

        # Ajouter un bouton Accueil
        home_button = Gtk.Button(label="Accueil")
        self.pack_start(home_button)

        # Ajouter un bouton Services
        services_button = Gtk.Button(label="Services")
        self.pack_start(services_button)

        # Ajouter un bouton À propos
        about_button = Gtk.Button(label="À propos")
        self.pack_start(about_button)

        # Ajouter un bouton de connexion
        connect_button = Gtk.Button(label="Se connecter")
        connect_button.connect("clicked", self.on_connect_clicked)
        self.pack_end(connect_button)

        # Ajouter un bouton de déconnexion (masqué au départ)
        disconnect_button = Gtk.Button(label="Se déconnecter")
        disconnect_button.connect("clicked", self.on_disconnect_clicked)
        self.pack_end(disconnect_button)
        #disconnect_button.set_visible(False)

    def on_connect_clicked(self, button):
        # Cacher le bouton de connexion et afficher le bouton de déconnexion
        connect_button = self.get_children()[-2]
        disconnect_button = self.get_children()[-1]
        #connect_button.set_visible(False)
        disconnect_button.set_visible(True)
        from connexion import ClientWindow
        win = ClientWindow()
        win.show_all()

    def on_disconnect_clicked(self, button):
        # Cacher le bouton de déconnexion et afficher le bouton de connexion
        connect_button = self.get_children()[-2]
        disconnect_button = self.get_children()[-1]
        connect_button.set_visible(True)
        #disconnect_button.set_visible(False)


class MainPage(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel 5 Etoiles")

        # Ajouter l'entête à la fenêtre principale
        header_bar = HeaderBar()
        self.set_titlebar(header_bar)

         # Crée une grille pour les boutons
        grid = Gtk.Grid(column_spacing=50, row_spacing=30)
        self.add(grid)

        # Crée les boutons avec les libellés respectifs
        button_chambre = Gtk.Button(label="Chambre")
        button_client = Gtk.Button(label="Client")
        button_annexe = Gtk.Button(label="Annexe")
        button_autre = Gtk.Button(label="Autre")

        # Ajoute les boutons à la grille
        grid.attach(button_chambre, 0, 0, 1, 1)
        grid.attach(button_client, 1, 0, 1, 1)
        grid.attach(button_annexe, 0, 1, 1, 1)
        grid.attach(button_autre, 1, 1, 1, 1)

         # Connecte chaque bouton à sa page respective
        button_chambre.connect("clicked", self.open_chambre)
        button_client.connect("clicked", self.open_client)
        button_annexe.connect("clicked", self.open_annexe)
        button_autre.connect("clicked", self.open_autre)

    # Ouvre la page de la chambre
    def open_chambre(self, widget):
        from chambre import ChambreWindow
        win = ChambreWindow()
        win.show_all()

    # Ouvre la page du client
    def open_client(self, widget):
        from client import ClientWindow
        win = ClientWindow()
        win.show_all()

    # Ouvre la page de l'annexe
    def open_annexe(self, widget):
        from annexe import AnnexeWindow
        win = AnnexeWindow()
        win.show_all()

    # Ouvre la page autre
    def open_autre(self, widget):
        from autre import AutreWindow
        win = AutreWindow()
        win.show_all()
        
        image = Gtk.Image()
        image.set_from_file("hotel2.png")
        # tester


window = MainPage()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()



