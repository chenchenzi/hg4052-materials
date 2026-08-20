"""Build week02/wordlist_ipa.csv: common English words with IPA transcriptions.

Provenance
- Pronunciations: CMU Pronouncing Dictionary (cmudict, via nltk; BSD-style licence).
- Frequencies: Brown corpus (via nltk), lowercase alphabetic tokens only.
- Selection: the top 8000 Brown word types by count, kept if CMUdict has an entry.
  Single letters are dropped except "a" and "i" (Brown lists letters such as
  "b" and "c" as tokens; they are not words).
- One pronunciation per word: the first CMUdict entry.
- ARPAbet -> IPA with stress digits stripped; unstressed AH0 becomes schwa.

Run with any Python that has nltk installed:
    python build_wordlist.py
"""
import csv
import re
from collections import Counter

import nltk

nltk.download("cmudict", quiet=True)
nltk.download("brown", quiet=True)
from nltk.corpus import brown, cmudict  # noqa: E402

ARPABET_TO_IPA = {
    "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ",
    "EY": "eɪ", "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i",
    "JH": "dʒ", "K": "k", "L": "l", "M": "m", "N": "n", "NG": "ŋ",
    "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "ɹ", "S": "s", "SH": "ʃ",
    "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u", "V": "v", "W": "w",
    "Y": "j", "Z": "z", "ZH": "ʒ",
}

TOP_N = 8000


def arpabet_to_ipa(phones):
    out = []
    for p in phones:
        if p == "AH0":
            out.append("ə")
            continue
        base = re.sub(r"\d", "", p)
        out.append(ARPABET_TO_IPA[base])
    return " ".join(out)


def main():
    counts = Counter(w.lower() for w in brown.words() if w.isalpha())
    top = [w for w, _ in counts.most_common(TOP_N)]
    pron = cmudict.dict()
    rows = []
    for w in top:
        if len(w) == 1 and w not in ("a", "i"):
            continue
        if w in pron:
            rows.append((w, arpabet_to_ipa(pron[w][0]), counts[w]))
    rows.sort(key=lambda r: (-r[2], r[0]))
    with open("wordlist_ipa.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f, lineterminator="\n")
        wr.writerow(["word", "ipa", "freq"])
        wr.writerows(rows)
    print(f"wrote {len(rows)} rows")


if __name__ == "__main__":
    main()
