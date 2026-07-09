from django import forms
from django.forms import ModelForm, TextInput
from .models import Main, Nam, Street, Fam, Otchestvo


class MainForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Nam.objects.all(), empty_label="Имя")
    fam = forms.ModelChoiceField(queryset=Fam.objects.all(), empty_label="Фамилия")
    otch = forms.ModelChoiceField(queryset=Otchestvo.objects.all(), empty_label="Отчество")
    street = forms.ModelChoiceField(queryset=Street.objects.all(), empty_label="Улица")
    class Meta:
        model = Main
        fields = ['name', 'fam', 'otch', 'street', 'bldn', 'bldn_k', 'appr', 'tel']

class MainFilterForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Nam.objects.all(), required=False, empty_label='Имя')
    fam = forms.ModelChoiceField(queryset=Fam.objects.all(), required=False, empty_label='Фамилия')
    otch = forms.ModelChoiceField(queryset=Otchestvo.objects.all(), required=False, empty_label='Отчество')
    street = forms.ModelChoiceField(queryset=Street.objects.all(), required=False, empty_label='Улица')
    bldn = forms.CharField(required=False)
    bldn_k = forms.CharField(required=False)
    appr = forms.CharField(required=False)
    tel = forms.CharField(required=False)


class namForm(ModelForm):
    class Meta:
        model = Nam
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            })
        }

class famForm(ModelForm):
    class Meta:
        model = Fam
        fields = ['fam']

        widgets = {
            "fam": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            })
        }

class otchForm(ModelForm):
    class Meta:
        model = Otchestvo
        fields = ['otch']

        widgets = {
            "otch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            })
        }

class streetForm(ModelForm):
    class Meta:
        model = Street
        fields = ['street']

        widgets = {
            "street": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Улица'
            })
        }
