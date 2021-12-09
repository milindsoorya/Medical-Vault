from django.contrib import admin
from .models import MedicalVault, VaultOwner


class DatavaultAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    list_filter = ('date_created',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(MedicalVault, DatavaultAdmin)
admin.site.register(VaultOwner)
