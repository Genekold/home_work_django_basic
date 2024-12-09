from django.forms import ModelForm, BooleanField

from blogs.models import Blog, Autor


class StyleFormBlog:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogsForm(StyleFormBlog, ModelForm):
    class Meta:
        model = Blog
        exclude = ('views_counter', 'creator')


class BlogsModeratorForm(StyleFormBlog, ModelForm):
    class Meta:
        model = Blog
        fields = ('is_active',)


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"
