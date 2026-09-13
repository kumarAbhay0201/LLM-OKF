import sys
from pathlib import Path


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    service_directory = Path(__file__).resolve().parent
    sys.path[:] = [
        entry
        for entry in sys.path
        if Path(entry or ".").resolve() != service_directory
    ]
    sys.path.insert(0, str(project_root))


from app.services.groq_service import generate_answer


context = """
## LoRA

LoRA (Low-Rank Adaptation) is a parameter-efficient
fine-tuning technique.

Instead of updating the original model weights directly,
LoRA learns small low-rank matrices that represent
weight updates.

## QLoRA

QLoRA combines LoRA with quantization to make
fine-tuning large models more memory-efficient.

## Parameter-Efficient Fine-Tuning

PEFT refers to techniques that adapt a pretrained model
without updating all of its parameters.
"""


question = "What is the relationship between LoRA and QLoRA?"


answer = generate_answer(
    question,
    context
)


print("\nANSWER:")
print(answer)
