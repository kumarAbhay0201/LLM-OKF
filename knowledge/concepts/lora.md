---
type: concept
id: lora
title: LoRA
description: Low-Rank Adaptation, a parameter-efficient technique for adapting pretrained models.
tags:
  - lora
  - peft
  - fine-tuning
---

# LoRA

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique.

Instead of updating the original model weights directly, LoRA learns
small low-rank matrices that represent weight updates.

## Benefits

LoRA can:

- Reduce trainable parameters
- Reduce memory requirements
- Make model adaptation more efficient
- Allow smaller adapter weights to be stored separately

## Relationships

- part_of: [[peft]]
- type_of: [[fine-tuning]]
- applied_to: [[llm]]
- related_to: [[qlora]]