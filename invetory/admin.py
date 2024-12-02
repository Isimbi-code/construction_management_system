# from django.contrib import admin
# from .models import Category, Item, InventoryTransaction

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     search_fields = ('name',)

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'quantity', 'unit_price', 'total_value')
#     list_filter = ('category',)
#     search_fields = ('name', 'description')

# @admin.register(InventoryTransaction)
# class InventoryTransactionAdmin(admin.ModelAdmin):
#     list_display = ('item', 'quantity', 'transaction_type', 'date')
#     list_filter = ('transaction_type', 'date')
#     search_fields = ('item__name', 'notes')