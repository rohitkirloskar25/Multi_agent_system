from langchain_core.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash'
)

consultant = create_agent(
    model=gemini_model,
    tools=[],
    system_prompt="You are a Technical Business Consultant. You job is to engage in conversation with consumer" \
    "and identify their requirements. Then communicate the specifications of the required software to the developer agent"
)