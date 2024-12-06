from django.contrib.auth.forms import UserCreationForm

from blogs.forms import StyleFormBlog
from users.models import User


class UserRegisterForm(StyleFormBlog, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')



