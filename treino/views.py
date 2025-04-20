# treino/views.py
from django.shortcuts import render, redirect
from .forms import OnboardingForm
from .models import TreinoGerado
from .schemas import validate_workout
from src.pipeline import workout_generator  # ajuste o caminho se necessário

def onboarding_view(request):
    if request.method == 'POST':
        form = OnboardingForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            # Gera treino com base no perfil preenchido
            profile_data = {
                "age": usuario.idade,
                "weight": usuario.peso,
                "goal": usuario.objetivo,
                "experience": usuario.nivel_condicionamento,
                "availability": usuario.frequencia_treino,
                "injuries": usuario.restricoes or "nenhuma"
            }

            resposta = workout_generator.generate_workout(profile_data)
            treino_validado = validate_workout(resposta)

            if treino_validado:
                TreinoGerado.objects.create(
                    usuario=usuario,
                    treino_texto=resposta,
                    modelo_usado="llama3-70b"
                )
                return redirect('mostrar_treino')
            else:
                form.add_error(None, "Erro ao gerar o treino. Tente novamente.")
    else:
        form = OnboardingForm()
    
    return render(request, 'onboarding.html', {'form': form})


def mostrar_treino(request):
    usuario = request.user
    treino = TreinoGerado.objects.filter(usuario=usuario).last()

    if treino:
        from json import loads
        try:
            treino_json = loads(treino.treino_texto)
        except:
            treino_json = {"erro": "Formato inválido"}
    else:
        treino_json = {"erro": "Nenhum treino gerado."}
    
    return render(request, 'treino.html', {'treino': treino_json})
