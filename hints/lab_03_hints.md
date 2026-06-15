# Final Lab Hints

## Hint 1

The final system combines everything from previous sections.

Pipeline:

Question
↓
Embeddings
↓
Retrieval
↓
Context
↓
Answer

---

## Hint 2

Build a context string from the top retrieved chunks.

Use:

join()

---

## Hint 3

Your prompt should contain:

- Instructions
- Context
- Question

---

## Hint 4

The assistant should not guess.

If the answer is not in the context:

"I do not know based on the provided information."

---

## Hint 5

Display source information.

At minimum:

- source file
- chunk id

---

## Hint 6

Build a simple Streamlit interface.

Required:

- question input
- answer output
- source display

---

## Hint 7

Test with an unknown question.

Example:

What is the maternity leave policy?

Does the assistant hallucinate?