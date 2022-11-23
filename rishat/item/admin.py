from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_editable = ('price',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)
