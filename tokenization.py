import nltk
from nltk.tokenize import word_tokenize

def ensure_tokenizers():
    for pkg in ("punkt", "punkt_tab"):
        try:
            nltk.data.find(f"tokenizers/{pkg}")
        except LookupError:
            nltk.download(pkg)

def normalize_quotes(s: str) -> str:
    return (s.replace("’", "'")
             .replace("‘", "'")
             .replace("“", '"')
             .replace("”", '"'))

def diff_by_index(a, b, limit=40):
    diffs = []
    m = max(len(a), len(b))
    for i in range(m):
        ai = a[i] if i < len(a) else "<none>"
        bi = b[i] if i < len(b) else "<none>"
        if ai != bi:
            diffs.append((i, ai, bi))
            if len(diffs) >= limit:
                break
    return diffs

ensure_tokenizers()

text = (
    "I can’t join the workshop today, but I’ll review the materials later. "
    "NLP seems confusing at first, yet it becomes very useful in real-world applications. "
    "Many people don’t realize how punctuation and contractions influence tokenization."
)

# Naive space-based tokenization
naive_tokens = text.split()

# Manual tokenization
manual_tokens = [
    'I', 'can', "n't", 'join', 'the', 'workshop', 'today', ',', 'but', 'I', "'ll",
    'review', 'the', 'materials', 'later', '.',
    'NLP', 'seems', 'confusing', 'at', 'first', ',', 'yet', 'it', 'becomes', 'very',
    'useful', 'in', 'real-world', 'applications', '.',
    'Many', 'people', 'do', "n't", 'realize', 'how', 'punctuation', 'and',
    'contractions', 'influence', 'tokenization', '.'
]

# NLTK tokenization
tool_tokens = word_tokenize(normalize_quotes(text))

print("Naive (text.split):")
print(naive_tokens)

print("\nManual tokens:")
print(manual_tokens)

print("\nNLTK word_tokenize tokens:")
print(tool_tokens)

diffs = diff_by_index(manual_tokens, tool_tokens)

print("\nDifferences (manual vs NLTK):")
if not diffs:
    print("No differences found.")
else:
    for i, m, t in diffs:
        print(f"index {i}: manual={m!r}  nltk={t!r}")

print("\nWhy differences happen:")
print('NLTK follows Penn Treebank conventions (e.g., "can\'t" → "ca" + "n\'t").')
