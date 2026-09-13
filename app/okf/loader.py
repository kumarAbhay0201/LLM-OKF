from pathlib import Path
import re
import yaml


KNOWLEDGE_DIR = Path(__file__).resolve().parents[2] / "knowledge" / "concepts"


def parse_frontmatter(content: str):
    """
    Extract YAML frontmatter from an OKF Markdown document.
    """

    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)

    if len(parts) < 3:
        return {}, content

    metadata = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()

    return metadata, body


def extract_relationships(content: str):
    """
    Extract relationships from the Markdown Relationships section.

    Example:

    - based_on: [[lora]]
    - uses: [[quantization]]
    """

    relationships = []

    pattern = r"-\s+(\w+):\s+\[\[([^\]]+)\]\]"

    matches = re.findall(pattern, content)

    for relation, target in matches:
        relationships.append({
            "relation": relation,
            "target": target,
        })

    return relationships


def load_knowledge():
    """
    Load all OKF concept files.
    """

    knowledge = {}

    for file_path in KNOWLEDGE_DIR.glob("*.md"):

        raw_content = file_path.read_text(
            encoding="utf-8"
        )

        metadata, body = parse_frontmatter(raw_content)

        relationships = extract_relationships(body)

        knowledge_id = metadata.get(
            "id",
            file_path.stem
        )

        knowledge[knowledge_id] = {
            "id": knowledge_id,
            "type": metadata.get("type"),
            "title": metadata.get("title"),
            "description": metadata.get("description"),
            "tags": metadata.get("tags", []),
            "content": body,
            "relationships": relationships,
            "file": str(file_path),
        }

    return knowledge