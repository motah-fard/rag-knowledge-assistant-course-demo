# RAG Knowledge Assistant

This project teaches the full RAG pipeline step by step.

You will learn:

- Why LLMs fail without private context
- How prompting improves behavior
- How to load documents
- How to chunk text
- How embeddings work
- How similarity search retrieves relevant chunks
- How to build a simple RAG assistant
- How to show sources
- How to build a simple UI

- ## Project Story

We are building an internal company knowledge assistant.

The assistant should answer employee questions using company policy documents.

Example questions:

- How many PTO days do employees get?
- What is the hotel budget for travel?
- Can employees share passwords?


# Assignment 1: Prompting

## Goal

Improve the assistant's behavior when it does not have enough context.

## Task

Update the prompt so the assistant:

1. Does not guess
2. Says "I do not know" when the answer is missing
3. Answers briefly
4. Uses a friendly tone

## Test Questions

- How many PTO days do employees get?
- What is the company bonus policy?
- Can employees work from another country?

## Expected Behavior

The assistant should not invent answers.

# Assignment 2: Chunking

## Goal

Understand how chunk size changes retrieval quality.

## Task

Run the chunking script with:

- chunk_size = 50
- chunk_size = 120
- chunk_size = 500

Compare the results.

## Questions

1. Which chunk size gives better context?
2. Which chunk size loses meaning?
3. Which chunk size includes too much unrelated information?

# Assignment 3: Embeddings

## Goal

Use embeddings to compare meaning, not just keywords.

## Task

Ask these questions:

- How much vacation do employees get?
- What is the hotel limit?
- Can I share my password?

For each question, print the top retrieved chunk.

## Expected Result

The system should retrieve the correct policy even when the wording is different.

# Assignment 4: RAG

## Goal

Build a RAG prompt using retrieved context.

## Task

Use the top 3 retrieved chunks as context.

Create a prompt that tells the model:

1. Use only the provided context
2. Do not guess
3. Include a short answer
4. Include the source file

## Failure Test

Ask:

"What is the company maternity leave policy?"

If the answer is not in the documents, the assistant should say it does not know.


# Final Project: Company Knowledge Assistant

## Goal

Build a simple RAG assistant for company policy questions.

## Requirements

Your app should:

1. Load documents from the docs folder
2. Split documents into chunks
3. Create embeddings
4. Retrieve the top 3 relevant chunks
5. Generate an answer using the retrieved context
6. Show the source document
7. Handle unknown questions without hallucinating

## Bonus

Add a simple Streamlit UI.


Video 1: Demo project overview
Video 2: LLM without context
Video 3: Better prompting
Video 4: Load documents
Video 5: Chunking
Video 6: Chunking failure demo
Video 7: Embeddings
Video 8: Similarity search
Video 9: Retrieval failure demo
Video 10: RAG prompt
Video 11: Final answer with sources
Video 12: Streamlit UI
Video 13: Final assignment walkthrough

For each section:

What breaks?
Why does it break?
How do we fix it?