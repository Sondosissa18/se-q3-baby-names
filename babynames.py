#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__author__ = "sondos with help from joseph , piero and gabby "

"""
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    names_dict = {}
    with open(filename, 'r') as f:
        lines = f.read()
        # print(lines)
        pattern = re.search(r'Popularity\sin\s(\d\d\d\d)', lines)
        # print(pattern)
        if not pattern:
            print("No year found")
            return None
        year = pattern.group(1)
        # print(year)
        names.append(year)
        names_list = re.findall(
            r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)', lines)
        for r, m, f in names_list:
            if m not in names_dict:
                names_dict[m] = r
            if f not in names_dict:
                names_dict[f] = r
        for n in sorted(names_dict):
            names.append(f"{n} {names_dict[n]}")
        return names


extract_names("baby1992.html")


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    file_list = ns.files
    # option flag
    create_summary = ns.summaryfile
    for file in file_list:
        result = extract_names(file)
        text = '\n'.join(result)
        if not create_summary:
            print(text)
        else:
            with open(file + ".summary", "w") as f:
                f.write(text)


if __name__ == '__main__':
    main(sys.argv[1:])
