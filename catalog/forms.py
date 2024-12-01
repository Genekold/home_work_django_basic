from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class StyleForm:
    def __init__(self, *args, **kwargs):
        super(StyleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите назавние продукта'
        })


class ProductForm(ModelForm, StyleForm):
    EXCEPTION_WORDS = [
        'казино',
        'биржа',
        'обман',
        'криптовалюта',
        'дешево',
        'полиция',
        'крипта',
        'бесплатно',
        'радар'
    ]

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите назавние продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта',
            'row': 3
        })
        self.fields['photo'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in ProductForm.EXCEPTION_WORDS:
            if word in name.lower():
                self.add_error('name', f'Назавание продукта содержит запрещенное слово "{word.upper()}"')
            if word in description.lower():
                self.add_error('description', f'Описание продукта содержит запрещенное слово "{word.upper()}"')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена на товар должна быть положительной')
        return price
