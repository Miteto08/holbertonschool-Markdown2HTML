#!/usr/bin/python3
''' Markdown to HTML '''
import sys
from os import path


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html' ,file=sys.stderr)
        exit(1)
    '''Markdown file doesn’t exist'''
    if not path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    '''Headings Markdown'''
    with open(sys.argv[1], 'r') as read_file:
        line_list = []
        for lines in read_file.readlines():
            number_of_hashes = 0
            for line in lines:
                for car in range(len(line)):
                    if line[car] == '#':
                        number_of_hashes += 1
            lines = lines.rstrip('\r\n')
            if number_of_hashes != 0:
                line_list.append("<h{}>{}</h{}>".format(number_of_hashes, lines.replace('#',''), number_of_hashes))
        with open(sys.argv[2], 'a') as write_file:
            for line in line_list:
                write_file.write('{}\n'.format(line))
