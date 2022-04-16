from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from .models import *
from .forms import WidgetsForm

"""
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

"""
# Define the home view


def home(request):
    context = {}
    context['form'] = WidgetsForm()
    return render(request, "index.html", context)


def add_widget(request):
    form = WidgetsForm(request.POST)

    if form.is_valid():
        widget = form.save()
        widget.save()

    return redirect('index')
