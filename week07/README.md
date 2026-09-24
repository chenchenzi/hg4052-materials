# Week 7 · A Matrix and a Squash

Files fetched by `week07_practical.ipynb` (the student notebook downloads them into `data/`):

- `hillenbrand1995_vowels.csv`: 1,668 vowel tokens from Hillenbrand et al. (1995): 139 speakers from
  Michigan (45 men, 48 women, 27 boys, 19 girls), 12 American English vowels in /hVd/ words (heed, hid,
  hayed, head, had, hod, hawed, hoed, hood, who'd, hud, heard). Columns: `speaker`, `group`, `vowel`
  (IPA), `word`, `duration_ms`, `f0`, `f1`, `f2`, `f3` (Hz, steady-state measurements). Real speech
  measurements, not synthetic.

Also here:

- `week07_practical.ipynb`: the Week 7 practical (student version). Open in Google Colab.

## Source and licence

Hillenbrand, J., Getty, L. A., Clark, M. J. & Wheeler, K. (1995). Acoustic characteristics of American
English vowels. *Journal of the Acoustical Society of America* 97(5), 3099–3111. The data were posted by
Dr Hillenbrand at homepages.wmich.edu/~hillenbr/voweldata.html.

This file is the `h95` data set of the phonTools R package (Barreda, S., phonTools: Tools for phonetic and
acoustic analyses, version 0.2-2.2, CRAN), converted to CSV with IPA vowel labels and the /hVd/ words
added. In phonTools, speaker numbers were made unique and 10 missing F2 and 41 missing F3 values were
imputed. phonTools is distributed under the BSD 2-Clause licence:

    Copyright (c) 2015, Santiago Barreda
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, are permitted
    provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this list of conditions
       and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
       and the following disclaimer in the documentation and/or other materials provided with the
       distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
    IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
    FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
    IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
    THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
