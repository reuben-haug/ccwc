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


def main():
    pass


if __name__ == '__main__':
    main()
