import random
from ai_generator import generate_text

# ---------------- Load Netflix dialogues ----------------
def load_netflix_dialogues():
    path = "data/netflix_dialogues.txt"  # ensure this file exists
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

NETFLIX_LINES = load_netflix_dialogues()

# ---------------- Generate a game round ----------------
def get_round(difficulty="Easy"):
    """
    Returns a dict: {"dialogue": <text>, "source": "Netflix"/"AI"}
    """
    use_ai = random.random() < 0.5  # 50% AI or Netflix
    if use_ai:
        # AI generated dialogue
        text = generate_text(prompt="Create a short dialogue:", max_new_tokens=50)
        return {"dialogue": text, "source": "AI"}
    else:
        dialogue = random.choice(NETFLIX_LINES)
        return {"dialogue": dialogue, "source": "Netflix"}
