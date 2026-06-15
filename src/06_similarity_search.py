from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer


def chunk_text(text, chunk_size=120, overlap=30):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


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

chunk_texts = [chunk["text"] for chunk in all_chunks]
chunk_embeddings = model.encode(chunk_texts)

question = "How many PTO days do employees get?"
question_embedding = model.encode([question])[0]

results = []

for index, chunk_embedding in enumerate(chunk_embeddings):
    score = cosine_similarity(question_embedding, chunk_embedding)

    results.append({
        "score": score,
        "chunk": all_chunks[index]
    })


results = sorted(results, key=lambda item: item["score"], reverse=True)

print("Question:", question)

print("\nTop retrieved chunks:")

for item in results[:3]:
    print("\n---")
    print("Score:", round(float(item["score"]), 4))
    print("Source:", item["chunk"]["source"])
    print(item["chunk"]["text"])