from sentence_transformers import SentenceTransformer

texts = [
    "Employees receive 15 paid time off days per year.",
    "Employees must not share passwords."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(texts)

print("Shape:", embeddings.shape)
print("First vector preview:")
print(embeddings[0][:10])