import os
import streamlit as st
from crewai import Agent, Task, Process, Crew
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definição dos Agentes
gerador = Agent(
  role='Greeting Generator',
  goal='Generate a greeting message',
  backstory="""You are an agent that generates a simple greeting message. Your task is to create a basic greeting.""",
  verbose=True,
  allow_delegation=False
)

verificador = Agent(
  role='Greeting Verifier',
  goal='Verify and improve the greeting message',
  backstory="""You are an agent that checks the greeting message for any errors or improvements. Your task is to ensure the greeting is friendly and polite.""",
  verbose=True,
  allow_delegation=False
)

enviador = Agent(
  role='Greeting Sender',
  goal='Send the final greeting message',
  backstory="""You are an agent that sends the final greeting message. Your task is to ensure the message is sent out properly.""",
  verbose=True,
  allow_delegation=False
)

# Definição das Tarefas
task_generate = Task(
    description="""Generate a simple greeting message. Your message should be something like 'Hello, world!'.""",
    agent=gerador,
    expected_output="A simple greeting message"
)

task_verify = Task(
    description="""Verify the greeting message and make any necessary improvements. Ensure it is friendly and polite.""",
    agent=verificador,
    expected_output="A verified and improved greeting message"
)

task_send = Task(
    description="""Send the final greeting message. Confirm that the message is sent successfully.""",
    agent=enviador,
    expected_output="Confirmation of greeting message sent"
)

# Instanciação da Crew
crew = Crew(
  agents=[gerador, verificador, enviador],
  tasks=[task_generate, task_verify, task_send],
  verbose=2,
  process=Process.sequential
)

# Interface Streamlit
st.title("CrewAI - Greeting Agents")
st.write("Este aplicativo utiliza agentes para gerar, verificar e enviar uma mensagem de saudação.")

if st.button("Iniciar Agentes"):
    result = crew.kickoff()
    st.success("Agentes executados com sucesso!")
    st.write("### Resultado:")
    st.write(result)
###teste