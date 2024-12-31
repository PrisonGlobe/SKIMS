from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, SupplyItemForm, HospitalItemForm, RoomItemForm, RackItemForm, BinItemForm
from .models import HospitalItem, RoomItem, RackItem, BinItem, SupplyItem, Category
from django.http import JsonResponse
from django.db.models import Q


class Index(TemplateView):
    template_name = 'SKIMS/index.html'

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'SKIMS/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')

        return render(request, 'SKIMS/signup.html', {'form': form})


# Hospital Item

class HospitalDashboard(LoginRequiredMixin, View):
    def get(self, request):
        hospitals = HospitalItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request, 'SKIMS/hospital_dashboard.html', {'hospitals': hospitals})


class AddHospital(LoginRequiredMixin, CreateView):
    model = HospitalItem
    form_class = HospitalItemForm
    template_name = 'SKIMS/hospital_form.html'
    success_url = reverse_lazy('hospital-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditHospital(LoginRequiredMixin, UpdateView):
    model = HospitalItem
    form_class = HospitalItemForm
    template_name = 'SKIMS/hospital_form.html'
    success_url = reverse_lazy('hospital-dashboard')


class DeleteHospital(LoginRequiredMixin, DeleteView):
    model = HospitalItem
    template_name = 'SKIMS/hospital_delete.html'
    success_url = reverse_lazy('hospital-dashboard')
    context_object_name = 'hospital'

# Room Item

class RoomDashboard(LoginRequiredMixin, View):
    def get(self, request):
        hospital_id = request.GET.get('hospital_id')  # Get hospital_id from query parameters
        if hospital_id:
            rooms = RoomItem.objects.filter(user=self.request.user.id, hospitalName_id=hospital_id).order_by('id')
        else:
            rooms = RoomItem.objects.filter(user=self.request.user.id).order_by('id')  # Default: all rooms for the user
        return render(request, 'SKIMS/room_dashboard.html', {'rooms': rooms})


class AddRoom(LoginRequiredMixin, CreateView):
    model = RoomItem
    form_class = RoomItemForm
    template_name = 'SKIMS/room_form.html'
    success_url = reverse_lazy('room-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditRoom(LoginRequiredMixin, UpdateView):
    model = RoomItem
    form_class = RoomItemForm
    template_name = 'SKIMS/room_form.html'
    success_url = reverse_lazy('room-dashboard')


class DeleteRoom(LoginRequiredMixin, DeleteView):
    model = RoomItem
    template_name = 'SKIMS/room_delete.html'
    success_url = reverse_lazy('room-dashboard')
    context_object_name = 'room'

# Rack Item

class RackDashboard(LoginRequiredMixin, View):
    def get(self, request):
        room_id = request.GET.get('room_id')  # Get hospital_id from query parameters
        if room_id:
            racks = RackItem.objects.filter(user=self.request.user.id, roomName_id=room_id).order_by('id')
        else:
            racks = RackItem.objects.filter(user=self.request.user.id).order_by('id')  # Default: all rooms for the user
        return render(request, 'SKIMS/rack_dashboard.html', {'racks': racks})


class AddRack(LoginRequiredMixin, CreateView):
    model = RackItem
    form_class = RackItemForm
    template_name = 'SKIMS/rack_form.html'
    success_url = reverse_lazy('rack-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditRack(LoginRequiredMixin, UpdateView):
    model = RackItem
    form_class = RackItemForm
    template_name = 'SKIMS/rack_form.html'
    success_url = reverse_lazy('rack-dashboard')


class DeleteRack(LoginRequiredMixin, DeleteView):
    model = RackItem
    template_name = 'SKIMS/rack_delete.html'
    success_url = reverse_lazy('rack-dashboard')
    context_object_name = 'rack'

# Bin Item

class BinDashboard(LoginRequiredMixin, View):
    def get(self, request):
        rack_id = request.GET.get('rack_id')  # Get hospital_id from query parameters
        if rack_id:
            bins = BinItem.objects.filter(user=self.request.user.id, rackName_id=rack_id).order_by('id')
        else:
            bins = BinItem.objects.filter(user=self.request.user.id).order_by('id')  # Default: all rooms for the user
        return render(request, 'SKIMS/bin_dashboard.html', {'bins': bins})


class AddBin(LoginRequiredMixin, CreateView):
    model = BinItem
    form_class = BinItemForm
    template_name = 'SKIMS/bin_form.html'
    success_url = reverse_lazy('bin-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditBin(LoginRequiredMixin, UpdateView):
    model = BinItem
    form_class = BinItemForm
    template_name = 'SKIMS/bin_form.html'
    success_url = reverse_lazy('bin-dashboard')


class DeleteBin(LoginRequiredMixin, DeleteView):
    model = BinItem
    template_name = 'SKIMS/bin_delete.html'
    success_url = reverse_lazy('bin-dashboard')
    context_object_name = 'bin'


# Supply Item

class SupplyDashboard(LoginRequiredMixin, View):
    def get(self, request):
        bin_id = request.GET.get('bin_id')  # Get hospital_id from query parameters
        if bin_id:
            supplies = SupplyItem.objects.filter(user=self.request.user.id, binName_id=bin_id).order_by('id')
        else:
            supplies = SupplyItem.objects.filter(user=self.request.user.id).order_by('id')  # Default: all rooms for the user
        return render(request, 'SKIMS/supply_dashboard.html', {'supplies': supplies})

class RackSupplyDashboard(LoginRequiredMixin, View):
    def get(self, request):
        rack_id = request.GET.get('rack_id')  # Get rack_id from query parameters
        if rack_id:
            # Follow relationships from SupplyItem -> Bin -> Rack
            supplies = SupplyItem.objects.filter(
                user=self.request.user.id,
                binName__rackName_id=rack_id  # Use __ to follow the relationship
            ).order_by('id')
        else:
            # Default: all supplies for the user
            supplies = SupplyItem.objects.filter(user=self.request.user.id).order_by('id')

        return render(request, 'SKIMS/rack_supply_dashboard.html', {'supplies': supplies})


class AddSupply(LoginRequiredMixin, CreateView):
    model = SupplyItem
    form_class = SupplyItemForm
    template_name = 'SKIMS/supply_form.html'
    success_url = reverse_lazy('supply-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditSupply(LoginRequiredMixin, UpdateView):
    model = SupplyItem
    form_class = SupplyItemForm
    template_name = 'SKIMS/supply_form.html'
    success_url = reverse_lazy('supply-dashboard')


class DeleteSupply(LoginRequiredMixin, DeleteView):
    model = SupplyItem
    template_name = 'SKIMS/supply_delete.html'
    success_url = reverse_lazy('supply-dashboard')
    context_object_name = 'supply'

class SupplyItemDashboard(View):
    def get(self, request, supplyName):
        # Fetch supply items by name and order them
        supply_items = SupplyItem.objects.filter(supplyName=supplyName).order_by(
            'binName__rackName__roomName__hospitalName',
            'binName__rackName__roomName__floor',
            'binName__rackName__roomName',
            'binName__rackName',
            'binName'
        )
        return render(request, 'SKIMS/supply_item_dashboard.html', {'supply_items': supply_items, 'supplyName': supplyName})

# Searchbar

def supply_search(request):
    query = request.GET.get('q', '')
    if query:
        # Filter supply items matching the query
        results = SupplyItem.objects.filter(supplyName__icontains=query).values('supplyName')
        # Deduplicate supply names and limit to top 3 results
        unique_results = []
        seen = set()
        for item in results:
            if item['supplyName'] not in seen:
                unique_results.append({'supplyName': item['supplyName'], 'url': f'/supply-item-dashboard/{item["supplyName"]}/'})
                seen.add(item['supplyName'])
                if len(unique_results) == 3:  # Stop adding after 3 unique results
                    break
        data = unique_results
    else:
        data = []
    return JsonResponse(data, safe=False)




