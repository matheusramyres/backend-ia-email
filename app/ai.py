from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

def generate_email(prompt: str) -> str:
    result = generator(prompt)
    return result[0]["generated_text"]
