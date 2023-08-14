from rest_framework import serializers, viewsets
from .models import User, Garage, Order, Item, CategoryPieces, Location, Vehicle, VehicleCategory, DetailOrder, \
    DetailCart, Cart

from rest_framework.views import exception_handler
from rest_framework.generics import  ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView


# Serializer pour le modèle User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# # Viewset pour l'API User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Views pour l'API User
class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['detail'] = "Object introuvable"
        response.data['status_code'] = response.status_code
    return response


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer


class GarageListView(ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer  # Assurez-vous d'utiliser le sérialiseur approprié


class GarageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer  # Assurez-vous d'utiliser le sérialiseur approprié


# def custom_exception_handler(self, exc, context):
#     response = super().custom_exception_handler(exc, context)

#     if response is not None:
#         response.data['detail'] = "Garage introuvable"
#         response.data['status_code'] = response.status_code

#     return response


# ------------------------------------------------------------------------------

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Commande introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Élément introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------

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

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Catégorie de pièces introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Localisation introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleListView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Véhicule introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------


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

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Catégorie de véhicule introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------


class DetailOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailOrder
        fields = '__all__'


class DetailOrderViewSet(viewsets.ModelViewSet):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer


class DetailOrderListView(ListCreateAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer


class DetailOrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DetailOrder.objects.all()
    serializer_class = DetailOrderSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Détail de commande introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------


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

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Détail du panier introuvable"
            response.data['status_code'] = response.status_code

        return response


# ------------------------------------------------------------------------------


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartListView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def custom_exception_handler(self, exc, context):
        response = super().custom_exception_handler(exc, context)

        if response is not None:
            response.data['detail'] = "Panier introuvable"
            response.data['status_code'] = response.status_code

        return response

# ------------------------------------------------------------------------------
