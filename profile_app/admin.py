from django.contrib import admin

from .models import Profile

admin.site.register(Profile)                                                    # Registriert das Profile-Modell im Django-Admin-Interface, sodass Administratoren Profile einsehen und verwalten können.
