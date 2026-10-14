#!/usr/bin/env python3
"""Render the complete syllabus PDF from SCHEDULE.md (overview) + CURRICULUM_MASTER.md (all content).
Usage: build_syllabus_pdf.py <repo> <out.pdf>"""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, NextPageTemplate)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

repo, out = sys.argv[1], sys.argv[2]
SUP = "/System/Library/Fonts/Supplemental/"
for n, f in [("U", "Arial Unicode.ttf"), ("UB", "Arial Bold.ttf"), ("UI", "Arial Italic.ttf"), ("UBI", "Arial Bold Italic.ttf")]:
    pdfmetrics.registerFont(TTFont(n, SUP + f))
pdfmetrics.registerFont(TTFont("Mono", "/System/Library/Fonts/Menlo.ttc", subfontIndex=0))
addMapping("U", 0, 0, "U"); addMapping("U", 1, 0, "UB"); addMapping("U", 0, 1, "UI"); addMapping("U", 1, 1, "UBI")

NAVY, TEAL, AMBER = colors.HexColor("#14213D"), colors.HexColor("#0E7C86"), colors.HexColor("#B8860B")
LIGHT, ZEBRA, LAYERBG = colors.HexColor("#E8F1F2"), colors.HexColor("#F6F8FA"), colors.HexColor("#FFF7E0")
S = lambda name, **kw: ParagraphStyle(name, fontName="U", **kw)
st = {
 "h1": S("h1", fontSize=17, leading=21, textColor=NAVY, spaceBefore=4, spaceAfter=8, keepWithNext=1),
 "h2": S("h2", fontSize=13.5, leading=17, textColor=TEAL, spaceBefore=10, spaceAfter=5, keepWithNext=1),
 "h3": S("h3", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=8, spaceAfter=4, keepWithNext=1),
 "p":  S("p", fontSize=9.2, leading=12.4, spaceAfter=4),
 "li": S("li", fontSize=9.2, leading=12.4, leftIndent=12, bulletIndent=2, spaceAfter=1.5),
 "q":  S("q", fontSize=9, leading=12, leftIndent=10, textColor=colors.HexColor("#33415C"),
          borderPadding=(4, 6, 4, 6), backColor=LIGHT, spaceAfter=0),
 "cell": S("cell", fontSize=8.1, leading=10.2),
 "cellh": S("cellh", fontSize=8.1, leading=10.2, textColor=colors.white),
}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️]")
TAMIL = re.compile("[஀-௿]")

