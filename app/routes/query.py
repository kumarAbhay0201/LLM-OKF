from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retriever import (
    retrieve,
    build_context,
)

from app.services.groq_service import (
    generate_answer,
)


router = APIRouter(
    prefix="/api",
    tags=["query"]
)


class QuestionRequest(BaseModel):

    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        return {
            "success": False,
            "error": "Question cannot be empty.",
        }

    # --------------------------------
    # 1. Retrieve OKF knowledge
    # --------------------------------

    result = retrieve(
        question=question,
        concept_limit=3,
        max_depth=2,
    )

    concepts = result["concepts"]
    paths = result["paths"]

    # --------------------------------
    # 2. Build context
    # --------------------------------

    context = build_context(
        concepts
    )

    # --------------------------------
    # 3. Generate answer
    # --------------------------------

    answer = generate_answer(
        question=question,
        context=context,
    )

    # --------------------------------
    # 4. Return response
    # --------------------------------

    return {
        "success": True,
        "question": question,
        "answer": answer,

        "knowledge": {
            "concepts": [
                {
                    "id": item["id"],
                    "title": item["title"],
                }
                for item in concepts
            ],

            "paths": paths,
        },
    }

