from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key= os.getenv("OPENAI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Use the web search agent to find information and the finance agent to analyze the data.",
    model=Groq(id="llama-3.3-70b-specdec"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tools_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-specdec"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True,
        key_financial_ratios=True,
        technical_indicators=True
    )],
    instructions=["Use tables to display the data and graphs if possible."],
    show_tools_calls=True,
    markdown=True,
)

# Multi-Agent System
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instruction=[
        "Use the web search agent to find information and the finance agent to analyze the data.",
        "Use tables to display the data and graphs if possible."
    ],
    show_tools_calls=True,
    markdown=True,
)

# Generate Response
print("Calling print_response method...")
result = multi_ai_agent.print_response("Summarize analyst recommendations and share the price of the latest news of NVDA.", stream=True)
print("Response:", result)

