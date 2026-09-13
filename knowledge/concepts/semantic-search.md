---
type: concept
id: semantic-search
title: Semantic Search
description: A search method that finds information by meaning and intent rather than exact keyword matches.
tags:
  - semantic-search
  - embeddings
  - retrieval
  - rag
---

# Semantic Search

Semantic search finds information based on the meaning of a query. Instead of
matching only the exact words used in a document, it represents queries and
documents as embeddings and compares their semantic similarity.

## Typical Pipeline

User Query
-> Query Embedding
-> Similarity Search
-> Relevant Documents
-> Answer or Results

## Key Benefit

Semantic search can retrieve relevant content even when the query and the
stored document use different words to describe the same idea.

## Relationships

- uses: [[embeddings]]
- supports: [[rag]]
- related_to: [[llm]]
