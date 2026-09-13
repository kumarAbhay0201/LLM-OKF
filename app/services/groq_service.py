import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def generate_answer(
    question: str,
    context: str,
    request_api_key: str | None = None,
):
    """
    Generate an answer using the Groq-hosted LLM.

    The model is instructed to use the OKF
    knowledge as its primary knowledge source.
    """

    system_prompt = """
You are an assistant that answers questions about
Large Language Models.

You are connected to a structured knowledge system
called LLM-OKF.

The knowledge provided by the system is the primary
source of truth for answering the user's question.

Instructions:

1. Use the provided OKF knowledge first.
2. Do not invent facts that contradict the knowledge.
3. If the knowledge does not contain enough information,
   clearly say that the knowledge base does not contain
   enough information.
4. Explain the answer clearly.
5. Do not mention internal implementation details
   unless the user asks.
"""

    user_prompt = f"""
KNOWLEDGE FROM OKF
==================

{context}


USER QUESTION
=============

{question}


Answer the user's question using the knowledge above.
"""

    api_key = request_api_key or os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL")

    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured on the server.")

    if not model:
        raise RuntimeError("GROQ_MODEL is not configured on the server.")

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content