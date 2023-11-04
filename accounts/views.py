from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpViews(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'