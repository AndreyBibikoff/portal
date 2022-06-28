from django.contrib import admin

from clients.models import Clients, ClientsStaff, Images
# Register your models here.

admin.site.register(Clients)
admin.site.register(ClientsStaff)
admin.site.register(Images)
