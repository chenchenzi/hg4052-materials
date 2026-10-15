# Week 9 · The Audit

Files fetched by `week09_practical.ipynb` (the student notebook downloads them into `data/`):

- `class_results.csv`: one row per clip: `file`, `speaker` (sg01..., us01...), `accent`, `gender`, `reference`,
  `hyp_A` (openai/whisper-small) and `hyp_B` (jensenlwt/whisper-small-singlish-122k). The transcripts were made
  in advance with `language="english"`.
- `class_clips.zip`: the 38 clips as MP3 (`clips/`): 19 by speakers who gave their accent as Singaporean English
  (12 speakers) and 19 by speakers who gave it as United States English (19 speakers), reading sentences.
- `align_clip.wav` and `align_clip.TextGrid`: one of the Singapore English clips ("Haggling or bargaining is the
  most common means of sale."), aligned with the Montreal Forced Aligner 3.3.3 (english_us_mfa dictionary,
  english_mfa acoustic model).
- `week09_practical.ipynb`: the Week 9 practical (student version). Open in Google Colab.

## Source and licence

The audio and reference sentences are from Mozilla Common Voice 17.0, English, test and dev splits, released under
CC0 1.0 (public domain dedication); accents and gender are as the contributors reported them. Downloaded from the
Hugging Face mirror `fsicoli/common_voice_17_0`. Common Voice asks users not to try to identify the speakers.
The original file names (`common_voice_en_...`) are kept; contributor ids are replaced by sg01 and us01.
