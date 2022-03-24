from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic import View
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

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