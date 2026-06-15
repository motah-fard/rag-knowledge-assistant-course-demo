# RAG Knowledge Assistant
### AI Engineering Course 1 Project

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![RAG](https://img.shields.io/badge/RAG-Knowledge%20Assistant-purple)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A step-by-step educational project for learning Retrieval-Augmented Generation (RAG) from first principles.

This repository accompanies the first course in an AI Engineering learning path and demonstrates how to build a complete document question-answering system using:

- Document Processing
- Chunking
- Embeddings
- Semantic Search
- Retrieval
- RAG
- Citations
- Streamlit

The project intentionally avoids heavy frameworks in order to make every stage of the pipeline visible and understandable.

---

# Learning Objectives

After completing this project, students should be able to:

- Explain why LLMs hallucinate
- Explain why prompting alone is insufficient
- Split documents into chunks
- Generate embeddings
- Perform semantic retrieval
- Build a RAG pipeline
- Display supporting evidence
- Build a simple knowledge assistant
- Diagnose common RAG failures

---

# Project Story

Imagine a company with hundreds of internal documents.

Employees ask questions such as:

- How many PTO days do employees get?
- What is the travel reimbursement policy?
- Can employees share passwords?

A traditional LLM does not know the answers.

Instead of guessing, we:

Load Documents
→ Chunk Documents
→ Generate Embeddings
→ Retrieve Relevant Chunks
→ Build Context
→ Generate Answer
→ Display Sources

The result is a simple but complete RAG system.

---

# Repository Structure

```text
docs/
src/
failures/
assignments/
labs/
hints/
solutions/
```

---

# Demo Progression

| Step | File | Concept |
|------|------|----------|
| 1 | 01_llm_without_context.py | LLM limitations |
| 2 | 02_prompt_engineering.py | Prompting |
| 3 | 03_load_documents.py | Document loading |
| 4 | 04_chunking.py | Chunking |
| 5 | 05_embeddings.py | Embeddings |
| 6 | 06_similarity_search.py | Semantic retrieval |
| 7 | 07_rag_answer.py | RAG |
| 8 | 08_sources.py | Citations |
| 9 | 09_streamlit_app.py | UI |

---

# Failure-First Learning

The repository includes intentionally broken examples:

- Bad Prompting
- Tiny Chunks
- Huge Chunks
- Keyword Search
- No Retrieved Context
- Unknown Questions

Students first observe failures, then implement the fixes.

---

# Assignments

Assignments reinforce each concept:

- Prompt Engineering
- Chunking
- Embeddings
- Similarity Search
- RAG
- Sources
- Final Project

---

# Labs

## Lab 1
Build a Document Search Pipeline

## Lab 2
Build a Retrieval Engine

## Lab 3
Build a Complete RAG Assistant

---

# Hints

Hints are provided for every lab without revealing the full implementation.

---

# Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# Running The Demos

```bash
python src/01_llm_without_context.py
python src/02_prompt_engineering.py
python src/03_load_documents.py
python src/04_chunking.py
python src/05_embeddings.py
python src/06_similarity_search.py
python src/07_rag_answer.py
python src/08_sources.py
```

Run Streamlit:

```bash
streamlit run src/09_streamlit_app.py
```

---

# Educational Philosophy

Concept
→ Demo
→ Failure Demo
→ Assignment
→ Lab
→ Hint

The goal is not to memorize code.

The goal is to understand why each part of a RAG system exists.

---

# Future Topics

Future courses expand into:

- AI Agents
- Tool Calling
- Memory
- Planning
- Multi-Agent Systems
- Evaluation
- Reliability
- Production AI Engineering

---

# License

MIT

---

# Author

Created as part of an AI Engineering course series focused on visual explanations, hands-on projects, and failure-first learning.


































///////////////////////////////////////////////////////////////////////////////////////////////

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