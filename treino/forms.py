from django import forms
from .models import Usuario

class OnboardingForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "idade",
            "peso",
            "altura",
            "objetivo",
            "frequencia_treino",
            "nivel_condicionamento",
            "restricoes",
        ]
        widgets = {
            "restricoes": forms.Textarea(attrs={"rows": 3}),
        }
