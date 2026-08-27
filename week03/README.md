# Week 3 · Audio for the acoustics practical

Files used by the Week 3 practical and slides (the notebook fetches what it needs with
`wget`). All clips are 16 kHz, 16-bit, mono WAV.

| file | what it is |
|---|---|
| `week03_demo.wav` | a steady 2 s synthetic [ɑː] vowel (Praat KlattGrid: F0 120 Hz, F1-F4 = 730/1090/2440/3500 Hz) for the narrowband vs wideband spectrogram demo |
| `bitdepth_16.wav`, `bitdepth_8.wav`, `bitdepth_4.wav`, `bitdepth_3.wav` | the same sentence quantised to 16/8/4/3 bits (mid-tread uniform quantisation, then stored as 16-bit PCM so it plays anywhere) |
| `hvd_heed.wav` ... `hvd_whod.wav` | fallback recordings of the hVd word list (heed, hid, head, had, hod, hawed, who'd) for anyone without a mic |
| `sentence_sheep.wav` | fallback recording of "She sees Sue's sheep." |

Provenance and licence: all clips are synthetic teaching materials made for this course.
No human voice was recorded. `week03_demo.wav` was synthesised with Praat's KlattGrid;
the speech clips were synthesised with Kokoro-82M (Apache-2.0), voice `af_heart`.
Because the hVd clips are synthetic, formant values you measure on them are for
practising the workflow; they are not ground truth for any human speaker.

Course materials developed by Chenzi Xu in collaboration with Claude (Anthropic).
All content has been reviewed by the instructor, who is responsible for it.

## Mystery clips

`mystery1.wav`, `mystery2.wav`, `mystery3.wav`, `contrast_word.wav`: short audio for an in-class
spectrogram-reading activity. Deliberately unlabelled; all synthetic voices (Kokoro-82M), 16 kHz mono.
