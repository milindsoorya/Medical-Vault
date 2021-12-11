from django.contrib import admin
from .models import MedicalVault, VaultOwner
from .models import experiment_hub


# class DatavaultAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date_created')
#     list_filter = ('date_created',)
#     prepopulated_fields = {'slug': ('title',)}


# admin.site.register(MedicalVault, DatavaultAdmin)
# admin.site.register(VaultOwner)

class DatavaultAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    list_filter = ('date_created',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(experiment_hub)
