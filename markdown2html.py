#!/usr/bin/python3
import sys
from os import path

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

if not path.exists(sys.argv[1]):
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    exit(1)

exit(0)
