---
type: concept
id: rag
title: Retrieval-Augmented Generation
description: A technique that retrieves external information and provides it to a language model during generation.
tags:
  - rag
  - retrieval
  - llm
---

# Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) combines information retrieval with
language generation.

A retrieval system finds relevant external information, which is then
provided to a language model as context.

## Typical Pipeline

User Query
→ Retrieval
→ Relevant Context
→ LLM
→ Answer

## Relationships

- uses: [[embeddings]]
- uses: [[llm]]
- related_to: [[fine-tuning]]
- alternative_to: [[persistent-knowledge-wiki]]