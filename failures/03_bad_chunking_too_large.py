from pathlib import Path


def chunk_text(text, chunk_size=2000, overlap=0):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size

    return chunks


all_chunks = []

for file_path in Path("docs").glob("*.txt"):
    text = file_path.read_text()

    for index, chunk in enumerate(chunk_text(text)):
        all_chunks.append({
            "source": file_path.name,
            "chunk_id": index,
            "text": chunk
        })


print("Total chunks:", len(all_chunks))

for chunk in all_chunks:
    print("\n---")
    print("Source:", chunk["source"])
    print(chunk["text"])