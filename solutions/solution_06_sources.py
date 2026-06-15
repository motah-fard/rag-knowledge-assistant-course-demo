answer = """
Employees receive 15 paid time off days per year.
"""

source = {
    "file": "pto_policy.txt",
    "chunk_id": 0,
    "text": "Employees receive 15 paid time off days per year."
}

print("Answer:")
print(answer)

print("\nSource File:")
print(source["file"])

print("\nChunk ID:")
print(source["chunk_id"])

print("\nEvidence:")
print(source["text"])