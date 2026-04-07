import ollama

def get_explanation(topic, mode):
    if mode == "eli5":
        prompt = f"""Explain '{topic}' to a 5 year old.
Use a simple real-life analogy.
No jargon. Max 5 bullet points. Short sentences."""
    else:
        prompt = f"""Explain '{topic}' to a senior software engineer.
Be technical and precise. No fluff.
Use structured bullet points."""

    response = ollama.chat(
        model="gemma4:e4b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


topic = "API"

print("=== ELI5 MODE ===")
print(get_explanation(topic, "eli5"))

print("\n=== SENIOR MODE ===")
print(get_explanation(topic, "senior"))
