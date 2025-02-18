from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Debugging: Print to check if keys are loaded (Remove after testing)
print("GROQ_API_KEY:", GROQ_API_KEY)
print("TAVILY_API_KEY:", TAVILY_API_KEY)
print("OPENAI_API_KEY:", OPENAI_API_KEY)
