import os


def answer_question(question: str, context: list[dict[str, str]]) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Set GROQ_API_KEY in .env to enable model answers."

    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        context_text = "\n\n".join(item["content"] for item in context)
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            messages=[
                {"role": "system", "content": "Answer using the supplied knowledge context. Say when the context is insufficient."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {question}"},
            ],
        )
        return response.choices[0].message.content or "No answer returned."
    except Exception as error:
        return f"Unable to contact Groq: {error}"
