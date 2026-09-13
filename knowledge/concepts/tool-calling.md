---
type: concept
id: tool-calling
title: Tool Calling
description: A capability that lets a language model request external tools or functions to perform actions or retrieve data.
tags:
  - tool-calling
  - agents
  - llm
---

# Tool Calling

Tool calling allows a language model to select a registered function and
provide structured arguments for it. The application executes the function
and returns its result to the model so it can continue the response.

## Typical Flow

User Request
-> LLM Selects Tool
-> Application Executes Tool
-> Tool Result
-> LLM Produces Response

## Common Uses

- Querying databases or APIs
- Running calculations
- Retrieving current information
- Taking actions in external systems

## Relationships

- enables: [[agents]]
- uses: [[llm]]
- related_to: [[rag]]
