---
type: concept
id: fine-tuning
title: Fine-Tuning
description: Additional training performed on a pretrained model to adapt it to a specific task or behavior.
tags:
  - training
  - adaptation
  - llm
---

# Fine-Tuning

Fine-tuning adapts a pretrained model using additional training data.

Instead of training a model entirely from scratch, fine-tuning starts
from an existing pretrained model.

## Uses

Fine-tuning can be used to:

- Adapt a model to a domain
- Improve task-specific performance
- Teach instruction-following behavior
- Change model behavior

## Relationships

- follows: [[pretraining]]
- applied_to: [[llm]]
- includes: [[peft]]
- related_to: [[lora]]
- related_to: [[qlora]]