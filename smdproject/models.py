from django.db import models

# One MedicalVault can have many VaultOwner, one-to-many relation


class VaultOwner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    affiliation = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} - {self.affiliation}'


class MedicalVault(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date_created = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    vault_owner = models.ManyToManyField(VaultOwner, blank=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'
