from pathlib import Path

DOCS_DIR = Path("docs")

documents = []

for file_path in DOCS_DIR.glob("*.txt"):
    documents.append({
        "source": file_path.name,
        "text": file_path.read_text()
    })

print("Loaded documents:")

for doc in documents:
    print("-", doc["source"])