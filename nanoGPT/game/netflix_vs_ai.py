import random
import subprocess
import os

NETFLIX_FILE = "netflix_dialogues.txt"
GPT_OUT_DIR = "../out-shakespeare-char"

def load_netflix_dialogues():
    with open(NETFLIX_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_ai_dialogue():
    cmd = [
        "python", "../sample.py",
        "--device=cpu",
        f"--out_dir={GPT_OUT_DIR}",
        "--start=ROMEO:",
        "--max_new_tokens=60"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    # Extract only generated text
    output = result.stdout.split("---------------")[-1]
    return output.strip().replace("\n", " ")

def play_round(netflix_dialogues):
    is_ai = random.choice([True, False])

    if is_ai:
        dialogue = generate_ai_dialogue()
        correct = "ai"
    else:
        dialogue = random.choice(netflix_dialogues)
        correct = "netflix"

    print("\nDialogue:\n")
    print(dialogue)
    guess = input("\nNetflix or AI? ").strip().lower()

    if guess == correct:
        print("Correct! You get the point.")
        return "player"
    else:
        print(f"Wrong! It was {correct.upper()}. GPT gets the point.")
        return "gpt"

def main():
    netflix_dialogues = load_netflix_dialogues()
    player, gpt = 0, 0

    print("🎬 NETFLIX vs AI 🎭")
    print("Guess whether the dialogue is real or AI-generated.\n")

    for round_no in range(1, 6):
        print(f"\n--- Round {round_no} ---")
        winner = play_round(netflix_dialogues)

        if winner == "player":
            player += 1
        else:
            gpt += 1

        print(f"Score → You: {player} | GPT: {gpt}")

    print("\nGAME OVER")
    if player > gpt:
        print("You win! Humans still have taste.")
    elif gpt > player:
        print("GPT wins! The machines are learning.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
