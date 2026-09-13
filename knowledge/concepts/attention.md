---
type: concept
id: attention
title: Attention
description: A mechanism that allows a model to determine the importance of different tokens when processing a sequence.
tags:
  - transformer
  - attention
---

# Attention

Attention allows a neural network to determine which parts of an input
sequence are important when processing a particular token.

In Transformers, self-attention allows tokens to interact with other
tokens in the sequence.

## Key Idea

For a given token, attention calculates how strongly it should consider
other tokens when producing its representation.

## Relationships

- part_of: [[transformer]]
- enables: [[transformer]]
- operates_on: [[tokenization]]

## Example

In the sentence:

"The animal didn't cross the road because it was tired."

Attention helps the model determine what "it" refers to based on the
relationships between the tokens.