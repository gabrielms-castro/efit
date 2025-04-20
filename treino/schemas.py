from pydantic import BaseModel, ValidationError
import logging

logger = logging.getLogger(__name__)
class ExerciseSchema(BaseModel):
    nome: str
    series: int
    repeticoes: str
    rpe: int
    carga_estimada_kg: float
    descanso: str
    observacoes: str

def validate_workout(data: dict):
    try:
        treino = data.get("treino")
        if not treino or "exercicios" not in treino:
            raise KeyError("Campo 'treino' ou 'exercicios' ausente na resposta")
        return [ExerciseSchema(**ex) for ex in treino["exercicios"]]
    except (ValidationError, KeyError) as e:
        logger.error(f"Validation error: {str(e)}")
        return None