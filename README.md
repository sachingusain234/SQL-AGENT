# SQL Agent

An AI-powered agent that converts natural language questions into SQL queries and returns results from a MySQL database. Built with LangChain and Groq.

## Overview

This project uses LangChain's SQL Database Toolkit to create an agent that can:

- Explore database tables and schemas automatically
- Generate syntactically correct SQL queries from plain English questions
- Execute queries and return human-readable answers
- Self-correct by rewriting failed queries

## Tech Stack

- **LangChain** — Agent framework and SQL toolkit
- **Groq** — LLM inference (OpenAI GPT-OSS-120B)
- **MySQL** — Database backend
- **PyMySQL / SQLAlchemy** — Database connectivity

## Prerequisites

- Python 3.10+
- MySQL server running locally
- A [Groq API key](https://console.groq.com/)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/sql-agent.git
   cd sql-agent
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key
   MY_SQL_PASSWORD=your_mysql_password
   ```

5. **Ensure your MySQL database is running**

   The agent connects to a local MySQL database named `demo` on port `3306` with the `root` user. Update the connection string in `main.py` if your setup differs.

## Usage

```bash
python main.py
```

The agent will process the question defined in `main.py` and stream its step-by-step reasoning and results to the console.

To ask a different question, edit the `question` variable in `main.py`:

```python
question = "how many tables are present and write their name"
```

## How It Works

1. The LLM receives the user's natural language question along with a system prompt.
2. The agent first inspects the available tables in the database.
3. It queries the schema of the most relevant tables.
4. It generates and executes a SQL query to answer the question.
5. Results are streamed back step by step.

## License

This project is for educational/tutorial purposes.