def inline(t):
    t = EMOJI.sub("", t).strip()
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\[`?([^\]`]+)`?\]\([^)]+\)", r"\1", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Mono" size="7.6">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    for seg in re.findall(r"<b>(.*?)</b>|<i>(.*?)</i>", t):
        assert not TAMIL.search("".join(seg)), f"Tamil inside bold/italic (no glyphs): {seg}"
    return t

def md_table(lines, width):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c) for c in r)]
    n = len(rows[0]); layer = "2026" in rows[0][-1]
    lens = [max(len(re.sub(r"[*`]", "", r[i])) if i < len(r) else 0 for r in rows) for i in range(n)]
    lens = [max(l, len(rows[0][i])) for i, l in enumerate(lens)]
    fixed = {i: max(10, (l + 2) * 1.75) * mm for i, l in enumerate(lens) if l <= 12}
    rest = width - sum(fixed.values()); flex = {i: min(l, 70) for i, l in enumerate(lens) if i not in fixed}
    cw = [fixed[i] if i in fixed else rest * flex[i] / sum(flex.values()) for i in range(n)]
    data = [[Paragraph(inline(c), st["cellh"] if i == 0 else st["cell"]) for c in r + [""] * (n - len(r))]
            for i, r in enumerate(rows)]
    t = Table(data, colWidths=cw, repeatRows=1)
    sty = [("BACKGROUND", (0, 0), (-1, 0), AMBER if layer else NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
           ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#C9D3DD")),
           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
           ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    sty += [("BACKGROUND", (0, i), (-1, i), LAYERBG if layer else ZEBRA) for i in range(2, len(data), 2)]
    t.setStyle(TableStyle(sty))
    return t

def render(md, width, breaks=()):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        s = lines[i].strip()
        if not s or s == "---": i += 1; continue
        if s.startswith("|"):
            blk = []
            while i < len(lines) and lines[i].strip().startswith("|"): blk.append(lines[i]); i += 1
            out += [md_table(blk, width), Spacer(1, 6)]; continue
        if s.startswith(">"):
            blk = []
            while i < len(lines) and lines[i].strip().startswith(">"): blk.append(lines[i].strip()[1:].strip()); i += 1
            paras = " ".join(b if b else "<br/><br/>" for b in blk)
            out += [Paragraph(inline(paras).replace("&lt;br/&gt;", "<br/>"), st["q"]), Spacer(1, 7)]; continue
        m = re.match(r"(#{1,3}) (.*)", s)
        if m:
            txt = m.group(2)
            if any(txt.startswith(b) for b in breaks) and out: out.append(PageBreak())
            out.append(Paragraph(inline(txt), st[f"h{len(m.group(1))}"])); i += 1; continue
        m = re.match(r"(\d+)\. (.*)", s)
        if m: out.append(Paragraph(inline(m.group(2)), st["li"], bulletText=f"{m.group(1)}.")); i += 1; continue
        if s.startswith("- "): out.append(Paragraph(inline(s[2:]), st["li"], bulletText="•")); i += 1; continue
        para = inline(s); i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"[|>#]|-\s|\d+\.\s|---", lines[i].strip()):
            nxt = lines[i].strip(); para += ("<br/>" if nxt.startswith("**") else " ") + inline(nxt); i += 1
        out.append(Paragraph(para, st["p"]))
    return out

sched = open(f"{repo}/SCHEDULE.md").read()
master = open(f"{repo}/CURRICULUM_MASTER.md").read()
run = re.search(r"\*\*Day 1: (.+?) → Day 84: (.+?) —", sched)
D1, D84 = run.group(1).replace(",", ""), run.group(2).replace(",", "")   # "Monday 19 October 2026"
short = lambda s: (lambda w: f"{w[1]} {w[2][:3]} {w[3]}")(s.split())  # "19 Oct 2026"
HDR = f"AI Engineering Intensive · 12 Weeks · {short(D1)} – {short(D84)}"

def deco(c, doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, A4[1] - 9 * mm, A4[0], 9 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("U", 8)
    c.drawString(14 * mm, A4[1] - 6 * mm, HDR)
    c.drawRightString(A4[0] - 14 * mm, A4[1] - 6 * mm, "Current to October 2026 · Revision m1 + u1")
    c.setFillColor(colors.grey); c.drawCentredString(A4[0] / 2, 8 * mm, f"Page {doc.page}"); c.restoreState()

def cover(c, doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    c.setFillColor(TEAL); c.rect(0, A4[1] * 0.42, A4[0], 3, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("UB", 30)
    c.drawString(22 * mm, A4[1] - 70 * mm, "AI Engineering"); c.drawString(22 * mm, A4[1] - 84 * mm, "Complete 12-Week Syllabus")
    c.setFont("U", 13); c.setFillColor(colors.HexColor("#9FD8DC"))
    c.drawString(22 * mm, A4[1] - 100 * mm, "From LLM foundations to production-grade agentic systems")
    c.setFillColor(colors.white); c.setFont("U", 12); y = A4[1] * 0.42 - 14 * mm
    for t in [f"Day 1: {D1}", f"Day 84: {D84}", "84 consecutive teaching days · no rest days", "",
              "Current to October 2026 — 2026 Currency Layer (u1) verified 11 Oct 2026",
              "Merged syllabus m1 — 133/133 topics and 53/53 resources preserved verbatim", "",
              "Instructor: Pro AI Principal Architect"]:
        c.drawString(22 * mm, y, t); y -= 7 * mm
    c.setFont("U", 9); c.setFillColor(colors.HexColor("#9FB3C8"))
    c.drawString(22 * mm, 18 * mm, "github.com/irudi2021/ai-engineering-journey"); c.restoreState()

doc = BaseDocTemplate(out, pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=15 * mm, bottomMargin=14 * mm,
                      title=f"AI Engineering — Complete 12-Week Syllabus ({short(D1)} – {short(D84)})",
                      author="Pro AI Principal Architect")
W = A4[0] - 28 * mm
fr = Frame(doc.leftMargin, doc.bottomMargin, W, A4[1] - doc.topMargin - doc.bottomMargin, id="f")
doc.addPageTemplates([PageTemplate("cover", [fr], onPage=cover), PageTemplate("body", [fr], onPage=deco)])
story = [NextPageTemplate("body"), PageBreak()]
story += render(sched.split("## Daily Protocol")[0], W)
story += [PageBreak()]
story += render(master, W, breaks=("0. 2026", "1. Merge", "TRACK 0", "WEEKS 1–4", "WEEKS 5–12",
                                    "WEEK ", "3. Complete", "4. Project"))
story += render("## History" + sched.split("## History")[1], W)
doc.build(story)
print("✓ built", out, "|", HDR)
