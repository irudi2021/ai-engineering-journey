"""Day 1 — Byte Pair Encoding from scratch (training + encoding)."""
from collections import Counter

def train_bpe(corpus: dict[str, int], num_merges: int):
    # Each word is a tuple of symbols; "</w>" marks end-of-word.
    vocab = {tuple(w) + ("</w>",): f for w, f in corpus.items()}
    merges = []
    for step in range(1, num_merges + 1):
        pairs = Counter()
        for word, freq in vocab.items():
            for a, b in zip(word, word[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best, count = pairs.most_common(1)[0]
        merges.append(best)
        print(f"merge {step}: {best[0]!r} + {best[1]!r} -> {best[0] + best[1]!r}  (count={count})")
        new_vocab = {}
        for word, freq in vocab.items():
            out, i = [], 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == best:
                    out.append(word[i] + word[i + 1]); i += 2
                else:
                    out.append(word[i]); i += 1
            new_vocab[tuple(out)] = freq
        vocab = new_vocab
    return merges

def encode(word: str, merges):
    symbols = list(word) + ["</w>"]
    for a, b in merges:                      # apply merges in learned order
        i, out = 0, []
        while i < len(symbols):
            if i < len(symbols) - 1 and symbols[i] == a and symbols[i + 1] == b:
                out.append(a + b); i += 2
            else:
                out.append(symbols[i]); i += 1
        symbols = out
    return symbols

if __name__ == "__main__":
    corpus = {"low": 5, "lower": 2, "newest": 6, "widest": 3}
    merges = train_bpe(corpus, 10)
    for w in ["lowest", "newer", "wider"]:
        print(w, "->", encode(w, merges))
