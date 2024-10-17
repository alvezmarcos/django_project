
from django.shortcuts import render
from .models import ExampleModel1

def example_view(request):
    examples = ExampleModel1.objects.all()
    return render(request, 'example_template.html', {'examples': examples})

def mi_vista(request):
    return render(request, 'otra_plantilla.html')
