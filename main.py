import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from urllib.parse import quote_plus
from langchain.agents import create_agent

load_dotenv()
# Model initialization
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key
)



password = os.getenv("MY_SQL_PASSWORD")

# Encode special characters like @, #, %, !
encoded_password = quote_plus(password)

db = SQLDatabase.from_uri(
    f"mysql+pymysql://root:{encoded_password}@localhost:3306/demo"
)



toolkit = SQLDatabaseToolkit(db=db, llm=model)

tools = toolkit.get_tools()
system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

You MUST double check your query before executing it. If you get an error while
executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
database.

To start you should ALWAYS look at the tables in the database to see what you
can query. Do NOT skip this step.

Then you should query the schema of the most relevant tables.
""".format(
    dialect=db.dialect,
    top_k=5,
)


agent = create_agent(
    model,
    tools,
    system_prompt=system_prompt,
)

question = "how many tables are present and write their name"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()