from django.db import models


# Create your models here.
#


class TypeChambre(models.Model):
    """ Table stature de la chambre"""
    type_chambre = models.CharField(max_length=150, verbose_name="Type Chambre", unique=True)
    statut = models.BooleanField(verbose_name="Status Chambre", default=True)


class EtatChambre(models.Model):
    """ Table stature de la chambre"""
    etat_chambre = models.CharField(max_length=150, verbose_name="Etat Chambre", unique=True)
    statut = models.BooleanField(verbose_name="Status Chambre", default=True)


class ChefReception(models.Model):
    """ Table chef de reception"""
    num_piece = models.CharField(max_length=200, verbose_name="Numero de Piece")
    nom = models.CharField(max_length=100, verbose_name="Nom Receptionist")
    prenom = models.CharField(max_length=200, verbose_name="Prenom")
    tel = models.CharField(max_length=8, verbose_name="Téléphone", unique=True)
    email = models.EmailField(max_length=100, verbose_name="E-mail", unique=True)
    statut_recep = models.BooleanField(verbose_name="Statut du chef Receptionist", default=True)


class Hotel(models.Model):
    """ Table Hotel"""
    nom_hotel = models.CharField(max_length=200, verbose_name="Nom Hotel")

    def __str__(self):
        """ Afficher le nom de l'hotel"""
        return self.nom_hotel


class Chambre(models.Model):
    """ Table chambre"""
    num_chambre = models.IntegerField(verbose_name="Numero Chambre", null=True)
    prix_nuit = models.FloatField(verbose_name="Prix Nuit")
    nbr_places = models.IntegerField(verbose_name="Nombre de Places", null=True)
    status_chambre = models.BooleanField(verbose_name="Status Chambre", default=True)
    etatchambres = models.ForeignKey(EtatChambre, on_delete=models.CASCADE, related_name="Voir")
    typechambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE, related_name="Avoir")
    chefreception = models.ForeignKey(ChefReception, on_delete=models.PROTECT, related_name="Gerer")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="Gerer")


class PrixChambreRepo(models.Model):
    """ Table prix lore d'un passage de repos """
    prix_repos_heure = models.FloatField(verbose_name="Prix Repos /Heur")
    heure = models.IntegerField(verbose_name="Heure", null=True)
    chambres = models.ForeignKey(Chambre, on_delete=models.PROTECT, related_name="Couter")


class MaitreHotel(models.Model):
    """ Maitre de l'hote"""
    num_piece = models.CharField(max_length=200, verbose_name="Numero de Piece")
    nom = models.CharField(max_length=100, verbose_name="Nom Maitre Hotel")
    prenom = models.CharField(max_length=250, verbose_name="Prenom Maitre Hotel")
    tel = models.CharField(max_length=8, verbose_name="Téléphone")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    statut_maitr = models.BooleanField(verbose_name="Statut du Maitre d'Hotel", default=True)
    # tables = models.ForeignKey(Table, on_delete=models.SET_DEFAULT)


class Receptionnist(models.Model):
    """ Table chef de reception"""
    num_piece = models.CharField(max_length=200, verbose_name="Numero de Piece")
    nom = models.CharField(max_length=100, verbose_name="Nom Receptionist")
    prenom = models.CharField(max_length=250, verbose_name="Prenom")
    tel = models.CharField(max_length=8, verbose_name="Téléphone")
    email = models.EmailField(max_length=100, verbose_name="E-mail", unique=True)
    statut_recep = models.BooleanField(verbose_name="Statut du Receptionist", default=True)


class TypePieceClient(models.Model):
    """ Type de piece occuper par le client """
    type_piece = models.CharField(max_length=200, unique=True, verbose_name="Type Piece")
    statut = models.BooleanField(verbose_name="Statut Pièce", default=True)


class Client(models.Model):
    """ Table client"""
    num_piece = models.CharField(max_length=200, verbose_name="Numero de Piece", unique=True)
    nom_cli = models.CharField(max_length=100, verbose_name="Nom Receptionist")
    prenom_cli = models.CharField(max_length=250, verbose_name="Prenom")
    tel_cli = models.CharField(max_length=8, verbose_name="Téléphone")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    statut = models.BooleanField(verbose_name="Statut Client", default=False)
    date_inscrip = models.DateTimeField(auto_now_add=True, verbose_name="Date INscription")
    nationalite_cli = models.CharField(max_length=200, verbose_name="Nationalité")
    typepiececlient = models.ForeignKey(TypePieceClient, on_delete=models.CASCADE, related_name="Appartenir")


