import re

from app.okf.loader import load_knowledge


def tokenize(text: str):
    """
    Convert text into normalized words.
    """

    return set(
        re.findall(
            r"\b[a-zA-Z0-9-]+\b",
            text.lower()
        )
    )


def calculate_score(question: str, item: dict):
    """
    Calculate a simple relevance score for an OKF concept.

    Weighting:
    - Title match: 5
    - Tag match: 3
    - Description match: 2
    - Content match: 1
    """

    question_tokens = tokenize(question)

    score = 0

    title_tokens = tokenize(
        item["title"] or ""
    )

    description_tokens = tokenize(
        item["description"] or ""
    )

    content_tokens = tokenize(
        item["content"] or ""
    )

    tag_tokens = {
        tag.lower()
        for tag in item.get("tags", [])
    }

    # Strong signal: title
    score += len(
        question_tokens & title_tokens
    ) * 5

    # Medium signal: tags
    score += len(
        question_tokens & tag_tokens
    ) * 3

    # Medium/weak signal: description
    score += len(
        question_tokens & description_tokens
    ) * 2

    # Weak signal: content
    score += len(
        question_tokens & content_tokens
    )

    return score


def find_concepts(
    question: str,
    knowledge: dict,
    limit: int = 3
):
    """
    Find the most relevant OKF concepts for a question.
    """

    scored = []

    for item in knowledge.values():

        score = calculate_score(
            question,
            item
        )

        if score > 0:
            scored.append(
                (score, item)
            )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item
        for score, item in scored[:limit]
    ]


def traverse(
    knowledge: dict,
    start_id: str,
    max_depth: int = 2
):
    """
    Traverse relationships starting from a concept
    using depth-limited DFS.

    Returns both the retrieved concepts and the
    relationships used to reach them.
    """

    visited = set()
    results = []
    edges = []

    def dfs(
        current_id: str,
        depth: int
    ):

        if depth > max_depth:
            return

        if current_id in visited:
            return

        if current_id not in knowledge:
            return

        visited.add(current_id)

        current = knowledge[current_id]

        results.append(current)

        for relationship in current.get(
            "relationships",
            []
        ):

            target_id = relationship["target"]
            relation = relationship["relation"]

            # Ignore links to concepts that don't exist yet.
            if target_id not in knowledge:
                continue

            edges.append({
                "source": current_id,
                "relation": relation,
                "target": target_id,
            })

            dfs(
                target_id,
                depth + 1
            )

    dfs(start_id, 0)

    return {
        "nodes": results,
        "edges": edges,
    }

def format_path(
    knowledge: dict,
    edges: list
):
    """
    Convert graph edges into a human-readable
    knowledge traversal.
    """

    formatted = []

    for edge in edges:

        source_title = knowledge[
            edge["source"]
        ]["title"]

        target_title = knowledge[
            edge["target"]
        ]["title"]

        formatted.append({
            "source": edge["source"],
            "source_title": source_title,
            "relation": edge["relation"],
            "target": edge["target"],
            "target_title": target_title,
        })

    return formatted


def retrieve(
    question: str,
    concept_limit: int = 3,
    max_depth: int = 2
):
    """
    Retrieve relevant OKF knowledge and traverse
    related concepts.
    """

    knowledge = load_knowledge()

    starting_concepts = find_concepts(
        question,
        knowledge,
        limit=concept_limit
    )

    retrieved = {}
    paths = []

    for concept in starting_concepts:

        traversal = traverse(
            knowledge,
            concept["id"],
            max_depth
        )

        nodes = traversal["nodes"]
        edges = traversal["edges"]

        for item in nodes:
            retrieved[item["id"]] = item

        paths.append({
    "start": concept["id"],
    "nodes": [
        item["id"]
        for item in nodes
    ],
    "edges": format_path(
        knowledge,
        edges
    ),
})

    return {
        "concepts": list(
            retrieved.values()
        ),
        "paths": paths,
    }


def build_context(retrieved_concepts):
    """
    Convert retrieved OKF knowledge into
    context for the LLM.
    """

    sections = []

    for item in retrieved_concepts:

        section = f"""
## {item["title"]}

Description:
{item["description"]}

Knowledge:
{item["content"]}
"""

        sections.append(section)

    return "\n\n".join(sections)