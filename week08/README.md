# Week 8 · The End of the Assembly Line

Files fetched by `week08_practical.ipynb` (the student notebook downloads them into `data/`):

- `clean_read.wav`: "We went to the market on Saturday morning and bought some fruit for the week." (3.9 s)
- `fallback_singlish.wav`: "Can lah, we go makan at the kopitiam after this." (3.0 s), for students who do
  not upload a recording of their own voice. It is read by a synthetic American voice, so it tests the
  Singlish words, not a Singapore accent.

Both clips are synthetic (Kokoro-82M neural TTS, voice af_heart), 16 kHz 16-bit mono, generated for this
course; no human recordings and no corpus audio.

The notebook also downloads two speech recognition models from Hugging Face when it runs:
`openai/whisper-small` and `jensenlwt/whisper-small-singlish-122k` (both MIT licence).

- `week08_practical.ipynb`: the Week 8 practical (student version). Open in Google Colab.
