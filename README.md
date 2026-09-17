# HG4052 · Speech Synthesis & Recognition
### Course materials

Data and notebooks for HG4052 (NTU Singapore). Each week's practical notebook fetches
its data from this repository with a single `wget`.

- `week01/vowels.csv`: 40 vowel tokens (label, F1, F2 in Hz), built around the
  Peterson & Barney (1952) male-speaker means.
- `week01/week01_practical.ipynb`: the Week 1 practical (student version).
- `week02/wordlist_ipa.csv`: 7,909 common English words with IPA transcriptions (CMU
  Pronouncing Dictionary via NLTK) and Brown-corpus frequencies; see `week02/README.md`.
- `week02/week02_practical.ipynb`: the Week 2 practical (student version).
- `week03/week03_demo.wav` and three fallback recordings (a sentence and two hVd words),
  all synthetic voices made for this course; see `week03/README.md`.
- `week03/week03_practical.ipynb`: the Week 3 practical (student version).
- `week04/fallback_i.wav`, `fallback_a.wav`, `fallback_u.wav` (three fallback vowels) and
  two feature tables (`vowels_mfcc.csv`, `fallback_logmel.csv`), all built from synthetic
  voices made for this course; see `week04/README.md`.
- `week04/week04_practical.ipynb`: the Week 4 practical (student version).
- `week05/fallback_digits.zip`: 200 spoken-digit clips by four synthetic voices, in the Free
  Spoken Digit Dataset's format; the notebook's offline fallback. See `week05/README.md`.
- `week05/week05_practical.ipynb`: the Week 5 practical (student version).
- `week06/state_loglik_no_go.csv`, `week06/clips_truth.csv`, `week06/bigram_counts.csv`,
  `week06/candidates.csv`, `week06/heldout_lines.txt`: the Week 6 practical's data, all synthetic
  (per-frame state scores for ten "no"/"go" clips, two invented bigram tables, five candidate
  transcripts). See `week06/README.md`.
- `week06/ice_cream_trellis.pdf`: the printed sheet for the Week 6 paper stage.
- `week06/week06_practical.ipynb`: the Week 6 practical (student version).

Instructor: Chenzi Xu (chenzi.xu@ntu.edu.sg)

Course materials developed by Chenzi Xu in collaboration with Claude (Anthropic).
All content has been reviewed by the instructor, who is responsible for it.
