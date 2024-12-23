from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import HospitalItem, RoomItem, RackItem, BinItem, SupplyItem, Category


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SupplyItemForm(forms.ModelForm):

    class Meta:
        model = SupplyItem
        fields = ['binName', 'supplyName', 'quantity', 'vendor', 'refNum']


class HospitalItemForm(forms.ModelForm):

    class Meta:
        model = HospitalItem
        fields = ['hospitalName', 'address']


class RoomItemForm(forms.ModelForm):

    class Meta:
        model = RoomItem
        fields = ['hospitalName', 'roomName', 'floor', 'department']


class RackItemForm(forms.ModelForm):

    class Meta:
        model = RackItem
        fields = ['roomName', 'rackName', 'binCount']


class BinItemForm(forms.ModelForm):

    class Meta:
        model = BinItem
        fields = ['rackName', 'binName', 'binHeight', 'binColor']

