import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

class ChatModel(ABC):
    @abstractmethod
    def instance_chat_model(self, model: str, temperature: float):
        """ Cria instância do modelo de chat da Langchain """
        pass

class ChatGroqModel(ChatModel):
    def __init__(self):
        load_dotenv()
        self._api_key = os.environ.get("GROQ_API_KEY")
        if not self._api_key:
            raise ValueError("GROQ API KEY is not set.")
    
    def instance_chat_model(self, model: str, temperature: float) -> ChatGroq:
        return ChatGroq(
            groq_api_key=self._api_key,
            model=model,
            temperature=temperature
        )
        
class ChatGoogleGenerativeAIModel(ChatModel):
    def __init__(self):
        load_dotenv()
        self._api_key = os.environ.get("GEMINI_API_KEY")
        if not self._api_key:
            raise ValueError("GEMINI API KEY is not set.")
    
    def instance_chat_model(self, model: str, temperature: float) -> ChatGroq:
        return ChatGoogleGenerativeAI(
            api_key=self._api_key,
            model=model,
            temperature=temperature
        )
