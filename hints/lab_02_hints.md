# Lab 2 Hints

## Hint 1

Generate embeddings for every chunk.

Which file already contains this logic?

Look at:

src/05_embeddings.py

---

## Hint 2

Generate an embedding for the user's question.

The question should be treated exactly like a chunk.

---

## Hint 3

Use cosine similarity.

Formula:

similarity = dot(a, b) / (norm(a) * norm(b))

---

## Hint 4

Store scores together with chunk metadata.

Example:

{
    "score": 0.87,
    "chunk": ...
}

---

## Hint 5

Sort results from highest similarity to lowest similarity.

---

## Hint 6

Return the top 3 chunks.

Do they contain the answer?