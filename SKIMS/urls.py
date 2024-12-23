from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, SupplyDashboard, AddSupply, EditSupply, DeleteSupply, SupplyItemDashboard
from .views import HospitalDashboard, AddHospital, EditHospital, DeleteHospital
from .views import RoomDashboard, AddRoom, EditRoom, DeleteRoom, RackDashboard, AddRack, EditRack, DeleteRack
from .views import BinDashboard, AddBin, EditBin, DeleteBin, supply_search
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='SKIMS/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='SKIMS/logout.html'), name='logout'),
    #Supply Item
    path('supply-dashboard/', SupplyDashboard.as_view(), name='supply-dashboard'),
    path('add-supply/', AddSupply.as_view(), name='add-supply'),
    path('edit-supply/<int:pk>', EditSupply.as_view(), name='edit-supply'),
    path('delete-supply/<int:pk>', DeleteSupply.as_view(), name='delete-supply'),
    path('supply-dashboard/', SupplyDashboard.as_view(), name='supply-dashboard'),
    path('supply-item-dashboard/<str:supplyName>/', SupplyItemDashboard.as_view(), name='supply-item-dashboard'),
    # Hospital Item
    path('hospital-dashboard/', HospitalDashboard.as_view(), name='hospital-dashboard'),
    path('add-hospital/', AddHospital.as_view(), name='add-hospital'),
    path('edit-hospital/<int:pk>', EditHospital.as_view(), name='edit-hospital'),
    path('delete-hospital/<int:pk>', DeleteHospital.as_view(), name='delete-hospital'),
    # Room Item
    path('room-dashboard/', RoomDashboard.as_view(), name='room-dashboard'),
    path('add-room/', AddRoom.as_view(), name='add-room'),
    path('edit-room/<int:pk>', EditRoom.as_view(), name='edit-room'),
    path('delete-room/<int:pk>', DeleteRoom.as_view(), name='delete-room'),
    # Rack Item
    path('rack-dashboard/', RackDashboard.as_view(), name='rack-dashboard'),
    path('add-rack/', AddRack.as_view(), name='add-rack'),
    path('edit-rack/<int:pk>', EditRack.as_view(), name='edit-rack'),
    path('delete-rack/<int:pk>', DeleteRack.as_view(), name='delete-rack'),
    # Bin Item
    path('bin-dashboard/', BinDashboard.as_view(), name='bin-dashboard'),
    path('add-bin/', AddBin.as_view(), name='add-bin'),
    path('edit-bin/<int:pk>', EditBin.as_view(), name='edit-bin'),
    path('delete-bin/<int:pk>', DeleteBin.as_view(), name='delete-bin'),
    path('search/', supply_search, name='supply-search'),

]
