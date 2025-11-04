from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from venteVoiture.views import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, GarageDetailView, GarageListView,
    VehicleListView, VehicleDetailView,
    OrderListView, OrderDetailView, ItemDetailView,get_user_order,get_vehicle_count,update_order_motif,get_pending_orders,get_completed_orders,get_rejected_orders, ItemListView, mark_payment_complete,create_user, get_user_vehicles, CartDetailView, CartListView, login_view,

    CategoryPiecesDetailView, CategoryPiecesListView, VehicleCategoryDetailView, VehicleCategoryListView,
    DetailCartDetailView, DetailCartListView, UserListView, OrderCreateView,
    DetailOrderDetailView, DetailOrderListView, VehicleCountView)


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs pour les utilisateurs
    path('api/userAll/', UserListView.as_view(), name='user-list-all'),
     path('api/postUser/', create_user, name='user-post'),
    # path('api/user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('api/deleteUser/<int:pk>/', UserDetailView.as_view(), name='delete-user'),
    # path('api/updateUser/<int:pk>/', UserDetailView.as_view(), name='update-user'),

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
    path('api/vehicleCount/', get_vehicle_count, name='vehicle-count'),
    path('api/vehicleOfUser/', get_user_vehicles, name='get_user_vehicles'),

    # URLs pour les commandes
    path('api/orderAll/', OrderListView.as_view(), name='order-list-all'),
    path('api/postOrder/', OrderCreateView.as_view(), name='order-post'),
    path('api/order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('api/deleteOrder/<int:pk>/', OrderDetailView.as_view(), name='delete-order'),
    path('api/updateOrder/<int:pk>', OrderDetailView.as_view(), name='update-order'),
    path('api/orderOfUser/', get_user_order, name='orderOfUser'),
    path('api/order/en-attente/', get_pending_orders, name='pending-order-list'),
    path('api/order/finalisee/', get_completed_orders, name='completed-orders'),
    path('api/order/rejetee/', get_rejected_orders, name='rejected-orders'),
    path('api/update_order_motif/<int:order_id>/', update_order_motif, name='update_order_motif'),


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
    path('details_commande/<int:commande_id>/', DetailOrderListView.as_view(), name='detailorder-list'),
    path('api/deleteDetailOrder/<int:pk>/', DetailOrderDetailView.as_view(), name='delete-detail-order'),
    path('api/updateDetailOrder/<int:pk>/', DetailOrderDetailView.as_view(), name='update-detail-order'),

    #URLs pour le login
    path('api/login/', login_view, name='login'),

    #URLs pour le payement
    path('api/payment/<int:order_id>/', mark_payment_complete, name='mark_payment_complete'),
]
