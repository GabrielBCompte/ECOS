# -*- coding: utf-8 -*-
from django import forms
from shuntsapp.models import Shunt


class CreateShuntForm(forms.ModelForm):
    """Formulario para crear shunts, solo se excluye la creation_date porque se asignara automaticamente 
    a datetime.now()
    """

    class Meta:
        model = Shunt
        exclude = ['creation_date']

