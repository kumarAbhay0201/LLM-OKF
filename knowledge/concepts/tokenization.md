---
type: concept
id: tokenization
title: Tokenization
description: The process of converting text into tokens that can be processed by a language model.
tags:
  - llm
  - preprocessing
  - tokens
---

# Tokenization

Tokenization converts text into a sequence of tokens that can be processed
by a language model.

A token may represent a complete word, part of a word, punctuation, or
another unit depending on the tokenizer.

## Common Approaches

- Byte Pair Encoding (BPE)
- WordPiece
- SentencePiece

## Relationships

- required_by: [[llm]]
- processed_by: [[transformer]]
- precedes: [[embeddings]]

## Example

A word such as "unbelievable" may be represented as multiple tokens
depending on the tokenizer and vocabulary.