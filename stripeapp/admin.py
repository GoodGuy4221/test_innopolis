from django.contrib import admin

from .models import ItemModel


@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'price',
    )
