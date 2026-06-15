from pathlib import Path
from sentence_transformers import SentenceTransformer


def chunk_text(text, chunk_size=120, overlap=30):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

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


model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk["text"] for chunk in all_chunks]
embeddings = model.encode(texts)

print("Number of chunks:", len(all_chunks))
print("Embedding shape:", embeddings.shape)
print("First embedding preview:")
print(embeddings[0][:10])