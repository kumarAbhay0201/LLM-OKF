import sys
from pathlib import Path


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


from app.services.retriever import retrieve, build_context


question = "How does QLoRA help with fine-tuning?"

result = retrieve(question)

print("\nMATCHED KNOWLEDGE:")
for item in result["concepts"]:
    print("-", item["id"])

print("\nKNOWLEDGE PATHS:")
for path in result["paths"]:
    print(
        path["start"],
        "→",
        " → ".join(path["nodes"])
    )

print("\nCONTEXT:")
print(
    build_context(
        result["concepts"]
    )
)