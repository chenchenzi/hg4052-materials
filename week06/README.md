# Week 6 · From Distance to Probability

Files fetched by `week06_practical.ipynb` (the student notebook downloads them into `data/`):

- `state_loglik_no_go.csv`: for ten clips, one row per frame: the log-likelihood of that frame under
  three states, /n/, /g/ and /oʊ/ (columns `ll_n`, `ll_g`, `ll_ou`). SYNTHETIC: drawn to sit at about
  −1.5 for a frame that fits its state and −5 to −6 otherwise; two clips have deliberately ambiguous
  onsets. No recordings were measured.
- `clips_truth.csv`: each clip's word and the number of onset frames (for checking, not for decoding).
- `bigram_counts.csv`: two bigram-count tables over one 18-word vocabulary, `news` (newswire-flavoured,
  no "makan", no "lah") and `nsc` (Singapore-conversation-flavoured). The counts are invented for
  teaching; they are not National Speech Corpus counts.
- `candidates.csv`: five candidate transcripts of one utterance with synthetic acoustic scores (log10).
- `heldout_lines.txt`: four Singlish lines the tables never saw, for the perplexity stretch.

Also here:

- `ice_cream_trellis.pdf`: the printed sheet for the practical's paper stage (one per pair).
- `week06_practical.ipynb`: the Week 6 practical (student version). Open in Google Colab.

Everything is synthetic and deterministic (generator: `demo_audio/week06/make_week06_assets.py` in the
course's private folder, seed 6). No human recordings, no real corpus data.
