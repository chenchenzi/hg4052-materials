# Week 4 · Thirteen Honest Numbers

Files fetched by `week04_practical.ipynb` (the student notebook downloads them with `wget`):

- `fallback_i.wav`, `fallback_a.wav`, `fallback_u.wav`: clean steady vowels (KlattGrid, 1.6 s each, F0 120 Hz, 16 kHz 16-bit mono) for students who skip recording; formant targets are the Peterson & Barney (1952) male means.
- `vowels_mfcc.csv`: 60 rows, one per vowel token (20 each of /i a u/ with jittered pitch and formants): the mean MFCCs `c1..c13` of each token, for the vowel-cluster plot.
- `fallback_logmel.csv`: one 26-value log-mel frame (natural log) from `fallback_a.wav`; the notebook's fallback for the keep-13 reconstruction plot.

All audio is a SYNTHETIC PLACEHOLDER (Praat KlattGrid), generated for this course; no human
recordings. The CSV tables are computed from synthetic tokens with the notebook's own analysis
settings (sr 16000, n_fft 512, hop 160, n_mels 26, n_mfcc 13, fmax 8000). Lecture demo audio
that is only played in class is not distributed here.

- `week04_practical.ipynb`: the Week 4 practical (student version). Open in Google Colab.
