question = "How many PTO days do employees get?"

retrieved_context = """
Employees receive 15 paid time off days per year.
PTO requests must be submitted at least 7 days in advance.
"""

prompt = f"""
Use only the context below.

Context:
{retrieved_context}

Question:
{question}

Answer:
"""

print(prompt)

answer = """
Employees receive 15 paid time off days per year.
"""

print(answer)