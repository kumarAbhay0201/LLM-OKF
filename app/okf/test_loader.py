import sys
from pathlib import Path


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


from app.okf.loader import load_knowledge


knowledge = load_knowledge()

print(f"Loaded {len(knowledge)} knowledge pages")

for knowledge_id, item in knowledge.items():

    print("\n--------------------")

    print("ID:", knowledge_id)
    print("Title:", item["title"])
    print("Tags:", item["tags"])
    print("Relationships:", item["relationships"])