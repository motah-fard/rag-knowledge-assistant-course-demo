from pathlib import Path

question = "How much vacation do employees get?"

documents = []

for file_path in Path("docs").glob("*.txt"):
    documents.append({
        "source": file_path.name,
        "text": file_path.read_text()
    })


results = []

for doc in documents:
    score = 0

    for word in question.lower().split():
        if word in doc["text"].lower():
            score += 1

    results.append({
        "score": score,
        "source": doc["source"],
        "text": doc["text"]
    })


results = sorted(results, key=lambda item: item["score"], reverse=True)

print("Question:")
print(question)

print("\nKeyword search results:")

for item in results:
    print("\n---")
    print("Score:", item["score"])
    print("Source:", item["source"])
    print(item["text"][:150])