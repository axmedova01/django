from django.shortcuts import render
from .models import Person
from .forms import PersonForm

def news_home(request):
    never = Person.objects.order_by('date')[:2]
    return render(request, 'news/news_home.html', {'news': never})

def create(request):
    form = PersonForm()
    data = {
        'form_key': form
    }
    return render(request, 'news/create.html', data)
