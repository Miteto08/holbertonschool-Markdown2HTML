#!/usr/bin/python3
import sys
import os

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

markdown_file = "README.md"
html_file = "README.html"

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    exit(1)

exit(0)
