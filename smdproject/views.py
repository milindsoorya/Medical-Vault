from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import RegistrationForm

from .models import MedicalVault, VaultOwner
from .models import fnirs_dataset1_deoxy, experiment_hub

from .utils import get_plot

# Create your views here.


# def index(request):
#     # Gets all instance
#     medicalvault = MedicalVault.objects.all()
#     return render(request, 'smdproject/index.html', {
#         'show_datasets': True,
#         'datasets': medicalvault
#     })


def index(request):
    # Gets all instance
    experiments = experiment_hub.objects.all()
    return render(request, 'smdproject/index.html', {
        'show_datasets': True,
        'datasets': experiments
    })


# def dataset_details(request, dataset_slug):
#     try:
#         selected_dataset = MedicalVault.objects.get(slug=dataset_slug)
#         if request.method == 'GET':
#             registration_form = RegistrationForm()
#         else:
#             registration_form = RegistrationForm(request.POST)
#             if registration_form.is_valid():
#                 new_user_email = registration_form.cleaned_data['email']
#                 user, _ = VaultOwner.objects.get_or_create(
#                     email=new_user_email)
#                 selected_dataset.vault_owner.add(user)
#                 return redirect('confirm-registration')

#         return render(request, 'smdproject/dataset-details.html', {
#             'dataset_found': True,
#             'dataset': selected_dataset,
#             'form': registration_form
#         })

#     except Exception as exc:
#         return render(request, 'smdproject/dataset-details.html', {
#             'dataset_found': False
#         })

def dataset_details(request, dataset_slug):
    try:
        selected_dataset = experiment_hub.objects.get(slug=dataset_slug)

        # Querying all the objects from fnirs dataset
        channel_info = fnirs_dataset1_deoxy.objects.all()

        # Querying channel 1 information from fnirs dataset
        channel_one = fnirs_dataset1_deoxy.objects.values_list(
            'data_ch1', flat=True)

        # Converting the queried data into list
        channel_one_list = list(channel_one)

        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                new_user_email = registration_form.cleaned_data['email']
                user, _ = VaultOwner.objects.get_or_create(
                    email=new_user_email)
                selected_dataset.vault_owner.add(user)
                return redirect('confirm-registration')

        # Passing the queried data to the front-end
        return render(request, 'smdproject/dataset-details.html', {
            'dataset_found': True,
            'dataset': selected_dataset,
            'form': registration_form,
            'channelinfo': channel_one_list,
        })

    except Exception as exc:
        print(exc)
        return render(request, 'smdproject/dataset-details.html', {
            'dataset_found': False
        })


def confirm_registraion(request):
    return render(request, 'smdproject/registration-success.html')


class ChartView(TemplateView):
    template_name = 'smdproject/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = fnirs_dataset1_deoxy.objects.all()
        return context
