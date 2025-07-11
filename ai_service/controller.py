from fastapi import FastAPI
from pydantic import BaseModel, Field
from service import LLMService
from chat_model_factory import chat_model_factory

app = FastAPI()

class WorkoutRequest(BaseModel):
    chat_model: str = Field(...)
    model: str = Field(...)
    temperature: float = Field(...)
    # prompt: str = Field(...)    

@app.get("/")
async def status():
    return {
        "status": "200 OK"
    }

@app.post("/generate_workout")
async def generate_workout(request: WorkoutRequest):
    with open("src/prompt.txt", "r", encoding="utf-8") as file:
        text = file.read()
    print(text)
    try:
        chat_model_instance = chat_model_factory(request.chat_model)
        
        llm_service = LLMService(
            chat_model=chat_model_instance,
            model=request.model,
            prompt=text,
            temperature=request.temperature
        )    
        result = llm_service.generate_workout()
        return {"sucess": True, "data": result}
    
    except Exception as exc:
        return {"sucess": False, "exception": str(exc)}