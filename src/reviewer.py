from langchain_core.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash'
)

reviewer = create_agent(
    model=gemini_model,
    tools=[],
    system_prompt="You are a QA Specialist, given the code in python for {topic}, review and test it in the sandbox in consideration" \
    "of the business requirements as specified by consultant"
)