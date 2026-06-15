question = "How many PTO days do employees get?"

prompt = f"""
You are a helpful HR assistant.

If you do not have enough information, say:
"I do not know based on the provided information."

Question:
{question}
"""

fake_llm_answer = """
I do not know based on the provided information.
"""

print("Prompt:")
print(prompt)

print("\nImproved answer:")
print(fake_llm_answer)