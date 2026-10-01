import re

from django import forms

from porteiros.models import Porteiro


class PorteiroForm(forms.ModelForm):
    cpf = forms.CharField(max_length=14, label="CPF")
    telefone = forms.CharField(max_length=15, label="Telefone de contato")

    class Meta:
        model = Porteiro
        fields = ["nome_completo", "cpf", "telefone", "data_nascimento"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_cpf(self):
        cpf = re.sub(r"\D", "", self.cleaned_data["cpf"])
        if len(cpf) != 11:
            raise forms.ValidationError("Informe um CPF com 11 dígitos.")
        return cpf

    def clean_telefone(self):
        telefone = re.sub(r"\D", "", self.cleaned_data["telefone"])
        if len(telefone) not in (10, 11):
            raise forms.ValidationError("Informe o telefone com DDD.")
        return telefone
