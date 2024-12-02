from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages


class ItemListView(ListView):
    model = Item
    template_name = 'invetory/item_list.html'
    context_object_name = 'items'

    def handle_no_permission(self):
        messages.warning(self.request, "You need to be logged in to view this page.")
        return redirect('login') 


    def get_queryset(self):
        # Filter projects based on the logged-in user
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'invetory/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'invetory/item_form.html'
    fields = ['name', 'description', 'quantity', 'unit_price', 'reorder_level']
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the inventory
        return super().form_valid(form)

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'invetory/item_form.html'
    fields = ['name', 'description', 'quantity', 'unit_price', 'reorder_level']
    success_url = reverse_lazy('item_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'invetory/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

# class InventoryTransactionListView(ListView):
#     model = InventoryTransaction
#     template_name = 'invetory/inventory_transaction_list.html'
#     context_object_name = 'transactions'

# class InventoryTransactionCreateView(CreateView):
#     model = InventoryTransaction
#     template_name = 'invetory/inventory_transaction_form.html'
#     fields = ['item', 'quantity', 'transaction_type', 'notes']
#     success_url = reverse_lazy('inventory_transaction_list')