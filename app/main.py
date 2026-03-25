from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
)

# Composable prompt (not hardcoded translation)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant. {task}"),
    ("user", "{text}")
])

# Output parser
parser = StrOutputParser()

# LCEL chain
chain = prompt_template | model | parser

# FastAPI app
app = FastAPI(
    title="Composable LLM Pipeline API",
    description="An API demonstrating LCEL-based composable LLM pipelines",
    version="1.0"
)

# Add LangServe routes
add_routes(
    app,
    chain,
    path="/chain"
)

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)