---
type: concept
id: parameter-efficient-fine-tuning
title: Parameter-Efficient Fine-Tuning
description: A family of methods that adapts a pretrained model by updating only a small number of parameters.
tags:
  - parameter-efficient-fine-tuning
  - peft
  - lora
  - fine-tuning
---

# Parameter-Efficient Fine-Tuning

Parameter-efficient fine-tuning (PEFT) adapts a pretrained model without
updating every model parameter. A small set of additional or selected
parameters is trained while the original model remains mostly frozen.

## Benefits

- Requires less memory and compute than full fine-tuning
- Produces smaller task-specific artifacts
- Makes it practical to adapt one base model to many tasks
- Reduces the storage cost of maintaining multiple model variants

## Common Methods

LoRA adds trainable low-rank matrices to selected layers. Other approaches
train adapters, prompts, or a small subset of the original parameters.

## Relationships

- includes: [[lora]]
- related_to: [[qlora]]
- related_to: [[fine-tuning]]
- uses: [[llm]]
