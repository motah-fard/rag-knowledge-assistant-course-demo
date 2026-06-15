question = "How many PTO days do employees get?"

bad_prompt = f"""
Answer the question confidently.

Question:
{question}
"""

bad_answer = """
Employees usually get 20 PTO days per year.
"""

print("Bad Prompt:")
print(bad_prompt)

print("\nBad Answer:")
print(bad_answer)

print("\nProblem:")
print("The assistant guessed instead of saying it does not know.")