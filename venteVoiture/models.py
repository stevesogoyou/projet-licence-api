
from django.db import models
from django.contrib.auth.models import User


class VehicleCategory(models.Model):
    objects = None
    CAT_VEHICULE_CHOICE = (
        ('Mini-citadines', 'Mini-citadines'),#1
        ('Petites voitures', 'Petites voitures'),#2
        ('Voitures compactes', 'Voitures compactes'),#3
        ('Grosses voitures', 'Grosses voitures'),#4
        ('Voitures de prestige', 'Voitures de prestige'),#5
        ('Voitures de luxe', 'Voitures de luxe'),#6
        ('SUV', 'SUV'),#7
        ('Grandes voitures familiales', 'Grandes voitures familiales'),#8
        ('Voitures de sport', 'Voitures de sport'),#9
        ('Je ne sais pas', 'Je ne sais pas'),#10
    )
    nomVehCat = models.CharField(max_length=100, choices=CAT_VEHICULE_CHOICE)
    descriptionVehCat = models.TextField()


class Vehicle(models.Model):
    objects = None
    marque = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    numPlaque = models.CharField(max_length=20)
    nombreCylindres = models.PositiveIntegerField()
    typeBoiteVitesse = models.BooleanField(default=False)  # Champ booléen pour le type de boîte de vitesse
    assurance = models.BooleanField(default=False)  # Champ booléen pour l'assurance
    numChassis = models.CharField(max_length=100)
    # Autres champs pour les informations relatives au véhicule


class Order(models.Model):
    objects = None
    UTILISATEUR_CHOICES = (
        ('En cours', 'En cours'),
        ('Finalisée', 'Finalisée'),
        ('En attente', 'En attente'),
        ('Rejetee', 'Rejetee'),
    )

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    dateCommande = models.DateTimeField(auto_now_add=True)
    statutCommande = models.CharField(max_length=20, choices=UTILISATEUR_CHOICES, default='En attente')
    paye = models.BooleanField(default=False)
    motif = models.CharField(max_length=200, null=True)
    # Autres champs pour les informations relatives à la commande




class Item(models.Model):
    objects = None
    nomItem = models.CharField(max_length=100)
    descriptionItem = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey('CategoryPieces', on_delete=models.CASCADE)
    statutItem = models.BooleanField(default=False) # rupture de stock ou pas
    marque = models.CharField(max_length=100, default='Toutes les marques')
    quantiteItems = models.PositiveIntegerField(default=0)  # colonne pour la quantité en stock
    itemCart = models.BooleanField(default=False)  # colonne pour savoir si l'article est dans le panier
    imageItem = models.CharField(max_length=100, null=True)  # Champ nullable pour le nom de l'image de la pièce


class DetailOrder(models.Model):
    objects = None
    commande = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    piece = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantitePiece = models.PositiveIntegerField()

    # def __str__(self):
    #     return f"{self.quantitePiece} x {self.piece}"
    #Cette table sera répété 3 fois, mais pour une seule commande




class CategoryPieces(models.Model):
    objects = None
    CAT_PIECE_CHOICE = (
        ('Mécanique', 'Mécanique'),
        ('Electrique', 'Electrique'),
        ('Accessoire', 'Accessoire'),
    )
    nomCatPiece = models.CharField(max_length=31, choices=CAT_PIECE_CHOICE)



class Garage(models.Model):
    objects = None
    nomGarage = models.CharField(max_length=100)
    adresseGarage = models.CharField(max_length=200)
    ville = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    numeroGarage = models.IntegerField()
    # Autres champs pour les informations relatives à la localisation







class Cart(models.Model):
    objects = None
    #utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    # Autres champs pour les informations relatives au panier



class DetailCart(models.Model):
    objects = None
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantiteCart = models.PositiveIntegerField()


