question = "What is the company maternity leave policy?"

retrieved_context = """
Employees receive 15 paid time off days per year.
Employees may book hotels up to $220 per night.
Employees must not share passwords with anyone.
"""

bad_answer = """
The company provides 12 weeks of maternity leave.
"""

good_answer = """
I do not know based on the provided information.
"""

print("Question:")
print(question)

print("\nRetrieved Context:")
print(retrieved_context)

print("\nBad Answer:")
print(bad_answer)

print("\nBetter Answer:")
print(good_answer)

print("\nProblem:")
print("The answer is not in the context, so the assistant should not invent it.")