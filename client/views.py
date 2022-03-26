from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm, LoginForm
from django.views.generic import View, UpdateView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

class ClientRegistration(View):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        request.title = _("Ro'yxatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', context={
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli ro'yxatdan o'tdingiz!"))
            messages.info(request, 'nimadir')
            return redirect('main:index')
        return render(request, 'layouts/form.html', {
            'form': form
        })


class ClientLogin(View):
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _('Tizimga kirish')
        request.button_title = _('Tizimga kirish')

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, _("Xush kelibsiz {} !").format(user.username))

                return redirect('main:index')
            form.add_error('password', _('Login yoki parol noto\'g\'ri.'))

        return render(request, 'layouts/form.html', context={
            'form': form
        })


@login_required
def client_logout(request):
    messages.success(request, _("Xayr {}").format(request.user.username))
    logout(request)
    return redirect('main:index')


class ClientProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'photo']
    template_name = 'layouts/form.html'
    success_url = '/'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _('Profile')
        request.button_title = _('Saqlash Saqlash')

    def get_object(self, queryset=None):
        return self.request.user