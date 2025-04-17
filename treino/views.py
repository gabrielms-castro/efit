from django.shortcuts import render, redirect
from .forms import OnboardingForm

def onboarding_view(request):
    form = OnboardingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alguma_pagina_sucesso')  # pode ser 'dashboard' ou similar
    return render(request, 'onboarding.html', {'form': form})
