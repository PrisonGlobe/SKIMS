from django.contrib import admin
from .models import HospitalItem, RoomItem, RackItem, BinItem, SupplyItem, Category

# Register your models here.
admin.site.register(HospitalItem)
admin.site.register(RoomItem)
admin.site.register(RackItem)
admin.site.register(BinItem)
admin.site.register(SupplyItem)
admin.site.register(Category)
