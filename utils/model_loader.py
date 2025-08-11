import os
from dotenv import load_dotenv
from typing import Optional, Any, Literal
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq

load_dotenv()

class ConfigLoader:
    def __init__(self):
        print("Loading configuration...")
        self.config=load_config()
    
    def __getitem__(self,key):
        return self.config[key]

class ModelLoader(BaseModel):
    
    model_provider: Literal["groq","openai"]= "groq"
    config: Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self,__context: Any) -> None:
        self.config=ConfigLoader()

    class Config:
        arbitrary_types_allowed=True
    
    def load_llm(self):
        """
        Load the LLM model based on the provider specified in the config.
        """
        print("Loading LLM model...")
        print(f"Model provider: {self.model_provider}")
        if self.model_provider=="groq":
            print("Loading Groq model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name= self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(
                model=model_name,
                api_key=groq_api_key,
            )
        return llm
