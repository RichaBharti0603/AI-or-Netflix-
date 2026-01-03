import torch
from model import GPTConfig, GPT
import pickle

# Load model checkpoint
def load_model(out_dir="out-shakespeare-char", device="cpu"):
    ckpt_path = f"{out_dir}/ckpt.pt"
    checkpoint = torch.load(ckpt_path, map_location=device)

    gptconf = GPTConfig(**checkpoint["model_args"])
    model = GPT(gptconf)
    model.load_state_dict(checkpoint["model"])
    model.eval()

    with open(f"{out_dir}/meta.pkl", "rb") as f:
        meta = pickle.load(f)

    return model, meta


def generate_text(prompt, model, meta, max_new_tokens=120):
    stoi, itos = meta["stoi"], meta["itos"]

    def encode(s): return [stoi[c] for c in s]
    def decode(l): return "".join([itos[i] for i in l])

    idx = torch.tensor([encode(prompt)], dtype=torch.long)
    with torch.no_grad():
        out = model.generate(idx, max_new_tokens=max_new_tokens)
    return decode(out[0].tolist())
