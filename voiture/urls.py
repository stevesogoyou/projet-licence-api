"""
URL configuration for voiture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from venteVoiture.views import (
    UserListView, UserDetailView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,GarageDetailView,GarageListView,VehicleListView,VehicleDetailView,
    OrderListView, OrderDetailView,ItemDetailView, ItemListView,CartDetailView, CartListView,LocationDetailView, LocationListView,
    CategoryPiecesDetailView,CategoryPiecesListView, VehicleCategoryDetailView, VehicleCategoryListView, DetailCartDetailView, DetailCartListView,
    DetailOrderDetailView, DetailOrderListView)


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs pour les utilisateurs
    path('api/userAll/', UserListView.as_view(), name='user-list-all'),
    path('api/postUser/', UserListView.as_view(), name='user-post'),
    path('api/user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/deleteUser/<int:pk>/', UserDetailView.as_view(), name='delete-user'),
    path('api/updateUser/<int:pk>/', UserDetailView.as_view(), name='update-user'),

    # URLs pour les garages
    path('api/garageAll/', GarageListView.as_view(), name='garage-list-all'),
    path('api/postGarage/', GarageListView.as_view(), name='garage-post'),
    path('api/garage/<int:pk>/', GarageDetailView.as_view(), name='garage-detail'),
    path('api/deleteGarage/<int:pk>/', GarageDetailView.as_view(), name='delete-garage'),
    path('api/updateGarage/<int:pk>/', GarageDetailView.as_view(), name='update-garage'),
    
    #URLs pour les véhicules
    path('api/vehicleAll/', VehicleListView.as_view(), name='vehicle-list-all'),
    path('api/postVehicle/', VehicleListView.as_view(), name='vehicle-post'),
    path('api/vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('api/deleteVehicle/<int:pk>/', VehicleDetailView.as_view(), name='delete-vehicle'),
    path('api/updateVehicle/<int:pk>/', VehicleDetailView.as_view(), name='update-vehicle'),

    # URLs pour les commandes
    path('api/orderAll/', OrderListView.as_view(), name='order-list-all'),
    path('api/postOrder/', OrderListView.as_view(), name='order-post'),
    path('api/order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('api/deleteOrder/<int:pk>/', OrderDetailView.as_view(), name='delete-order'),
    path('api/updateOrder/<int:pk>/', OrderDetailView.as_view(), name='update-order'),

    #URLs pour les Pieces
    path('api/itemAll/', ItemListView.as_view(), name='item-list-all'),
    path('api/postItem/', ItemListView.as_view(), name='item-post'),
    path('api/item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('api/deleteItem/<int:pk>/', ItemDetailView.as_view(), name='delete-item'),
    path('api/updateItem/<int:pk>/', ItemDetailView.as_view(), name='update-item'),

    #URLs pour le Panier
    path('api/cartAll/', CartListView.as_view(), name='cart-list-all'),
    path('api/postCart/', CartListView.as_view(), name='cart-post'),
    path('api/cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('api/deleteCart/<int:pk>/', CartDetailView.as_view(), name='delete-cart'),
    path('api/updateCart/<int:pk>/', CartDetailView.as_view(), name='update-cart'),

    #URLs pour la localisation
    path('api/locationAll/', LocationListView.as_view(), name='location-list-all'),
    path('api/postLocation/', LocationListView.as_view(), name='location-post'),
    path('api/location/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('api/deleteLocation/<int:pk>/', LocationDetailView.as_view(), name='delete-location'),
    path('api/updateLocation/<int:pk>/', LocationDetailView.as_view(), name='update-location'),

    #URLs pour les catégories de pièces
    path('api/categoryPiecesAll/', CategoryPiecesListView.as_view(), name='category-pieces-list-all'),
    path('api/postCategoryPieces/', CategoryPiecesListView.as_view(), name='category-pieces-post'),
    path('api/categoryPieces/<int:pk>/', CategoryPiecesDetailView.as_view(), name='category-pieces-detail'),
    path('api/deleteCategoryPieces/<int:pk>/', CategoryPiecesDetailView.as_view(), name='delete-category-pieces'),
    path('api/updateCategoryPieces/<int:pk>/', CategoryPiecesDetailView.as_view(), name='update-category-pieces'),

    #URLs pour les catégories de véhicules
    path('api/vehicleCategoryAll/', VehicleCategoryListView.as_view(), name='vehicle-category-list-all'),
    path('api/postVehicleCategory/', VehicleCategoryListView.as_view(), name='vehicle-category-post'),
    path('api/vehicleCategory/<int:pk>/', VehicleCategoryDetailView.as_view(), name='vehicle-category-detail'),
    path('api/deleteVehicleCategory/<int:pk>/', VehicleCategoryDetailView.as_view(), name='delete-vehicle-category'),
    path('api/updateVehicleCategory/<int:pk>/', VehicleCategoryDetailView.as_view(), name='update-vehicle-category'),

    #URLs de détail du Panier
    path('api/detailCartAll/', DetailCartListView.as_view(), name='detail-cart-list-all'),
    path('api/postDetailCart/', DetailCartListView.as_view(), name='detail-cart-post'),
    path('api/detailCart/<int:pk>/', DetailCartDetailView.as_view(), name='detail-cart-detail'),
    path('api/deleteDetailCart/<int:pk>/', DetailCartDetailView.as_view(), name='delete-detail-cart'),
    path('api/updateDetailCart/<int:pk>/', DetailCartDetailView.as_view(), name='update-detail-cart'),

    #URLs de détail Commande
    path('api/detailOrderAll/', DetailOrderListView.as_view(), name='detail-order-list-all'),
    path('api/postDetailOrder/', DetailOrderListView.as_view(), name='detail-order-post'),
    path('api/detailOrder/<int:pk>/', DetailOrderDetailView.as_view(), name='detail-order-detail'),
    path('api/deleteDetailOrder/<int:pk>/', DetailOrderDetailView.as_view(), name='delete-detail-order'),
    path('api/updateDetailOrder/<int:pk>/', DetailOrderDetailView.as_view(), name='update-detail-order'),
]
