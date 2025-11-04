from rest_framework import serializers, viewsets, generics, status
from django.shortcuts import get_object_or_404
from .models import Garage, Order, Item, CategoryPieces, Vehicle, VehicleCategory, DetailOrder, \
    DetailCart, Cart
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from datetime import datetime


@csrf_exempt
@require_POST
def login_view(request):
    try:
        # Charger les données JSON depuis le corps de la requête

        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        print(f"Attempting login with username: {username}, password: {password}")
    except json.JSONDecodeError:
        response_data = {'error': 'Invalid JSON'}
        return JsonResponse(response_data, status=400)

    # Authentification de l'utilisateur
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # L'utilisateur est trouvé, vous pouvez renvoyer ses informations
        user_data = {
            'id' : user.id,
            'username': user.username,
            'email': user.email,
            'prenom': user.first_name,  # Adapté selon les champs de votre modèle User
            # Ajoutez d'autres champs si nécessaire
        }
        response_data = {'user': user_data}
        return JsonResponse(response_data, status=200)
    else:
        # L'utilisateur n'est pas trouvé, renvoyer une réponse non autorisée (401)
        response_data = {'error': 'Unauthorized'}
        return JsonResponse(response_data, status=401)
def mark_payment_complete(request, order_id):
    try:
        order = get_object_or_404(Order, pk=order_id)
        order.paye = True
        order.save()

        return JsonResponse({'success': True, 'message': 'Paiement marqué comme complet'})
    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Commande non trouvée'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Une erreur s\'est produite : {str(e)}'})

@csrf_exempt
@require_POST
def update_order_motif(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)

        # Charger les données JSON depuis le corps de la requête
        data = json.loads(request.body.decode('utf-8'))
        motif_value = data.get('motif')

        # Mettre à jour le champ motif
        order.motif = motif_value
        order.save()

        # Mettre à jour la colonne statutCommande si elle est fournie dans la requête
        new_statut_commande = data.get('statutCommande')
        if new_statut_commande is not None:
            order.statutCommande = new_statut_commande
            order.save()

        return JsonResponse({'success': True, 'message': 'Motif et statutCommande mis à jour avec succès'})

    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Commande non trouvée'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Une erreur s\'est produite : {str(e)}'})
class UserListView(ListView):
    model = User
    def render_to_response(self, context, **response_kwargs):
        users = []
        for user in context['object_list']:
            user_data = {
                'id' : user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name' : user.last_name,
                'email': user.email,
                'password': user.password,  # C'est le hachage du mot de passe, pas le mot de passe en clair
            }
            users.append(user_data)
        return JsonResponse({'users': users})

def create_user(username, password, email,last_name,first_name):
    # Créer un nouvel utilisateur
    user = User.objects.create_user(username=username, password=password, email=email,last_name=last_name,first_name=first_name)

    # Enregistrer l'utilisateur dans la base de données
    user.save()

    return user
# def create_user(request):
#     # Récupérer les données JSON du corps de la requête
#     try:
#         data = json.loads(request.body)
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Données JSON non valides'}, status=400)
#
#     # Créer un nouvel utilisateur en utilisant la fonction de classe dans votre modèle User
#     try:
#         new_user = User.create_user(data)
#     except ValueError as e:
#         return JsonResponse({'error': str(e)}, status=400)
#
#     # Sauvegarder le nouvel utilisateur dans la base de données
#     new_user.save()
#
#     # Répondre avec les détails de l'utilisateur créé
#     response_data = {
#         'last_name': new_user.last_name,
#         'first_name': new_user.first_name,
#         'email': new_user.email,
#         'username': new_user.username,
#         'password': new_user.password,
#     }
#
#     return JsonResponse(response_data, status=201)




class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

