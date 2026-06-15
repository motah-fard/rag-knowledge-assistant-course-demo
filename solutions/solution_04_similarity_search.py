from sentence_transformers import SentenceTransformer
import numpy as np

texts = [
    "Employees receive 15 paid time off days per year.",
    "Employees may book hotels up to $220 per night.",
    "Employees must not share passwords."
]

question = "How many vacation days do employees get?"

model = SentenceTransformer("all-MiniLM-L6-v2")

text_embeddings = model.encode(texts)
question_embedding = model.encode([question])[0]


def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


results = []

for i, emb in enumerate(text_embeddings):
    score = cosine_similarity(question_embedding, emb)

    results.append({
        "score": score,
        "text": texts[i]
    })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

for item in results:
    print(item["score"])
    print(item["text"])
    print()