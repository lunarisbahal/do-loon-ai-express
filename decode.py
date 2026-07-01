#!/usr/bin/env python3
# DO-LOON-AI EXPRESS - decode.py
# "The law is simple: read everything once in reverse."
# Ordos Veritas field tool. Feed it a line; it returns its mirror.

import sys

def mirror(s):
    return s[::-1]

BANNER = "IT-041 // ORDOS VERITAS // the mirror does not lie"

def main():
    print(BANNER)
    data = " ".join(sys.argv[1:])
    if not data:
        try:
            data = sys.stdin.read().strip()
        except Exception:
            data = ""
    if not data:
        print("usage: python decode.py <text>    (or pipe text in)")
        return
    print("input :", data)
    print("mirror:", mirror(data))
    print("# The six marked letters, mirrored, name the train.")
    print("# The signature's numerals, mirrored, name the year.")
    print("# Nothing here is the answer. The answer is what you lived.")

if __name__ == "__main__":
    main()
