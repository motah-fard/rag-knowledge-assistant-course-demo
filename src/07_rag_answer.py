question = "How many PTO days do employees get?"

retrieved_context = """
Employees receive 15 paid time off days per year.
PTO requests must be submitted at least 7 days in advance.
"""

prompt = f"""
You are a helpful HR assistant.

Use only the context below to answer the question.
If the answer is not in the context, say you do not know.

Context:
{retrieved_context}

Question:
{question}

Answer:
"""

final_answer = "Employees receive 15 paid time off days per year."

print("RAG Prompt:")
print(prompt)

print("\nFinal Answer:")
print(final_answer)