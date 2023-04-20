from django import forms

class CalculatorForm(forms.Form):
    principal = forms.FloatField(label='Principal', min_value=0)
    rate = forms.FloatField(label='Annual Interest Rate', min_value=0, max_value=100)
    time = forms.FloatField(label='Time Period (in years)', min_value=0)
    compound_periods = forms.ChoiceField(label='Compound Periods per Year', choices=[('1', 'Annually'), ('2', 'Semi-Annually'), ('4', 'Quarterly'), ('12', 'Monthly')])