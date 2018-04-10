from django.contrib import admin

# Register your models here.
from .models import Chambre, ChefReception, Client, EtatSalle, EtatTable, EtatChambre, Facture, Hotel, PrixChambreRepo, \
    TypeSalle, Table, TypePieceClient, TypeChambre, ReserverTable, MaitreHotel, Receptionnist, RelaisDomotique, \
    ReserverChambre, ReserverSalle

admin.site.register(Chambre)
admin.site.register(Client)
admin.site.register(ChefReception)
admin.site.register(TypeChambre)
admin.site.register(ReserverSalle)
admin.site.register(ReserverChambre)
admin.site.register(RelaisDomotique)
admin.site.register(EtatChambre)
admin.site.register(EtatTable)
admin.site.register(EtatSalle)
admin.site.register(Facture)
admin.site.register(Hotel)
admin.site.register(PrixChambreRepo)
admin.site.register(TypeSalle)
admin.site.register(Table)
admin.site.register(TypePieceClient)
admin.site.register(ReserverTable)
admin.site.register(MaitreHotel)
admin.site.register(Receptionnist)
