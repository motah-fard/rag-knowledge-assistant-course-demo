question = "How many PTO days do employees get?"

prompt = f"""
You are a helpful HR assistant.

Rules:
- Do not guess
- Be concise
- If the answer is not available, say:
  "I do not know based on the provided information."

Question:
{question}
"""

print(prompt)

answer = """
I do not know based on the provided information.
"""

print(answer)