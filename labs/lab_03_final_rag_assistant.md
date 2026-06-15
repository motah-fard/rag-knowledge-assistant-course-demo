Final Lab - Build a Complete RAG Assistant

Objective

Build a complete company knowledge assistant.

⸻

Requirements

Your application must:

1. Load documents
2. Create chunks
3. Generate embeddings
4. Retrieve relevant chunks
5. Build a RAG prompt
6. Generate an answer
7. Display sources
8. Display supporting evidence

⸻

UI Requirements

Build a simple Streamlit application.

Required elements:

* text input
* answer section
* source section
* retrieved context section

⸻

Test Questions

How many PTO days do employees get?

What is the travel reimbursement policy?

Can employees share passwords?

⸻

Failure Test

Ask a question that does not exist in the documents.

Example:

What is the maternity leave policy?

Expected Result:

The assistant should respond:

“I do not know based on the provided information.”

⸻

Bonus

Add a new document:

remote_work_policy.txt

Verify that retrieval continues to work correctly.