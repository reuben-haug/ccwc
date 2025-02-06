# src/ccwc.py
"""
ccwc.py: A coding challenge copy of the wc command in Unix/Linux.

This script reads the contents of a text file or standard input
and counts the number of lines, words, characters, and bytes.
The file name is passed as an argument to the script.

Usage: python ccwc.py [file_name] [-c] [-l] [-w] [-m]

Arguments:
    file_name: The name of the file to be read.  If no file is provided,
    the script will read from standard input.
    -c: Count the number of bytes in the file.
    -l: Count the number of words in the file.
    -w: Count the number of words in the file.
    -m: Count the number of characters in the file.

Examples:
    python ccwc.py myfile.txt -l
    cat myfile.txt | python ccwc.py -c
"""


# Imports go here
import argparse
import sys


def read_file(file_path):
    """Read the contents of a file at the given path."""
    pass


def count_bytes(file_path):
    """Return the number of bytes in a file."""
    pass


def count_lines(file_path):
    """Return the number of lines in a file."""
    pass


def count_words(file_path):
    """Return the number of words in a file."""
    pass


def count_chars(file_path):
    """Return the number of characters in a file."""
    pass


def main():
    parser = argparse.ArgumentParser(
        description="A coding challenge copy of the wc command in Unix/Linux."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default=sys.stdin,
        type=argparse.FileType("r"),
        help="The file to be processed.",
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
        help="Count the number of characters in the file.  Locale dependant.",
    )
    args = parser.parse_args()

    file_contents = args.file.read()
    # Check if file contents or standard input
    file_name = args.file.name if args.file is not sys.stdin else ""

    count_functions = {
        "bytes": count_bytes,
        "lines": count_lines,
        "words": count_words,
        "characters": count_chars,
    }

    # Default behaviour: Count lines, words, and characters
    if not any([args.bytes, args.lines, args.words, args.characters]):
        line_count = count_lines(file_contents)
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        print(f"{line_count} {word_count} {char_count}")

    if args.bytes:
        byte_count = count_bytes(file_contents)
        print(f"{byte_count} {file_name}")

    if args.lines:
        line_count = count_lines(file_contents)
        print(f"{line_count} {file_name}")

    if args.words:
        word_count = count_words(file_contents)
        print(f"{word_count} {file_name}")

    if args.lines:
        line_count = count_lines(file_contents)
        print(f"{line_count} {file_name}")


if __name__ == "__main__":
    main()
