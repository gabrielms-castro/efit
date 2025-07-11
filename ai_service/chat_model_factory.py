from models import ChatGoogleGenerativeAIModel, ChatGroqModel


def chat_model_factory(chat_model):
    chat_model_dict = {
        "ChatGroq": ChatGroqModel,
        "ChatGoogle": ChatGoogleGenerativeAIModel
    }
    
    if chat_model not in chat_model_dict:
        raise ValueError("Chat Model não encontrado")
    
    return chat_model_dict[chat_model]( )