from django.contrib import admin
from clients.models import Client

class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','tin', 'pin', 'cell', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'tin',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
    ordering = ('name',)

admin.site.register(Client, Clients)