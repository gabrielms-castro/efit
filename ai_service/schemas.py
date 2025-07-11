from typing_extensions import Annotated, Dict, List, TypedDict


class ExerciseDict(TypedDict):
    exercise_name: Annotated[str, ..., "Nome do exercício"]
    reps: Annotated[str, ..., "Número de repetições. Pode haver mínimas e máximas dependendo do exercício, intensidade e objetivo para autocomposição (ex: 2-4, 4-6, 6-8, 8-10, 10-12, 12-15, 15-20, 20-30)"]
    warmup_sets: Annotated[str, ..., "Número de séries de aquecimento para o exercício"]
    work_sets: Annotated[int, ..., "Número de séries principais para o exercício"]
    rest_time: Annotated[str, ..., "Faixa do tempo de descanso entre as séries (ex: 1-2 min, 2-3 min, 3-5 min)"]
    rpe: Annotated[str, ..., "Escala de percepção de esforço (RPE) mínima e máxima, de 1 a 10, podendo haver uma faixa (ex: 7-8, 8-9, 9-10)"]
    one_rep_max: Annotated[str, ..., "Para exercícios específicos e quando não aplicável o RPE, a estimativa de carga mínima e máxima como porcentagem do 1RM (ex: 70-80%, 80-90%)"]
    exercise_substitute: Annotated[str, ..., "Substituto sugerido para o exercício"]
    notes: Annotated[str, ..., "Notas ou orientações adicionais sobre o exercício"]

class TrainingDayDict(TypedDict):
    name: Annotated[str, ..., "Nome do dia de treino (ex: 'Push 1', 'Treino A', 'Full Body 3 - Foco em Pernas', etc.)"]
    exercises: Annotated[List[ExerciseDict], ..., "Lista de exercícios para o dia"]

class WeekDict(TypedDict):
    name: Annotated[str, ..., "Nome da semana (ex: 'Semana 1', 'Semana 2', etc.)"]
    training_days: Annotated[List[TrainingDayDict], ..., "Lista de dia de treino ao longo da semana"]
    
class PeriodizationDict(TypedDict):
    profile_analysis: Annotated[str, ..., "Análise do perfil do aluno gerada pela justificando o treino"]
    treino: Annotated[Dict[str, WeekDict], ..., "O treino dividido ao longo de 12 semanas (ex: 'Semana 1', 'Semana 2', etc.)"]
