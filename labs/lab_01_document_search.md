Lab 1 - Build a Document Search Pipeline

Objective

Build the first stage of a RAG system.

You will create a document processing pipeline that loads company policy documents and prepares them for retrieval.

⸻

Requirements

Step 1

Load all files from the docs folder.

Expected documents:

* pto_policy.txt
* travel_policy.txt
* security_policy.txt

⸻

Step 2

Split every document into chunks.

Requirements:

* chunk_size = 120
* overlap = 30

⸻

Step 3

Print the following information:

* document name
* chunk id
* chunk text

⸻

Example Output

Document: pto_policy.txt

Chunk 0

Employees receive 15 paid time off days per year.

⸻

Challenge

Experiment with:

* chunk_size = 20
* chunk_size = 500

Answer:

1. What breaks?
2. Which setting performs best?
3. Why?