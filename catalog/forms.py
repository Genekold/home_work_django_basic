from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class StyleFormProduct:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormProduct, ModelForm):
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
