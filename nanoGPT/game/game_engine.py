import random
from real_texts import REAL_TEXTS

AI_PROMPTS = [
    "A dark story about power and betrayal.",
    "A dramatic tale of loss and ambition.",
    "A secret that changes everything."
]

def get_round(model, meta):
    is_ai = random.choice([True, False])

    if is_ai:
        prompt = random.choice(AI_PROMPTS)
        from ai_generator import generate_text
        text = generate_text(prompt, model, meta)
        answer = "AI"
    else:
        text = random.choice(REAL_TEXTS)
        answer = "HUMAN"

    return text.strip(), answer
