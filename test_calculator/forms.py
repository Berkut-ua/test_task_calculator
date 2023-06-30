from django import forms

class CalculatorForm(forms.Form):
    field_x = forms.FloatField()
    action = forms.ChoiceField(choices=(
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ))
    field_y = forms.FloatField()
    
