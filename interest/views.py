from django.shortcuts import render
from .forms import CalculatorForm

# def compound_interest_calculator(request):
#     if request.method == 'POST':
#         principal = float(request.POST['principal'])
#         rate = float(request.POST['rate'])
#         time = float(request.POST['time'])
#         compound_periods = float(request.POST['compound_periods'])
#         amount = principal * (1 + rate / (compound_periods * 100)) ** (compound_periods * time)
#         context = {'amount': amount}
#     else:
#         context = {}
#     return render(request, 'calculator.html', context)
def compound_interest_calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            rate = float(form.cleaned_data['rate'])
            time = float(form.cleaned_data['time'])
            compound_periods = float(form.cleaned_data['compound_periods'])
            amount = float(principal * (1 + rate / (compound_periods * 100)) ** (compound_periods * time))
            context = {'amount': amount, 'form': form}
        else:
            context = {'form': form}
    else:
        form = CalculatorForm()
        context = {'form': form}
    return render(request, 'calculator.html', context)