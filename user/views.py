from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm, UpdateUserForm, ChangepassForm


class RegisterUser(generic.CreateView):
    form_class = UserRegForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditUser(generic.UpdateView):
    form_class = UpdateUserForm
    template_name = 'registration/editprofile.html'
    #success_url = reverse_lazy('success')
    success_url = reverse_lazy('password_success')

    def get_object(self):
        return self.request.user


class PasswordChange(PasswordChangeView):
    form_class = ChangepassForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {}) 
