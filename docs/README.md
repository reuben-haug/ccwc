# coding_challenge_word_count

## Table of Contents

1. [Overview](#overview)
2. [Examples](#examples)

## Overview

Returns the word, line, character, and byte count for a given .txt file.
This tool has the following flags implemented:
- -c: byte count
- -l: line count
- -w: word count
- -m: character count

The default behavior without flags is to return all counts.

todo: Support reading from standard input when no filename is specified.

todo: Support reading from multiple files.

todo: Support multiple flags.

## Examples

```bash
>ccwc -c test.txt
    342190 test.txt
```
