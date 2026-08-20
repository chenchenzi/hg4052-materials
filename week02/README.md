# Week 2 · Probability, bigrams, perplexity

Files used by `week02_practical.ipynb` (the notebook fetches the CSV with one `wget`).

## wordlist_ipa.csv

7,909 common English words with a phonemic transcription and a frequency count.
One row per word, sorted by frequency, highest first.

| column | meaning |
|---|---|
| `word` | lowercase spelling, alphabetic characters only |
| `ipa` | phones separated by single spaces, IPA, no stress marks (e.g. `s t ɹ ɛ ŋ k θ`) |
| `freq` | token count of the word in the Brown corpus |

Provenance:
- Pronunciations: the CMU Pronouncing Dictionary (cmudict), read through NLTK
  (`nltk.download('cmudict')`). cmudict is distributed under a BSD-style licence
  (Copyright Carnegie Mellon University). One pronunciation per word: the first
  cmudict entry. ARPAbet was mapped to IPA with stress digits removed; unstressed
  `AH0` became `ə`, stressed `AH` became `ʌ`. The phone inventory has 40 symbols
  (39 cmudict phones plus schwa).
- Frequencies and word selection: the Brown corpus, read through NLTK
  (`nltk.download('brown')`). Tokens were lowercased and only alphabetic tokens were
  counted. The top 8,000 word types by count were kept if cmudict has an entry for
  them; single letters other than "a" and "i" were dropped. 7,909 words survive.
- `build_wordlist.py` regenerates the file (needs a Python with nltk and internet
  access for the two downloads).

Notes for users of the file: transcriptions are General American (cmudict), so
"strength" is `s t ɹ ɛ ŋ k θ` (cmudict's first entry has the epenthetic k), "the" is
`ð ə`, "of" is `ʌ v`. Word-internal phone pairs are counted when the notebook builds
bigrams, so clusters that are impossible word-initially (tl, as in "atlas") are rare
rather than absent.

## week02_practical.ipynb

The Week 2 practical (student version). Letter counts on Jane Austen's *Emma*
(NLTK's bundled Gutenberg corpus), letter and phone bigram heatmaps, a pseudo-word
babbler, and perplexity on held-out text.
