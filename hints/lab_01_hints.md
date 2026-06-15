# Lab 1 Hints

## Hint 1

Start by loading all documents from the docs folder.

Useful concepts:

- Path
- glob()
- read_text()

---

## Hint 2

Create a chunking function.

Think about:

- chunk_size
- overlap

---

## Hint 3

Store chunk metadata.

Example:

{
    "source": "...",
    "chunk_id": 0,
    "text": "..."
}

---

## Hint 4

Print the chunks and inspect them manually.

Do they still contain meaningful information?

---

## Hint 5

Compare:

- chunk_size = 20
- chunk_size = 120
- chunk_size = 500

What changes?