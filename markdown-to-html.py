#!/usr/bin/env python3


import markdown
import sys

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:
		content = f.read()

		html_content = markdown.markdown(content)
		print(html_content)
