from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CustomUserCreationForm


class SignUp(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Sign up has been completed!'

    def form_valid(self, form):
        form.save()
        return super(SignUp, self).form_valid(form)
