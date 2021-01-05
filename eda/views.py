from django.shortcuts import render

# Create your views here.
def intro_view(request):
    return render(request, 'intro.html', {})

def eda_view(request):
    return render(request, 'eda-korea-data-analysis-based-on-income.html', {})
