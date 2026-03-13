from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()
# Initialize Gemini with Native Google Search enabled
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash", # or gemini-2.0-flash
    google_search=True 
)

# 1. The Consultant
consultant = Agent(
  role='Business Consultant',
  goal='Transform vague ideas into technical specs',
  backstory='Expert at software architecture and user needs.',
  llm=gemini_llm,
  verbose=True
)

# 2. The Writer
developer = Agent(
  role='Senior Python Developer',
  goal='Write optimized, bug-free code',
  backstory='Specializes in clean code and efficient algorithms.',
  llm='gemini-3-flash'
)

# 3. The Reviewer
qa_engineer = Agent(
  role='QA Specialist',
  goal='Ensure code matches business logic and is bug-free',
  backstory='Obsessed with edge cases and business alignment.',
  llm='gemini-3-flash'
)



task1 = Task(description="Define specs for {topic}}", agent=consultant)
task2 = Task(description="Write code based on specs from Task 1", agent=developer)
task3 = Task(description="Review code against original specs. If bugs found, restart Task 2.", agent=qa_engineer)

# Assemble the Crew
software_factory = Crew(
  agents=[consultant, developer, qa_engineer],
  tasks=[task1, task2, task3],
  process='sequential' # They work one after another
)

result = software_factory.kickoff(inputs={'topic': 'a real-time weather dashboard'})

