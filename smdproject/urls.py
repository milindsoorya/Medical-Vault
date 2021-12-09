from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all_databases'),
    path('success', views.confirm_registraion,
         name="confirm-registration"),
    path('<slug:dataset_slug>',
         views.dataset_details, name='dataset_details',)
]
