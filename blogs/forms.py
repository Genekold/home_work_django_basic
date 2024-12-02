from django.forms import ModelForm

from blogs.models import Blog


class BlogsForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('views_counter',)
