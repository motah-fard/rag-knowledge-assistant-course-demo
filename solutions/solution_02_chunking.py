def chunk_text(text, chunk_size=120, overlap=30):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


sample_text = """
Employees receive 15 paid time off days per year.
PTO requests must be submitted at least 7 days in advance.
"""

chunks = chunk_text(sample_text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}")
    print(chunk)