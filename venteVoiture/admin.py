from django.contrib import admin


from .models import (Order, Item, CategoryPieces, Garage, Cart,

                     Vehicle, VehicleCategory, DetailOrder, DetailCart)


admin.site.register(Order)
admin.site.register(Item)
admin.site.register(CategoryPieces)
admin.site.register(Garage)
admin.site.register(Cart)
admin.site.register(Vehicle)
admin.site.register(VehicleCategory)
admin.site.register(DetailOrder)
admin.site.register(DetailCart)


