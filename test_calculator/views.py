import json
from django import http
from django.shortcuts import render

from . import forms
from .calculator import calculate

def home_page(request):
    form = forms.CalculatorForm()
    return render(request,
                  'test_calculator/index.html',
                  {'form': form})

def calculator(request):
    form = forms.CalculatorForm(request.GET)
    if form.is_valid():
        result = calculate(
            [form.cleaned_data['field_x'],
             form.cleaned_data['action'],
             form.cleaned_data['field_y']],
            lambda r: {'result': r}
        )
    else:
        return http.HttpResponseBadRequest(json.dumps(form.errors))
    return http.HttpResponse(json.dumps(result))