class RelaisDomotique(models.Model):
    """ Relais domotique (eletricité)"""
    conso_electricite = models.IntegerField(verbose_name="Consomation Electricité")
    statut_relait = models.BooleanField(verbose_name="Statut Relais", default=False)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="COnso_2")
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name="COnso_1")


class Facture(models.Model):
    """ Facture de consomation du client"""
    date_facture = models.DateTimeField(auto_now_add=True, verbose_name="Date INscription")
    montant = models.IntegerField(null=True, verbose_name="Montant facture")
    statut = models.BooleanField(verbose_name="Statut facture", default=False)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="Payer")


class EtatTable(models.Model):
    """ Etat de la table"""
    etat = models.CharField(max_length=100, verbose_name="Etat Table")
    statut_table = models.BooleanField(verbose_name="Statut Table", default=False)


class Table(models.Model):
    """ Table accuper par un client"""
    num_table = models.IntegerField(null=0, verbose_name="Numero Table", unique=True)
    nbr_palces = models.IntegerField(null=True, verbose_name="Nombre de Places")
    statut_table = models.BooleanField(verbose_name="Statut Table", default=False)
    tarif = models.FloatField(verbose_name="Tarif")
    maitrehotel = models.ForeignKey(MaitreHotel, on_delete=models.CASCADE, related_name="Gerer_Table")
    etattable = models.ForeignKey(EtatTable, on_delete=models.CASCADE, related_name="Etre_dans")


class EtatSalle(models.Model):
    """ Etat de la table"""
    etat = models.CharField(max_length=100, verbose_name="Etat Salle")
    statut_salle = models.BooleanField(verbose_name="Statut Salle", default=True)


class TypeSalle(models.Model):
    """ Etat de la table"""
    type = models.CharField(max_length=100, verbose_name="Type Salle", unique=True)
    statut_type = models.BooleanField(verbose_name="Statut Type", default=False)


class Salle(models.Model):
    """ Table Salle"""
    tarif = models.FloatField()
    statut_table = models.BooleanField(verbose_name="Statut Table", default=False)
    typesalles = models.ForeignKey(TypeSalle, on_delete=models.CASCADE, related_name="Constituer")
    etatsalles = models.ForeignKey(EtatSalle, on_delete=models.CASCADE, related_name="Etre_dans")


class ReserverChambre(models.Model):
    """ Table relation reservation chambre"""
    date_arriver = models.DateTimeField(auto_now_add=True, verbose_name="Date Arriver")
    date_sorti = models.DateTimeField(auto_now_add=True, verbose_name="Date Sortie")
    date_reservation = models.DateTimeField(auto_now_add=True, verbose_name="Date Reservation")
    statut_reservation = models.BooleanField(verbose_name="Statut Reservation", default=False)
    maitrehotels = models.ForeignKey(MaitreHotel, on_delete=models.CASCADE, related_name="Gerer_chambre")
    salles = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name="Reserver_chambre")
    receptionnists = models.ForeignKey(Receptionnist, on_delete=models.CASCADE, related_name="Reserver_chambre")
    chambres = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name="Reserver_chambre")


class ReserverSalle(models.Model):
    """ Table relation reservation salle"""
    nbr_personnes = models.IntegerField(verbose_name="Nombe Personnes", null=True)
    date_reservation = models.DateTimeField(auto_now_add=True, verbose_name="Date Reservation")
    date_commande_creer = models.DateTimeField(auto_now_add=True, verbose_name="Date Creation Commande")
    statut_reservation = models.BooleanField(verbose_name="Statut Reservation", default=False)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="Reserver_salle")
    salles = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name="Reserver_salle")
    receptionnists = models.ForeignKey(Receptionnist, on_delete=models.CASCADE, related_name="Reserver_salle")


class ReserverTable(models.Model):
    """ Table relation reservation salle"""
    nbr_personnes = models.IntegerField(verbose_name="Nombe Personnes", null=True)
    date_reservation = models.DateTimeField(auto_now_add=True, verbose_name="Date Reservation")
    date_commande_creer = models.DateTimeField(auto_now_add=True, verbose_name="Date Creation Commande")
    statut_reservation = models.BooleanField(verbose_name="Statut Reservation", default=False)
    salles = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name="Reserver_table")
    receptionnists = models.ForeignKey(Receptionnist, on_delete=models.CASCADE, related_name="Reserver_table")
    tables = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="Reserver_table")
