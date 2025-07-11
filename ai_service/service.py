from typing import Dict
from models import ChatModel
from schemas import PeriodizationDict


class LLMService:
    def __init__(self, chat_model: ChatModel, model: str, prompt: str, temperature: float = 0.1):
        
        self.chat_model = chat_model
        self.model = model
        self.prompt = prompt
        self.temperature = temperature
    
    def generate_workout(self) -> Dict:
        llm = self.chat_model.instance_chat_model(
            model=self.model,
            temperature=self.temperature
        )        
        chain = llm.with_structured_output(PeriodizationDict)
        result = chain.invoke(self.prompt)
        print(result)
        return result
            