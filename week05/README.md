# Week 5 · The Same Word, Twice

Files fetched by `week05_practical.ipynb`:

- `fallback_digits.zip`: 200 clips of the spoken digits *zero* to *nine* by four SYNTHETIC voices
  (macOS speech synthesis: Daniel, Karen, Moira, Aman), five speaking rates each (140 to 240 words
  per minute), trimmed and stored in the Free Spoken Digit Dataset's format (8 kHz, 16-bit, mono)
  and naming (`{digit}_{speaker}_{index}.wav`, index 0 to 4). No human recordings. The notebook
  uses this set automatically when the dataset below cannot be cloned, or when `USE_FSDD = False`.

The notebook's primary data is the **Free Spoken Digit Dataset** (Zohar Jakobovski and
contributors, CC BY-SA 4.0), cloned by the notebook itself from
https://github.com/Jakobovski/free-spoken-digit-dataset: 3,000 recordings of the ten digits by six
speakers. It is not redistributed here.

- `week05_practical.ipynb`: the Week 5 practical (student version). Open in Google Colab.
