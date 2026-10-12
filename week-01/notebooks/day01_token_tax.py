"""Day 1 — Measure the token tax of the same sentence across tokenizers and languages."""
import tiktoken

SENTENCES = {
    "English": "Artificial intelligence is changing the world.",
    "Tamil": "செயற்கை நுண்ணறிவு உலகை மாற்றுகிறது.",
}

for name in ["gpt2", "cl100k_base", "o200k_base"]:
    enc = tiktoken.get_encoding(name)
    counts = {lang: len(enc.encode(s)) for lang, s in SENTENCES.items()}
    tax = counts["Tamil"] / counts["English"]
    print(f"{name:12} vocab={enc.n_vocab:>7}  " +
          "  ".join(f"{k}={v:3}" for k, v in counts.items()) + f"  Tamil tax={tax:.1f}x")
