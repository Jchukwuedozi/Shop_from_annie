from django.shortcuts import render
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import login

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Registration(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
