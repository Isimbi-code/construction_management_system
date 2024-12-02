from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('items/new/', views.ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    # path('transactions/', views.InventoryTransactionListView.as_view(), name='inventory_transaction_list'),
    # path('transactions/new/', views.InventoryTransactionCreateView.as_view(), name='inventory_transaction_create'),
]