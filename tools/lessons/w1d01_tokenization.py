#!/usr/bin/env python3
"""Week 1 Day 01 — Tokenization lesson PDF. Usage: w1d01_tokenization.py <out.pdf>"""
import os, sys
from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, Preformatted, NextPageTemplate, Image as RLImage)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

DAY_DATE, NEXT_DATE = "Monday 19 October 2026", "Tue 20 Oct 2026"
out = sys.argv[1]
SUP = "/System/Library/Fonts/Supplemental/"
for n, f in [("U", "Arial Unicode.ttf"), ("UB", "Arial Bold.ttf"), ("UI", "Arial Italic.ttf"), ("UBI", "Arial Bold Italic.ttf")]:
    pdfmetrics.registerFont(TTFont(n, SUP + f))
pdfmetrics.registerFont(TTFont("Mono", "/System/Library/Fonts/Menlo.ttc", subfontIndex=0))
addMapping("U", 0, 0, "U"); addMapping("U", 1, 0, "UB"); addMapping("U", 0, 1, "UI"); addMapping("U", 1, 1, "UBI")

# Tamil needs complex-script shaping, which ReportLab lacks: render it with PIL + raqm.
TAMIL = "செயற்கை நுண்ணறிவு உலகை மாற்றுகிறது."
tamil_png = os.path.splitext(out)[0] + "_tamil.png"
_f = ImageFont.truetype(SUP + "Tamil Sangam MN.ttc", 96, layout_engine=ImageFont.Layout.RAQM)
l, t_, r, b = _f.getbbox(TAMIL, language="ta")
_img = PILImage.new("RGB", (r - l + 20, b - t_ + 30), "white")
ImageDraw.Draw(_img).text((10 - l, 15 - t_), TAMIL, font=_f, fill="black", language="ta")
_img.save(tamil_png)

NAVY, TEAL, AMBER = colors.HexColor("#14213D"), colors.HexColor("#0E7C86"), colors.HexColor("#B8860B")
LIGHT, ZEBRA, WARM, CODEBG = colors.HexColor("#E8F1F2"), colors.HexColor("#F6F8FA"), colors.HexColor("#FFF7E0"), colors.HexColor("#F3F4F6")
S = lambda name, **kw: ParagraphStyle(name, fontName="U", **kw)
H1 = S("h1", fontSize=16, leading=20, textColor=NAVY, spaceBefore=6, spaceAfter=6, keepWithNext=1)
H2 = S("h2", fontSize=12.5, leading=16, textColor=TEAL, spaceBefore=8, spaceAfter=4, keepWithNext=1)
P = S("p", fontSize=9.6, leading=13.2, spaceAfter=5)
LI = S("li", fontSize=9.6, leading=13.2, leftIndent=13, bulletIndent=3, spaceAfter=2)
CELL = S("c", fontSize=8.4, leading=10.8); CELLH = S("ch", fontSize=8.4, leading=10.8, textColor=colors.white)
CALL = S("call", fontSize=9.4, leading=13, borderPadding=(6, 7, 6, 7), spaceAfter=8)
CODE = ParagraphStyle("code", fontName="Mono", fontSize=7.9, leading=9.8, backColor=CODEBG,
                      borderPadding=(5, 6, 5, 6), spaceAfter=8, spaceBefore=2)
W = A4[0] - 30 * mm
story = []
h1 = lambda t: story.append(Paragraph(t, H1))
h2 = lambda t: story.append(Paragraph(t, H2))
p = lambda t: story.append(Paragraph(t, P))
def ul(items):
    for it in items: story.append(Paragraph(it, LI, bulletText="•"))
    story.append(Spacer(1, 3))
def ol(items):
    for i, it in enumerate(items, 1): story.append(Paragraph(it, LI, bulletText=f"{i}."))
    story.append(Spacer(1, 3))
