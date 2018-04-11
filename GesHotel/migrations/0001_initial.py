# Generated by Django 2.0.4 on 2018-04-10 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_chambre', models.IntegerField(null=True, verbose_name='Numero Chambre')),
                ('prix_nuit', models.FloatField(verbose_name='Prix Nuit')),
                ('nbr_places', models.IntegerField(null=True, verbose_name='Nombre de Places')),
                ('status_chambre', models.BooleanField(default=True, verbose_name='Status Chambre')),
            ],
        ),
        migrations.CreateModel(
            name='ChefReception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_piece', models.CharField(max_length=200, verbose_name='Numero de Piece')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom Receptionist')),
                ('prenom', models.CharField(max_length=200, verbose_name='Prenom')),
                ('tel', models.CharField(max_length=8, unique=True, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('statut_recep', models.BooleanField(default=True, verbose_name='Statut du chef Receptionist')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_piece', models.CharField(max_length=200, unique=True, verbose_name='Numero de Piece')),
                ('nom_cli', models.CharField(max_length=100, verbose_name='Nom Receptionist')),
                ('prenom_cli', models.CharField(max_length=250, verbose_name='Prenom')),
                ('tel_cli', models.CharField(max_length=8, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('statut', models.BooleanField(default=False, verbose_name='Statut Client')),
                ('date_inscrip', models.DateTimeField(auto_now_add=True, verbose_name='Date INscription')),
                ('nationalite_cli', models.CharField(max_length=200, verbose_name='Nationalité')),
            ],
        ),
        migrations.CreateModel(
            name='EtatChambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat_chambre', models.CharField(max_length=150, unique=True, verbose_name='Etat Chambre')),
                ('statut', models.BooleanField(default=True, verbose_name='Status Chambre')),
            ],
        ),
        migrations.CreateModel(
            name='EtatSalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100, verbose_name='Etat Salle')),
                ('statut_salle', models.BooleanField(default=True, verbose_name='Statut Salle')),
            ],
        ),
        migrations.CreateModel(
            name='EtatTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100, verbose_name='Etat Table')),
                ('statut_table', models.BooleanField(default=False, verbose_name='Statut Table')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facture', models.DateTimeField(auto_now_add=True, verbose_name='Date INscription')),
                ('montant', models.IntegerField(null=True, verbose_name='Montant facture')),
                ('statut', models.BooleanField(default=False, verbose_name='Statut facture')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payer', to='GesHotel.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_hotel', models.CharField(max_length=200, verbose_name='Nom Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='MaitreHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_piece', models.CharField(max_length=200, verbose_name='Numero de Piece')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom Maitre Hotel')),
                ('prenom', models.CharField(max_length=250, verbose_name='Prenom Maitre Hotel')),
                ('tel', models.CharField(max_length=8, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('statut_maitr', models.BooleanField(default=True, verbose_name="Statut du Maitre d'Hotel")),
            ],
        ),
        migrations.CreateModel(
            name='PrixChambreRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_repos_heure', models.FloatField(verbose_name='Prix Repos /Heur')),
                ('heure', models.IntegerField(null=True, verbose_name='Heure')),
                ('chambres', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Couter', to='GesHotel.Chambre')),
            ],
        ),
        migrations.CreateModel(
            name='Receptionnist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_piece', models.CharField(max_length=200, verbose_name='Numero de Piece')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom Receptionist')),
                ('prenom', models.CharField(max_length=250, verbose_name='Prenom')),
                ('tel', models.CharField(max_length=8, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('statut_recep', models.BooleanField(default=True, verbose_name='Statut du Receptionist')),
            ],
        ),
        migrations.CreateModel(
            name='RelaisDomotique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conso_electricite', models.IntegerField(verbose_name='Consomation Electricité')),
                ('statut_relait', models.BooleanField(default=False, verbose_name='Statut Relais')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='COnso_1', to='GesHotel.Chambre')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='COnso_2', to='GesHotel.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ReserverChambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_arriver', models.DateTimeField(auto_now_add=True, verbose_name='Date Arriver')),
                ('date_sorti', models.DateTimeField(auto_now_add=True, verbose_name='Date Sortie')),
                ('date_reservation', models.DateTimeField(auto_now_add=True, verbose_name='Date Reservation')),
                ('statut_reservation', models.BooleanField(default=False, verbose_name='Statut Reservation')),
                ('chambres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_chambre', to='GesHotel.Chambre')),
                ('maitrehotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gerer_chambre', to='GesHotel.MaitreHotel')),
                ('receptionnists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_chambre', to='GesHotel.Receptionnist')),
            ],
        ),
        migrations.CreateModel(
            name='ReserverSalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbr_personnes', models.IntegerField(null=True, verbose_name='Nombe Personnes')),
                ('date_reservation', models.DateTimeField(auto_now_add=True, verbose_name='Date Reservation')),
                ('date_commande_creer', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation Commande')),
                ('statut_reservation', models.BooleanField(default=False, verbose_name='Statut Reservation')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_salle', to='GesHotel.Client')),
                ('receptionnists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_salle', to='GesHotel.Receptionnist')),
            ],
        ),
        migrations.CreateModel(
            name='ReserverTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbr_personnes', models.IntegerField(null=True, verbose_name='Nombe Personnes')),
                ('date_reservation', models.DateTimeField(auto_now_add=True, verbose_name='Date Reservation')),
                ('date_commande_creer', models.DateTimeField(auto_now_add=True, verbose_name='Date Creation Commande')),
                ('statut_reservation', models.BooleanField(default=False, verbose_name='Statut Reservation')),
                ('receptionnists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_table', to='GesHotel.Receptionnist')),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.FloatField()),
                ('statut_table', models.BooleanField(default=False, verbose_name='Statut Table')),
                ('etatsalles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Etre_dans', to='GesHotel.EtatSalle')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_table', models.IntegerField(null=0, unique=True, verbose_name='Numero Table')),
                ('nbr_palces', models.IntegerField(null=True, verbose_name='Nombre de Places')),
                ('statut_table', models.BooleanField(default=False, verbose_name='Statut Table')),
                ('tarif', models.FloatField(verbose_name='Tarif')),
                ('etattable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Etre_dans', to='GesHotel.EtatTable')),
                ('maitrehotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gerer_Table', to='GesHotel.MaitreHotel')),
            ],
        ),
        migrations.CreateModel(
            name='TypeChambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_chambre', models.CharField(max_length=150, unique=True, verbose_name='Type Chambre')),
                ('statut', models.BooleanField(default=True, verbose_name='Status Chambre')),
            ],
        ),
        migrations.CreateModel(
            name='TypePieceClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_piece', models.CharField(max_length=200, unique=True, verbose_name='Type Piece')),
                ('statut', models.BooleanField(default=True, verbose_name='Statut Pièce')),
            ],
        ),
        migrations.CreateModel(
            name='TypeSalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True, verbose_name='Type Salle')),
                ('statut_type', models.BooleanField(default=False, verbose_name='Statut Type')),
            ],
        ),
        migrations.AddField(
            model_name='salle',
            name='typesalles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Constituer', to='GesHotel.TypeSalle'),
        ),
        migrations.AddField(
            model_name='reservertable',
            name='salles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_table', to='GesHotel.Salle'),
        ),
        migrations.AddField(
            model_name='reservertable',
            name='tables',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_table', to='GesHotel.Table'),
        ),
        migrations.AddField(
            model_name='reserversalle',
            name='salles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_salle', to='GesHotel.Salle'),
        ),
        migrations.AddField(
            model_name='reserverchambre',
            name='salles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserver_chambre', to='GesHotel.Salle'),
        ),
        migrations.AddField(
            model_name='client',
            name='typepiececlient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appartenir', to='GesHotel.TypePieceClient'),
        ),
        migrations.AddField(
            model_name='chambre',
            name='chefreception',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gerer', to='GesHotel.ChefReception'),
        ),
        migrations.AddField(
            model_name='chambre',
            name='etatchambres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Voir', to='GesHotel.EtatChambre'),
        ),
        migrations.AddField(
            model_name='chambre',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gerer', to='GesHotel.Hotel'),
        ),
        migrations.AddField(
            model_name='chambre',
            name='typechambre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Avoir', to='GesHotel.TypeChambre'),
        ),
    ]
