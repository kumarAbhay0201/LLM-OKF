---
type: concept
id: qlora
title: QLoRA
description: A fine-tuning approach that combines LoRA with quantization to reduce memory requirements.
tags:
  - qlora
  - lora
  - quantization
  - peft
---

# QLoRA

QLoRA combines LoRA with quantization to make fine-tuning large models
more memory-efficient.

The pretrained model is loaded using a quantized representation while
LoRA adapters are trained for parameter-efficient adaptation.

## Key Idea

QLoRA combines:

- Quantization
- LoRA
- Parameter-efficient fine-tuning

## Relationships

- based_on: [[lora]]
- part_of: [[peft]]
- uses: [[quantization]]
- applied_to: [[llm]]
- related_to: [[fine-tuning]]