def code(t): story.append(Preformatted(t.strip("\n"), CODE))
def call(title, body, bg=LIGHT, edge=TEAL):
    t = Table([[Paragraph(f"<b>{title}</b><br/>{body}", CALL)]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3, edge),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.extend([t, Spacer(1, 7)])
def table(rows, widths, head=NAVY, zebra=ZEBRA):
    data = [[Paragraph(str(c), CELLH if i == 0 else CELL) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=[W * x for x in widths], repeatRows=1)
    sty = [("BACKGROUND", (0, 0), (-1, 0), head), ("VALIGN", (0, 0), (-1, -1), "TOP"),
           ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#C9D3DD")),
           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    sty += [("BACKGROUND", (0, i), (-1, i), zebra) for i in range(2, len(data), 2)]
    t.setStyle(TableStyle(sty)); story.extend([t, Spacer(1, 8)])

# ───────────────────────────── CONTENT ─────────────────────────────
story.append(NextPageTemplate("body")); story.append(PageBreak())

h1("1. Why Tokenization Is Day 1")
p("A language model never sees text. It sees a list of integers. <b>Tokenization</b> is the step that turns "
  "your string into those integers, and turns the model's integers back into text. Every number you will "
  "care about as an AI engineer — <b>cost, latency, context-window capacity, rate limits, and even accuracy</b> — "
  "is measured in tokens, not characters or words.")
call("Architect's one-liner",
     "The tokenizer is part of the model's contract. Change the model and you may change the tokenizer — and "
     "with it your bill, your context budget and your failure modes.")
h2("The pipeline")
code("""
 "Tokenization matters!"
        │  1. normalise      (Unicode NFC/NFKC, optional lower-casing)
        ▼
 "Tokenization matters!"
        │  2. pre-tokenise   (split on spaces, punctuation, digit runs)
        ▼
 ["Token","ization"," matters","!"]   ◄─ 3. subword model (BPE / WordPiece / Unigram)
        │  4. map to IDs     (lookup in the vocabulary)
        ▼
 [ 3404, 2065, 13146, 0 ]   ◄─ cl100k_base, measured
        │  5. embedding lookup → vectors → transformer   (Day 2, Day 3)
        ▼
 model output IDs → detokenise → text
""")

h1("2. Three Ways to Cut Text")
table([["Granularity", "Example: \"unbelievable\"", "Strength", "Fatal weakness"],
       ["Word-level", "[unbelievable]", "Short sequences; intuitive", "Huge vocabulary; any unseen word becomes [UNK] (out-of-vocabulary)"],
       ["Character-level", "[u,n,b,e,l,i,e,v,a,b,l,e]", "Tiny vocabulary; never [UNK]", "Very long sequences; attention cost grows with length; meaning is spread thin"],
       ["<b>Subword</b> (modern LLMs)", "[un, belie, vable] (cl100k_base, measured)", "Frequent words stay whole; rare words decompose; no [UNK]", "Splits are statistical, not linguistic — causes quirks (Section 6)"]],
      [0.17, 0.27, 0.25, 0.31])
p("Subword tokenization is the compromise every frontier and open-weight LLM uses today. "
  "The vocabulary is a fixed set of pieces (typically ~30K to ~260K) learned from a training corpus.")

h1("3. Byte Pair Encoding (BPE) — The Workhorse")
p("<b>Training idea:</b> start with single symbols, count every adjacent pair across the corpus, merge the most "
  "frequent pair into a new symbol, and repeat until the vocabulary reaches the target size. The ordered list "
  "of merges <i>is</i> the tokenizer. BPE was adapted from data compression to neural machine translation by "
  "Sennrich et al. (2016).")
p("<b>Encoding a new word:</b> split into characters, then apply the learned merges in the same order.")
h2("Worked run — real output from week-01/notebooks/day01_bpe_from_scratch.py")
p("Corpus (word: frequency) = low: 5, lower: 2, newest: 6, widest: 3. The marker &lt;/w&gt; means end-of-word.")
code("""
merge 1: 'e' + 's' -> 'es'  (count=9)
merge 2: 'es' + 't' -> 'est'  (count=9)
merge 3: 'est' + '</w>' -> 'est</w>'  (count=9)
merge 4: 'l' + 'o' -> 'lo'  (count=7)
merge 5: 'lo' + 'w' -> 'low'  (count=7)
merge 6: 'n' + 'e' -> 'ne'  (count=6)
merge 7: 'ne' + 'w' -> 'new'  (count=6)
merge 8: 'new' + 'est</w>' -> 'newest</w>'  (count=6)
merge 9: 'low' + '</w>' -> 'low</w>'  (count=5)
merge 10: 'w' + 'i' -> 'wi'  (count=3)
lowest -> ['low', 'est</w>']
newer -> ['new', 'e', 'r', '</w>']
wider -> ['wi', 'd', 'e', 'r', '</w>']
""")
p("Notice: <b>lowest</b> never appeared in training, yet it encodes cleanly as <i>low + est</i>. "
  "<b>newer</b> and <b>wider</b> fall back to single characters for the parts the merges never covered. "
  "That graceful fallback is why subword models have no out-of-vocabulary problem.")
h2("Byte-level BPE — why modern models never emit [UNK]")
p("Instead of starting from Unicode characters, byte-level BPE starts from the <b>256 possible byte values</b>. "
  "Any string in any language, emoji or binary-ish noise is a sequence of UTF-8 bytes, so it can always be "
  "encoded. GPT-2 popularised this; the open-source <b>tiktoken</b> library implements the same family "
  "(encodings <i>gpt2</i>, <i>cl100k_base</i>, <i>o200k_base</i>). Before merging, a regex <b>pre-tokeniser</b> "
  "splits text into chunks (words with their leading space, digit runs, punctuation) so merges never cross "
  "those boundaries.")

h1("4. The Other Algorithms and Who Uses Them")
table([["Algorithm", "How it builds the vocabulary", "Notes"],
       ["<b>BPE</b>", "Bottom-up: merge the most frequent adjacent pair", "Deterministic, simple, fast; byte-level variant has no [UNK]"],
       ["<b>WordPiece</b>", "Bottom-up: merge the pair that most increases training-data likelihood (score ≈ count(ab) ÷ (count(a)·count(b)))", "Google's BERT; continuation pieces are marked with ## (e.g. play, ##ing)"],
       ["<b>Unigram LM</b>", "Top-down: start with a huge candidate set, repeatedly prune pieces that least hurt likelihood", "Probabilistic — a word can have several segmentations; enables subword regularisation (Kudo, 2018)"],
       ["<b>SentencePiece</b>", "A library/framework, not a separate algorithm — runs BPE or Unigram directly on raw text", "Treats the space as a symbol (▁), so it is language-agnostic and fully reversible; from Google"]],
      [0.16, 0.46, 0.38])
h2("FAANG tokenizer choices (published figures)")
table([["Company / model", "Tokenizer", "Vocabulary", "Why it matters"],
       ["<b>Google</b> — BERT", "WordPiece", "~30K", "Classic encoder baseline; the ## convention you will see in NLP code"],
       ["<b>Google</b> — T5", "SentencePiece (Unigram)", "32K", "Text-to-text models; reversible ▁ spaces"],
       ["<b>Google</b> — PaLM / Gemma", "SentencePiece", "~256K", "Very large multilingual vocabulary reduces fragmentation in languages such as Tamil"],
       ["<b>Meta</b> — Llama 2", "SentencePiece (BPE)", "32K", "Small vocab → more tokens per sentence"],
       ["<b>Meta</b> — Llama 3", "tiktoken-based BPE", "128K (100K + 28K non-English)", "Meta reports English compression improved from 3.17 to 3.94 characters per token vs Llama 2"],
       ["<b>Apple</b> — Apple Intelligence (2024 report)", "BPE-family", "49K on-device / 100K server", "Smaller vocabulary on device saves memory in the embedding table (Section 7)"]],
      [0.24, 0.19, 0.2, 0.37])

h1("5. Special Tokens and Chat Templates")
p("Every vocabulary reserves <b>special tokens</b> that never come from normal text: beginning/end of sequence, "
  "padding, and the markers that separate system, user and assistant turns. A <b>chat template</b> is the exact "
  "recipe for wrapping a conversation in those markers. Example (Meta Llama 3 family):")
code("""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a helpful assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>

What is a token?<|eot_id|><|start_header_id|>assistant<|end_header_id|>
""")
ul(["<b>Wrong template = silent quality loss.</b> The model still answers, just worse. When self-hosting open "
    "models, always apply the template shipped with the tokenizer.",
    "<b>Security:</b> if user text containing the string \"&lt;|endoftext|&gt;\" were encoded as the real special "
    "token, a user could forge turn boundaries. tiktoken refuses by default — measured below."])
code("""
>>> enc = tiktoken.get_encoding("cl100k_base")
>>> enc.encode("<|endoftext|>")
ValueError: Encountered text corresponding to disallowed special token '<|endoftext|>'.
>>> enc.encode("<|endoftext|>", allowed_special="all")   # trusted text only
[100257]
>>> enc.encode("<|endoftext|>", disallowed_special=())     # treat as plain text
[27, 91, 8862, 728, 428, 91, 29]
""")

h1("6. Quirks Lab — Real cl100k_base Output")
table([["Input", "Token IDs", "Pieces", "Lesson"],
       ["'hello'", "[15339]", "hello", "Common word = 1 token"],
       ["' hello'", "[24748]", "␣hello", "Leading space creates a <b>different</b> token"],
       ["'Hello'", "[9906]", "Hello", "Case creates a different token"],
       ["' HELLO'", "[38757, 1623]", "␣HEL | LO", "Rare casing fragments"],
       ["'strawberry'", "[496, 675, 15717]", "str | aw | berry", "Why letter-counting is hard: the model never sees individual letters"],
       ["' strawberry'", "[73700]", "␣strawberry", "Same word, one token with a leading space"],
       ["'1234567'", "[4513, 10961, 22]", "123 | 456 | 7", "Numbers are chunked in up to 3 digits — arithmetic sees chunks, not digits"],
       ["'2026-10-12'", "[2366, 21, 12, 605, 12, 717]", "202 | 6 | - | 10 | - | 12", "Dates cost 6 tokens; the year is split"],
       ["' tokenization'", "[4037, 2065]", "␣token | ization", "Morphology emerges from statistics"]],
      [0.15, 0.22, 0.2, 0.43])
call("Production lesson — the prompt boundary problem",
     "Because ' hello' and 'hello' are different tokens, a prompt that ends with a trailing space pushes the "
     "model into an unusual token path and can degrade the completion. <b>Microsoft</b>'s open-source Guidance "
     "library addresses this with <i>token healing</i>: it backs up one token at the prompt boundary and constrains "
     "generation to continue the removed text. Practical rule: strip trailing whitespace from prompts.",
     bg=WARM, edge=AMBER)

h1("7. Tokens Are Money, Latency and Memory")
ul(["<b>Money.</b> Providers price input and output per token (e.g. <b>Amazon</b> Bedrock on-demand pricing). "
    "Output tokens usually cost more than input tokens.",
    "<b>Latency.</b> Input tokens are processed in parallel; output tokens are generated one at a time. "
    "Output length dominates response time.",
    "<b>Context.</b> A \"128K context window\" means 128K <i>tokens of that model's tokenizer</i> — not a fixed "
    "amount of text.",
    "<b>Rule of thumb (English only):</b> roughly 4 characters or ~0.75 words per token. Never apply it to "
    "other languages or code — measure."])
h2("The vocabulary-size trade-off")
p("The embedding table holds one vector per token: <b>parameters = V × d</b>. For a 128,256-token vocabulary and "
  "a 4,096-dimensional model (Meta Llama 3 8B sizes) that is 128,256 × 4,096 ≈ <b>525 million parameters</b>, "
  "about 1.05 GB in 16-bit precision — before the output layer, which has a matching matrix unless weights are tied.")
table([["Bigger vocabulary", "Smaller vocabulary"],
       ["Fewer tokens per sentence → cheaper, faster, more text fits in context", "More tokens per sentence → higher cost and latency"],
       ["Better coverage of many languages and code", "Rare languages fragment into bytes"],
       ["Larger embedding/output matrices → more memory, bigger softmax", "Smaller memory footprint — why <b>Apple</b> chose 49K on-device vs 100K on server"],
       ["Rare tokens get little training signal (under-trained 'glitch' tokens)", "Each token is seen more often in training"]],
      [0.5, 0.5])

h1("8. 2026 Addition — Tokenizer Differences and the Token Tax")
p("The same sentence costs different numbers of tokens on different model families, and non-English text "
  "usually costs <b>far</b> more. Measured with week-01/notebooks/day01_token_tax.py:")
p("English: <i>Artificial intelligence is changing the world.</i> (46 characters)")
story.append(Table([[Paragraph("Tamil:", P), RLImage(tamil_png, width=62 * mm, height=62 * mm * _img.height / _img.width),
                     Paragraph("(35 characters, 97 UTF-8 bytes — same meaning)", P)]],
                   colWidths=[13 * mm, 66 * mm, W - 79 * mm],
                   style=[("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
table([["Encoding", "Vocabulary", "English tokens", "Tamil tokens", "Tamil token tax"],
       ["gpt2", "50,257", "8", "97", "<b>12.1×</b>"],
       ["cl100k_base", "100,277", "8", "49", "<b>6.1×</b>"],
       ["o200k_base", "200,019", "7", "14", "<b>2.0×</b>"]],
      [0.2, 0.18, 0.2, 0.2, 0.22], head=AMBER, zebra=WARM)
ul(["<b>Why 97 tokens for gpt2?</b> Each Tamil character is 3 bytes in UTF-8. With almost no Tamil merges learned, "
    "byte-level BPE falls back to one token per byte: 97 bytes → 97 tokens.",
    "<b>Why it improves:</b> larger, deliberately multilingual vocabularies learn Tamil merges. Meta added 28K "
    "non-English tokens to Llama 3; Google's ~256K SentencePiece vocabulary was designed for broad language coverage.",
    "<b>Research backing:</b> Petrov et al., <i>Language Model Tokenizers Introduce Unfairness Between Languages</i> "
    "(NeurIPS 2023), found up to 15× differences in tokenized length for the same content across languages."])
h2("What the token tax does to a product")
table([["Effect", "Impact for a Tamil-speaking user (6.1× tax example)"],
       ["Cost", "The same answer costs ~6× more"],
       ["Context", "A fixed token window holds ~1/6 as much Tamil text — RAG can retrieve fewer documents"],
       ["Latency", "Generating a Tamil reply takes many more decode steps"],
       ["Quality", "Fragmented tokens carry less meaning each; models are often weaker in heavily fragmented languages"],
       ["Rate limits", "Tokens-per-minute quotas are exhausted sooner"]], [0.2, 0.8])
h2("Cross-family rules for 2026")
ol(["<b>Compare cost per task, not price per token.</b> A cheaper per-token model with a less efficient "
    "tokenizer for your language can cost more per answer.",
    "<b>Count with the model's own tokenizer.</b> Use the provider's token-counting API or the published tokenizer "
    "— never another family's tokenizer as a proxy.",
    "<b>Budget per language.</b> Set context, cost and rate-limit budgets per locale, measured on real traffic.",
    "<b>Re-measure on every model migration.</b> Model churn in 2026 is monthly; a tokenizer change silently "
    "moves every cost and capacity number."])

h1("9. Real-World Scenarios")
table([["Company", "Scenario", "Tokenization decision"],
       ["<b>Meta</b>", "Llama 3 serves many languages to open-weight users", "Grew vocabulary 32K → 128K, adding 28K non-English tokens; better compression with no English regression (Meta's paper)"],
       ["<b>Google</b>", "Gemma / PaLM must work across many scripts", "~256K SentencePiece vocabulary to avoid fragmenting languages such as Tamil"],
       ["<b>Apple</b>", "On-device model with tight memory", "49K vocabulary on device vs 100K on server (2024 report) — vocabulary size is a memory decision"],
       ["<b>Microsoft</b>", "Prompt-boundary artefacts in constrained generation", "Guidance library's token healing"],
       ["<b>Amazon</b>", "Bedrock bills each model per input/output token", "Customers must forecast spend with each model's own tokenizer"],
       ["<b>Netflix</b> <i>(illustrative scenario)</i>", "Generating synopses in many languages", "A per-language token budget would be needed: a fixed English budget would truncate or overspend in fragmented languages"]],
      [0.14, 0.33, 0.53])

h1("10. Architect's Lens")
table([["Decision", "Question to ask", "Default"],
       ["Model choice", "What is the token tax for <i>our</i> languages and data (code, JSON, tables)?", "Measure on a 1,000-sample real-traffic set before choosing"],
       ["Capacity planning", "Tokens/sec and tokens/minute at p95 — per locale?", "Plan in tokens, never characters"],
       ["Context budget", "How many tokens are left for retrieval after system prompt + history?", "Reserve output tokens first"],
       ["Self-hosting", "Is the exact tokenizer + chat template shipped with the weights?", "Pin tokenizer version with model version"],
       ["Security", "Can user input be encoded as special tokens?", "Encode user text as plain text only"],
       ["Migration", "Did the tokenizer change between model versions?", "Re-run cost and context tests on every upgrade"]],
      [0.18, 0.47, 0.35])
h2("Failure modes to recognise in production")
ul(["Bill jumps after a model upgrade with no traffic change → tokenizer changed.",
    "Non-English users report truncated answers → context budget set in English token terms.",
    "Model miscounts letters or digits → it sees chunks, not characters; use code/tools for exact counting.",
    "Self-hosted model answers poorly → wrong chat template.",
    "Weird completions after prompts ending in spaces → prompt-boundary problem."])

h1("11. Hands-On Exercises")
ol(["<b>Run BPE from scratch.</b> Execute week-01/notebooks/day01_bpe_from_scratch.py. Change the corpus to "
    "{\"hug\": 10, \"pug\": 5, \"pun\": 12, \"bun\": 4, \"hugs\": 5} and predict the first 3 merges before running.",
    "<b>Measure your own token tax.</b> Add a Tamil paragraph from a news site and its English translation to "
    "day01_token_tax.py. Record the tax for all three encodings.",
    "<b>Break the model.</b> Encode 'strawberry', ' strawberry', 'Strawberry' and 'STRAWBERRY' with cl100k_base. "
    "Explain why letter-counting questions fail.",
    "<b>Number chunks.</b> Encode 1000000, 1,000,000 and 1e6. Which format would you choose in prompts that ask for arithmetic, and why?",
    "<b>Architect write-up (½ page).</b> Your product serves English and Tamil users. Using today's numbers, "
    "write how you would set the context budget and monthly cost forecast per language."])
code("""
pip install tiktoken
python week-01/notebooks/day01_bpe_from_scratch.py
python week-01/notebooks/day01_token_tax.py
""")

h1("12. Key Takeaways")
ol(["Models read integer token IDs; the tokenizer is part of the model's contract.",
    "Subword tokenization (BPE, WordPiece, Unigram via SentencePiece) balances vocabulary size and sequence length.",
    "Byte-level BPE starts from 256 bytes, so nothing is ever out-of-vocabulary.",
    "Cost, latency, context and rate limits are all measured in tokens.",
    "Spaces, case and digits change tokenization — the root of many 'dumb' model failures.",
    "Vocabulary size trades memory against sequence length.",
    "2026: the same text costs different token counts per model family, and non-English text can cost 2–12× more "
    "(measured) — compare cost per task, measure per language, and re-measure on every model migration."])
call(f"Next — Day 2 · {NEXT_DATE} · Embeddings",
     "Token IDs become vectors. 2026 addition: Matryoshka (truncatable) embeddings, multi-vector late interaction "
     "(ColBERT) and multimodal embeddings.")
h2("References")
ul(["Sennrich, Haddow &amp; Birch (2016), <i>Neural Machine Translation of Rare Words with Subword Units</i>.",
    "Kudo (2018), <i>Subword Regularization</i>; Kudo &amp; Richardson (2018), <i>SentencePiece</i>.",
    "Petrov et al. (2023), <i>Language Model Tokenizers Introduce Unfairness Between Languages</i>, NeurIPS.",
    "Meta (2024), <i>The Llama 3 Herd of Models</i> — arxiv.org/abs/2407.21783.",
    "Apple (2024), <i>Apple Intelligence Foundation Language Models</i> — machinelearning.apple.com.",
    "Microsoft Guidance — github.com/guidance-ai/guidance (token healing).",
    "tiktoken — github.com/openai/tiktoken."])

# ───────────────────────────── PAGES ─────────────────────────────
def deco(c, doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, A4[1] - 9 * mm, A4[0], 9 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("U", 8)
    c.drawString(15 * mm, A4[1] - 6 * mm, "AI Engineering · Week 1 · Day 1 · Tokenization")
    c.drawRightString(A4[0] - 15 * mm, A4[1] - 6 * mm, DAY_DATE)
    c.setFillColor(colors.grey); c.drawCentredString(A4[0] / 2, 8 * mm, f"Page {doc.page}"); c.restoreState()
def cover(c, doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setFillColor(TEAL); c.rect(0, A4[1] * 0.45, A4[0], 3, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#9FD8DC")); c.setFont("U", 13)
    c.drawString(22 * mm, A4[1] - 60 * mm, f"WEEK 1 · DAY 1 · {DAY_DATE.upper()}")
    c.setFillColor(colors.white); c.setFont("UB", 34); c.drawString(22 * mm, A4[1] - 80 * mm, "Tokenization")
    c.setFont("U", 13); c.drawString(22 * mm, A4[1] - 92 * mm, "How text becomes numbers — and why it sets your bill")
    y = A4[1] * 0.45 - 16 * mm; c.setFont("U", 11)
    for t in ["BPE · WordPiece · Unigram · SentencePiece · byte-level BPE",
              "Special tokens & chat templates · quirks lab · vocabulary trade-offs",
              "2026 addition: tokenizer differences & the non-English token tax (measured)", "",
              "Week 1 · Foundations — LLM internals", "Instructor: Pro AI Principal Architect"]:
        c.drawString(22 * mm, y, t); y -= 7 * mm
    c.setFont("U", 9); c.setFillColor(colors.HexColor("#9FB3C8"))
    c.drawString(22 * mm, 18 * mm, "github.com/irudi2021/ai-engineering-journey · week-01/notes"); c.restoreState()

doc = BaseDocTemplate(out, pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm, topMargin=15 * mm,
                      bottomMargin=14 * mm, title="Week 1 Day 1 — Tokenization", author="Pro AI Principal Architect")
fr = Frame(doc.leftMargin, doc.bottomMargin, W, A4[1] - 29 * mm, id="f")
doc.addPageTemplates([PageTemplate("cover", [fr], onPage=cover), PageTemplate("body", [fr], onPage=deco)])
doc.build(story)
os.remove(tamil_png)
print("✓ built", out)
