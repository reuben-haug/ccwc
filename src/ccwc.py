# src/ccwc.py
"""
ccwc.py: A coding challenge copy of the wc command in Unix/Linux.

This script reads the contents of a text file or standard input
and counts the number of bytes, lines, words, and characters.
The file name is passed as an argument to the script.

Usage: python src/ccwc.py [-c] [-l] [-w] [-m] [file_name]

Arguments:
    file_name: The name of the file to be read.  If no file is provided,
    the script will read from standard input.
    -c: Count the number of bytes in the file.
    -l: Count the number of lines in the file.
    -w: Count the number of words in the file.
    -m: Count the number of characters in the file.

Examples:
    python src/ccwc.py myfile.txt -l
    cat myfile.txt | python ccwc.py -c
"""


# Imports go here
import argparse
import sys


def count_bytes(content):
    """Return the number of bytes in a file."""
    return len(content.encode())


def count_lines(content):
    """Return the number of lines in a file."""
    return content.count("\n")


def count_words(content):
    """Return the number of words in a file."""
    words = content.split()
    return len(words)


def count_chars(content):
    """Return the number of characters in a file."""
    return len(content)


def main():
    parser = argparse.ArgumentParser(
        description="A coding challenge copy of the wc command in Unix/Linux."
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=str,
        default="-",
        help="The file(s) to be processed."
    )
    parser.add_argument(
        "-c",
        "--bytes",
        action="store_true",
        help="Count the number of bytes in the file.",
    )
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="Count the number of lines in the file.",
    )
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="Count the number of words in the file.",
    )
    parser.add_argument(
        "-m",
        "--characters",
        action="store_true",
        help="Count the number of characters in the file.",
    )

    args = parser.parse_args()

    if not sys.stdin.isatty():
        file_contents = sys.stdin.read()
        file_name = ""
    else:
        try:
            # Read file in binary mode 
            if args.bytes:
                with open(args.file, 'rb') as file:
                    file_contents = len(file.read())
                    print(f"{file_contents} {args.file}")
                    sys.exit(0)
            with open(args.file, 'r', encoding='utf-8') as file:
                file_contents = file.read()
                file_name = args.file
        except FileNotFoundError:
            print(f"File not found: {args.file}")
            sys.exit(1)

    count_functions = {
        "bytes": count_bytes,
        "lines": count_lines,
        "words": count_words,
        "characters": count_chars,
    }

    # Default behaviour: Count lines, words, and characters
    if not any([args.bytes, args.lines, args.words, args.characters]):
        results = [
            count_functions["lines"](file_contents),
            count_functions["words"](file_contents),
            count_functions["characters"](file_contents)
        ]
        print(f"{' '.join(map(str, results))} {file_name}")
    else:
        results = []
        flag_map = {
            args.bytes: "bytes",
            args.lines: "lines",
            args.words: "words",
            args.characters: "characters"
        }
        for flag, func_name in flag_map.items():
            if flag:
                results.append(count_functions[func_name](file_contents))
        print(f"{' '.join(str(x) for x in results)} {file_name}")


if __name__ == "__main__":
    main()
