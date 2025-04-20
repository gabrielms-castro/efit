from django import forms
from treino.models import Usuario


class OnboardingForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'idade', 'peso', 'altura', 'objetivo', 'frequencia_treino', 'nivel_condicionamento', 'restricoes']
