GRE2Anki
========

Chooses a GRE word from a list of nearly 4000 words and outputs its
description. You can then copy that in Anki or other SRS software.
Every time you run the script, the random word will be added to
`archive.txt`, which will stop the word from appearing again. In case
you want to start over, just delete `archive.txt`.

Requirements
------------

* `python3`

Instruction
-----------

```
$ python gre2anki.py -f GRE_WORDS.txt
```

Acknowledgements
----------------

The list of words has been exported from
[this deck](https://ankiweb.net/shared/info/3676380352).
