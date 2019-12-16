# [G.729А](https://en.wikipedia.org/wiki/G.729#G.729_Annex_A) for python 3

Encodes PCM 16-bit 80 sample chunks to 10 bytes of G.729А and back.

Good for speech.

Fixed compression ratio 16:1 (16kbps PCM -> 1kbps G.729A).

## Usage

- Linux x64, Windows x64

  you can use precompiled libg729a.so (linux) or libg729a.dll (windows)

- Other

  ```bash
  cd src
  make
  cp libg729a.so ../python
  ```

See `python/example.py` for usage from python.

In the end you only need two files: 

- libg729a.so (linux) or libg729a.dll (windows) - g729a library file
- g729a.py - python wrapper

## License

Copyright (c) 2015, Russell

Copyright (c) 2019, github.com/AlexIII

[BSD 2-Clause License](LICENSE)

## Notice

**Most of source codes are under the following ITU notice:**

> ITU-T G.729 Software Package Release 2 (November 2006)
> 
> ITU-T G.729A Speech Coder    ANSI-C Source Code
> Version 1.1    Last modified: September 1996
> 
> Copyright (c) 1996,
> AT&T, France Telecom, NTT, Universite de Sherbrooke
> All rights reserved.
