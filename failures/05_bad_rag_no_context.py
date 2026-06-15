question = "How many PTO days do employees get?"

bad_prompt = f"""
You are a helpful HR assistant.

Answer the user's question.

Question:
{question}

Answer:
"""

bad_answer = """
Employees receive 20 paid time off days per year.
"""

print("Bad RAG Prompt:")
print(bad_prompt)

print("\nBad Answer:")
print(bad_answer)

print("\nProblem:")
print("There is no retrieved context, so the assistant guesses.")