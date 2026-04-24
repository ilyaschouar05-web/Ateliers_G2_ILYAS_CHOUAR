from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',
                  'phone', 'address', 'city', 'postal_code']
        labels = {
            'username': "Nom d'utilisateur",
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Adresse email',
            'phone': 'Téléphone',
            'address': 'Adresse',
            'city': 'Ville',
            'postal_code': 'Code postal',
        }
