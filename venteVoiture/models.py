
from django.db import models


class User(models.Model):
    objects = None
    SEXE_CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Non-binaire', 'Non-binaire'),
    )

    nomUser = models.CharField(max_length=100)
    prenomUser = models.CharField(max_length=100)
    email = models.EmailField()
    sexe = models.CharField(max_length=20, choices=SEXE_CHOICES)
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    # Autres champs pour les informations relatives à l'utilisateur


class Order(models.Model):
    objects = None
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCommande = models.DateTimeField(auto_now_add=True)
    statutCommande = models.BooleanField(default=False)  # Champ booléen pour le statut de la commande
    # Autres champs pour les informations relatives à la commande


class Item(models.Model):
    objects = None
    nomItem = models.CharField(max_length=100)
    descriptionItem = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey('CategoryPieces', on_delete=models.CASCADE)
    statutItem = models.BooleanField(default=False)
    # Autres champs pour les informations relatives à la pièce


class CategoryPieces(models.Model):
    objects = None
    CAT_PIECE_CHOICE = (
        ('Mécanique', 'Mécanique'),
        ('Electrique', 'Electrique'),
    )
    nomCatPiece = models.CharField(max_length=31, choices=CAT_PIECE_CHOICE)
    # Autres champs pour les informations relatives à la catégorie de pièces


class Garage(models.Model):
    objects = None
    nomGarage = models.CharField(max_length=100)
    adresseGarage = models.CharField(max_length=200)
    localisation = models.OneToOneField('Location', on_delete=models.CASCADE)
    # Autres champs pour les informations relatives au garage


class Location(models.Model):
    objects = None
    quartier = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Autres champs pour les informations relatives à la localisation


class Cart(models.Model):
    objects = None
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    # Autres champs pour les informations relatives au panier


class Vehicle(models.Model):
    objects = None
    marque = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    numPlaque = models.CharField(max_length=20)
    nombreCylindres = models.PositiveIntegerField()
    typeBoiteVitesse = models.BooleanField(default=False)  # Champ booléen pour le type de boîte de vitesse
    assurance = models.BooleanField(default=False)  # Champ booléen pour l'assurance
    numChassis = models.CharField(max_length=100)
    # Autres champs pour les informations relatives au véhicule


class VehicleCategory(models.Model):
    objects = None
    CAT_VEHICULE_CHOICE = (
        ('Mini-citadines', 'Mini-citadines'),
        ('Petites voitures', 'Petites voitures'),
        ('Voitures compactes', 'Voitures compactes'),
        ('Grosses voitures', 'Grosses voitures'),
        ('Voitures de prestige', 'Voitures de prestige'),
        ('Voitures de luxe', 'Voitures de luxe'),
        ('SUV', 'SUV'),
        ('Grandes voitures familiales', 'Grandes voitures familiales'),
        ('Voitures de sport', 'Voitures de sport'),
        ('Je ne sais pas', 'Je ne sais pas'),
    )
    nomVehCat = models.CharField(max_length=100, choices=CAT_VEHICULE_CHOICE)
    descriptionVehCat = models.TextField()


class DetailOrder(models.Model):
    objects = None
    commande = models.ForeignKey(Order, on_delete=models.CASCADE)
    piece = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantitePiece = models.PositiveIntegerField()


class DetailCart(models.Model):
    objects = None
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantiteCart = models.PositiveIntegerField()