class GarageListView(ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

    def list(self, request, *args, **kwargs):
        garages = self.get_queryset()
        serialized_data = GarageSerializer(garages, many=True).data
        return JsonResponse({'garages': serialized_data})

class GarageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

class DetailOrderSerializer(serializers.ModelSerializer):
    piece_nom = serializers.CharField(source='piece.nomItem', read_only=True)
    class Meta:
        model = DetailOrder
        fields = ['id','piece', 'quantitePiece', 'piece_nom']#7

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['piece_nom'] = instance.piece.nomItem
        return representation

class OrderSerializer(serializers.ModelSerializer):
    details = DetailOrderSerializer(many=True, required=False)


    class Meta:
        model = Order
        fields = ['id', 'voiture', 'utilisateur', 'dateCommande', 'statutCommande', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', None)
        order = Order.objects.create(**validated_data)

        if details_data:
            for detail_data in details_data:
                DetailOrder.objects.create(commande=order, **detail_data)

        return order

    class Meta:
        model = Order
        fields = '__all__'

    def get_pieces(self, order):
        details = DetailOrder.objects.filter(commande=order)
        serializer = DetailOrderSerializer(details, many=True)
        return serializer.data

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@csrf_exempt
def get_pending_orders(request):
    if request.method == 'GET':
        # Récupérer la liste des commandes en attente depuis la base de données avec les détails (pièces associées)
        pending_orders = Order.objects.filter(statutCommande='En attente').prefetch_related('details').values()

        # Convertir la queryset en une liste de dictionnaires
        pending_orders_list = list(pending_orders)

        # Ajouter les détails de chaque commande
        for order in pending_orders_list:
            order_id = order['id']
            details = DetailOrder.objects.filter(commande_id=order_id).values('piece__nomItem', 'quantitePiece')
            order['details'] = list(details)

            order['dateCommande'] = order['dateCommande'].strftime("%d-%m-%Y")

        # Vous pouvez renvoyer les données filtrées sous forme de réponse JSON
        return JsonResponse({'pending_orders': pending_orders_list})
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def get_completed_orders(request):
    if request.method == 'GET':
        # Récupérer la liste des commandes finalisées depuis la base de données avec les détails (pièces associées)
        completed_orders = Order.objects.filter(statutCommande='Finalisée').values()

        # Convertir la queryset en une liste de dictionnaires
        completed_orders_list = list(completed_orders)

        # Ajouter les détails de chaque commande
        for order in completed_orders_list:
            order_id = order['id']
            details = DetailOrder.objects.filter(commande_id=order_id).values('piece__nomItem', 'quantitePiece')
            order['details'] = list(details)
            order['dateCommande'] = order['dateCommande'].strftime("%d-%m-%Y")

        # Vous pouvez renvoyer les données filtrées sous forme de réponse JSON
        return JsonResponse({'completed_orders': completed_orders_list})
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def get_rejected_orders(request):
    if request.method == 'GET':
        # Récupérer la liste des commandes en attente depuis la base de données avec les détails (pièces associées)
        reject_orders = Order.objects.filter(statutCommande='Rejetee').values()

        # Convertir la queryset en une liste de dictionnaires
        pending_orders_list = list(reject_orders)

        # Ajouter les détails de chaque commande
        for order in pending_orders_list:
            order_id = order['id']
            details = DetailOrder.objects.filter(commande_id=order_id).values('piece__nomItem', 'quantitePiece')
            order['details'] = list(details)
            order['dateCommande'] = order['dateCommande'].strftime("%d-%m-%Y")
        # Vous pouvez renvoyer les données filtrées sous forme de réponse JSON
        return JsonResponse({'reject_orders': pending_orders_list})
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def get_user_order(request):
    # Récupère l'ID de l'utilisateur à partir des paramètres de requête
    user_id = request.GET.get('utilisateur')

    # Assure-toi que l'ID de l'utilisateur est un entier valide
    if user_id is not None and user_id.isdigit():
        user = get_object_or_404(User, id=int(user_id))
        orders = Order.objects.filter(utilisateur=user)

        order_data = []
        for order in orders:
            order_details = DetailOrder.objects.filter(commande=order)
            details_data = [
                {
                    'id': detail.id,
                    'piece': detail.piece.id,
                    'quantitePiece': detail.quantitePiece,
                    'piece_nom': detail.piece.nomItem,
                }
                for detail in order_details
            ]

            order_data.append({
                'id': order.id,
                'dateCommande': order.dateCommande,
                'statutCommande': order.statutCommande,
                'paye': order.paye,
                'details': details_data,
                'motif' : order.motif
            })

        return JsonResponse({'orders': order_data})
    else:
        return JsonResponse({'error': 'ID utilisateur non valide'})





class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Récupérer les données du JSON
        print("qsdfsdgs")
        data = json.loads(request.body.decode('utf-8'))
        print("data" , data)
        voiture_id = data.get('voiture')
        pieces_data = data.get('pieces')
        user_id = data.get('user')

        # Créer la commande
        order_data = {'voiture': voiture_id, 'utilisateur': user_id}
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order = order_serializer.save()
            print("--------------------------------------------")
            print(order.id)
            print("--------------------------------------------")

            # Créer les détails de la commande (pièces avec quantités)
            for piece_data in pieces_data:
                piece = piece_data.get('piece')
                quantity = piece_data.get('quantity')

                detail_order_data = {'commande': order.id, 'piece': piece, 'quantitePiece': quantity}
                print("-------------------piece id-------------------------")
                print(piece,detail_order_data)
                print("--------------------quantitePiece------------------------")
                print(quantity)
                detail_order_serializer = DetailOrderSerializer(data=detail_order_data)
                print("after detail_order_serializer",detail_order_serializer)
                if detail_order_serializer.is_valid():
                    detail_order_serializer.save(piece_id= piece)
                    print("-------------------detail_order_serializer-------------------------")
                    print(detail_order_serializer)
                else:
                    # Gérer les erreurs de validation des détails de la commande
                    return Response(detail_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Commande créée avec succès','order_id': order.id}, status=status.HTTP_201_CREATED)
        else:
            # Gérer les erreurs de validation de la commande
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Récupérer la nouvelle valeur de statutCommande du corps de la requête
        new_statut_commande = request.data.get('statutCommande', None)

        # Vérifier si une nouvelle valeur est fournie
        if new_statut_commande is not None:
            # Mettre à jour la colonne statutCommande avec la nouvelle valeur
            instance.statutCommande = new_statut_commande
            instance.save()

        serializer = self.get_serializer(instance, partial=partial)
        return Response(serializer.data)

class ItemSerializer(serializers.ModelSerializer):
    #details_commande = DetailOrderSerializer(many=True, read_only=True, source='detailorder_set')

    class Meta:
        model = Item
        fields = '__all__'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        items = self.get_queryset()
        serialized_data = ItemSerializer(items, many=True).data
        return JsonResponse({'items': serialized_data})

class ItemListView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryPiecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPieces
        fields = '__all__'

class CategoryPiecesViewSet(viewsets.ModelViewSet):
    queryset = CategoryPieces.objects.all()
    serializer_class = CategoryPiecesSerializer

class CategoryPiecesListView(ListCreateAPIView):
    queryset = CategoryPieces.objects.all()
    serializer_class = CategoryPiecesSerializer

class CategoryPiecesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryPieces.objects.all()
    serializer_class = CategoryPiecesSerializer

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


def get_vehicle_count(request):
    # Récupère l'ID de l'utilisateur à partir des paramètres de requête
    user_id = request.GET.get('utilisateur')

    # Assure-toi que l'ID de l'utilisateur est un entier valide
    if user_id is not None and user_id.isdigit():
        user_id = int(user_id)
        vehicle_count = Vehicle.objects.filter(utilisateur=user_id).count()
        print("----------vehicle count----------")
        print(vehicle_count)
        return JsonResponse({'count': vehicle_count})

    else:
        return JsonResponse({'error': 'ID utilisateur non valide'})


class VehicleListView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


def get_user_vehicles(request):
    # Récupère l'ID de l'utilisateur à partir des paramètres de requête
    user_id = request.GET.get('utilisateur')

    # Assure-toi que l'ID de l'utilisateur est un entier valide
    if user_id is not None and user_id.isdigit():
        user = get_object_or_404(User, id=int(user_id))
        vehicles = Vehicle.objects.filter(utilisateur=user)

        vehicle_data = [
            {
                'id': vehicle.id,
                'marque': vehicle.marque,
                # 'category': vehicle.category.name,
                'numPlaque': vehicle.numPlaque,
                'nombreCylindres': vehicle.nombreCylindres,
                'typeBoiteVitesse': vehicle.typeBoiteVitesse,
                'assurance': vehicle.assurance,
                'numChassis': vehicle.numChassis,
            }
            for vehicle in vehicles
        ]

        return JsonResponse({'vehicles': vehicle_data})
    else:
        # Retourne une réponse d'erreur si l'ID de l'utilisateur n'est pas valide
        return JsonResponse({'error': 'ID utilisateur non valide'})

class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleCountView(APIView):
    def get(self, request, format=None):
        count = Vehicle.objects.count()
        return Response({'count': count}, status=status.HTTP_200_OK)

class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = '__all__'

class VehicleCategoryViewSet(viewsets.ModelViewSet):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer

class VehicleCategoryListView(ListCreateAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer

class VehicleCategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer

class DetailOrderSerializer(serializers.ModelSerializer):
    piece = serializers.IntegerField(source='piece.id', read_only=True)
    piece_nom = serializers.CharField(source='piece.nomItem', read_only=True)

    class Meta:
        model = DetailOrder
        fields = ['id', 'quantitePiece', 'commande', 'piece', 'piece_nom']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['piece_nom'] = instance.piece.nomItem
        return representation
class DetailOrderViewSet(viewsets.ModelViewSet):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer

class DetailOrderListView(ListCreateAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer
#7
    def get(self, request, *args, **kwargs):
        commande_id = self.kwargs.get('commande_id')
        ma_commande = get_object_or_404(Order, id=commande_id)
        details_commande = DetailOrder.objects.filter(commande=ma_commande)
        serializer = DetailOrderSerializer(details_commande, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

class DetailOrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer

class DetailCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCart
        fields = '__all__'

class DetailCartViewSet(viewsets.ModelViewSet):
    queryset = DetailCart.objects.all()
    serializer_class = DetailCartSerializer

class DetailCartListView(ListCreateAPIView):
    queryset = DetailCart.objects.all()
    serializer_class = DetailCartSerializer

class DetailCartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DetailCart.objects.all()
    serializer_class = DetailCartSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartListView(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(itemCart=True)
        return queryset

class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
