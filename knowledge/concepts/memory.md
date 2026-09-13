---
type: concept
id: memory
title: Memory
description: A mechanism that allows an AI system to retain and use information across interactions or within a task.
tags:
  - memory
  - agents
  - rag
---

# Memory

Memory gives an AI system access to information beyond the immediate prompt.
It can store conversation history, user preferences, task state, or durable
knowledge and retrieve that information when it becomes relevant.

## Main Types

- Short-term memory: Information available during the current interaction
- Long-term memory: Information stored for future interactions
- Working memory: Intermediate facts and state used during a task

## Design Considerations

A memory system should decide what to store, when to retrieve it, and how to
keep outdated or incorrect information from affecting later responses.

## Relationships

- supports: [[agents]]
- uses: [[rag]]
- related_to: [[embeddings]]
