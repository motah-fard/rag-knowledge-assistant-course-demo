from pathlib import Path


def chunk_text(text, chunk_size=20, overlap=0):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size

    return chunks


for file_path in Path("docs").glob("*.txt"):
    text = file_path.read_text()
    chunks = chunk_text(text)

    print("\nSource:", file_path.name)

    for index, chunk in enumerate(chunks[:5]):
        print("---")
        print("Chunk ID:", index)
        print(chunk)