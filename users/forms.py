from django.contrib.auth.forms import UserCreationForm

from users.models import User
from catalog.forms import StyleForm


class UserRegisterForm(StyleForm, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')



