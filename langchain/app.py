from langchain_community.utilities import SQLDatabase
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent


project_path = os.path.dirname(__file__)
with open(os.path.join(project_path, ".env"), "r") as f:
    os.environ["OPENAI_API_KEY"] = f.readline()

def main():
    st.set_page_config(page_title="Ask Chinook")
    st.header("Ask Chinook")

    db = SQLDatabase.from_uri("sqlite:///movie.db")
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

    user_input = st.text_input("Ask a question: ")

    if user_input is not None and user_input != "":
        with st.spinner(text="Thinking..."):
            st.write(agent_executor.invoke(user_input))

if __name__ == "__main__":
    main()
