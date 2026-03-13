from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
)

def get_weather(city: str) -> str:
    """
    This tool will get weather for a given city
    """
    return f"Its always sunny in {city}"


developer = create_agent(
    model=gemini_model,
    tools=[get_weather],
    system_prompt="You are a Senior Software Devloper, give the python code for {topic}"
)

response = developer.invoke(
    {
        "messages": [{"role": "user", "content": "What is the weather in new york"}]
    }
)

print(response['messages'][-1].content)