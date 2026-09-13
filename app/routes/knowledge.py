
from fastapi import APIRouter

from app.okf.loader import load_knowledge


router = APIRouter(
    prefix="/api/knowledge",
    tags=["knowledge"],
)


@router.get("/graph")
def get_knowledge_graph():

    knowledge = load_knowledge()

    nodes = []
    edges = []

    for item in knowledge.values():

        nodes.append({
            "id": item["id"],
            "title": item["title"],
        })

        for relationship in item.get(
            "relationships",
            []
        ):

            target = relationship["target"]

            if target not in knowledge:
                continue

            edges.append({
                "source": item["id"],
                "relation": relationship["relation"],
                "target": target,
            })

    return {
        "nodes": nodes,
        "edges": edges,
    }