from django.shortcuts import render, redirect

from .forms import RegistrationForm

from .models import MedicalVault, VaultOwner
from .models import fnirs_dataset1_deoxy, experiment_hub

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

        return render(request, 'smdproject/dataset-details.html', {
            'dataset_found': True,
            'dataset': selected_dataset,
            'form': registration_form
        })

    except Exception as exc:
        return render(request, 'smdproject/dataset-details.html', {
            'dataset_found': False
        })


def confirm_registraion(request):
    return render(request, 'smdproject/registration-success.html')
