---
type: concept
id: pretraining
title: Pre-training
description: The initial training stage where a language model learns general language patterns from large datasets.
tags:
  - training
  - llm
---

# Pre-training

Pre-training is the initial stage of training a language model on a large
dataset.

The model learns general patterns in language by optimizing an objective
such as next-token prediction.

## Key Idea

Given a sequence of tokens, the model learns to predict the next token.

## Relationships

- trains: [[llm]]
- uses: [[tokenization]]
- uses: [[transformer]]
- precedes: [[fine-tuning]]