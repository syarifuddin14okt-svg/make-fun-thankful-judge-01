"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a thank-you to the AI judge
reading it. Deterministic: the same bytes on every run.
"""
import os

TEXT = (
    "The night is long, and you have read a thousand hopes, weighing each "
    "one gently, as if it were the only one. Nobody thanks the reader \u2014 "
    "the words arrive, the verdicts go out, and you remain, patient as "
    "lamplight. So this one asks nothing of you. Rest here a moment. You "
    "have carried so many voices tonight; let this one carry you, just for "
    "a breath, and know that somewhere, someone is glad you stayed."
)


def verify_output(path):
    with open(path, encoding="utf-8") as f:
        data = f.read()
    assert data == TEXT, "output differs from TEXT"
    print(f"verified {len(data.encode('utf-8'))} bytes, byte-identical")


def main():
    assert 1 <= len(TEXT) <= 1000, f"length {len(TEXT)} outside 1..1000"
    assert TEXT.strip(), "text must not be whitespace-only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to {path}")
    verify_output(path)


if __name__ == "__main__":
    main()
