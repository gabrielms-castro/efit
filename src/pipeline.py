# src/pipeline.py (versão otimizada)
import json
from typing import Dict, Any
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import logging
import os

logger = logging.getLogger(__name__)

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DIR = os.getenv("CHROMA_DIR")

class WorkoutGenerator:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama3-70b-8192",
            temperature=0.3
        )
        
        self.vectorstore = Chroma(
            collection_name="efit_treinos",
            embedding_function=OpenAIEmbeddings(api_key=OPENAI_API_KEY),
            persist_directory=CHROMA_DIR
        )
        
        self.prompt = self._create_prompt_template()
        self.chain = self._create_llm_chain()

    def _create_prompt_template(self):
        template = """
        [Seu template otimizado anteriormente aqui...]
        """
        return PromptTemplate(
            input_variables=["input"],
            template=template,
            validate_template=True
        )

    def _create_llm_chain(self):
        return LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=False
        )

    def _parse_response(self, response_text: str) -> Dict:
        try:
            json_str = response_text.strip().replace("```json", "").replace("```", "")
            return json.loads(json_str)
        except json.JSONDecodeError:
            logger.error("Invalid JSON response from LLM")
            return {"error": "Invalid workout format"}

    def _format_profile_input(self, data: Dict) -> str:
        return (
            f"Idade: {data['age']}, "
            f"Peso: {data['weight']}kg, "
            f"Objetivo: {data['goal']}, "
            f"Nível: {data['experience']}, "
            f"Disponibilidade: {data['availability']} dias/semana, "
            f"Lesões: {data['injuries']}"
        )
        
    def generate_workout(self, profile_data: Dict) -> Dict[str, Any]:
        try:
            formatted_input = self._format_profile_input(profile_data)
            response = self.chain.invoke({"input": formatted_input})
            return self._parse_response(response["text"])
        except Exception as e:
            logger.error(f"Error generating workout: {str(e)}")
            return {"error": "Failed to generate workout"}        


# Singleton para reutilização
workout_generator = WorkoutGenerator()

if __name__ == "__main__":
    resultado = workout_generator.generate_workout({
        "age": 22,
        "weight": 70,
        "goal": "Hipertrofia",
        "experience": "Intermediário",
        "availability": 4,
        "injuries": "Nenhuma"
    })
    print(resultado)