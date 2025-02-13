**Core Functionality**
 * Command line tool similar to Unix `wc` utility
 * Python-based implementation
 
**Counting Features**
    * Word count
    * Line count
    * Character count
    * Byte count
**Output Format**
    * Counts are displayed in the following order:
        * Word count
        * Line count
        * Character count
        * Byte count
    * The file name is displayed at the end of the output
**Error Handling**
    * Proper error message is displayed when the file is not found

Command line tool similar to Unix `wc` utility (Python implementation).
Returns the word, line, character, and byte count for a given .txt file.
This tool has the following flags implemented:

- -c: byte count
- -l: line count
- -w: word count

- -m: character count

The default behavior without flags is to return all counts.