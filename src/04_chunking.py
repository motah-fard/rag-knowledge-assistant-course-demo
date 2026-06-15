from pathlib import Path


def chunk_text(text, chunk_size=120, overlap=30):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


documents = []

for file_path in Path("docs").glob("*.txt"):
    documents.append({
        "source": file_path.name,
        "text": file_path.read_text()
    })


all_chunks = []

for doc in documents:
    chunks = chunk_text(doc["text"])

    for index, chunk in enumerate(chunks):
        all_chunks.append({
            "source": doc["source"],
            "chunk_id": index,
            "text": chunk
        })


print(f"Total chunks: {len(all_chunks)}")

for chunk in all_chunks:
    print("\n---")
    print("Source:", chunk["source"])
    print("Chunk ID:", chunk["chunk_id"])
    print(chunk["text"])