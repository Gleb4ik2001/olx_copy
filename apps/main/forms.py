from django import forms
from .models import Products

class AddProductForm(forms.Form):
    title = forms.CharField(
        label='Название товара',
        max_length=200,
        required=True
    )
    price = forms.DecimalField(
        label='Цена(KZT)',
        max_digits=8,
        required=True
    )
    photo = forms.ImageField(
        label='Фото товара',
        required=True
    )
    description = forms.CharField(
        label='Описание',
        max_length=255,
        required=True
    )
    category = forms.ChoiceField(
        label='Категория',
        choices=Products.CATOGORIES_CHOISES
    )
