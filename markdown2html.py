#!/usr/bin/python3
"""A script that converts Markdown to HTML"""

import sys
def func(markdown_file, html_file):
    """Converts markdown to html"""
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_text = md_file.read()
            html_content = markdown.markdown(markdown_text)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    if not markdown:
        