---
type: concept
id: quantization
title: Quantization
description: The process of representing model parameters using lower numerical precision to reduce memory and computation requirements.
tags:
  - optimization
  - inference
  - fine-tuning
---

# Quantization

Quantization reduces the numerical precision used to represent model
parameters.

For example, model weights may be represented using lower-bit formats
instead of higher-precision representations.

## Benefits

Quantization can reduce:

- Memory usage
- Storage requirements
- Computational requirements

## Relationships

- used_by: [[qlora]]
- related_to: [[llm]]
- supports: memory-efficient-model-adaptation