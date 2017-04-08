#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def return_year(filename):
    inputfile = open(filename, 'rU')
    for line in inputfile:
        match_year = re.search(r'Popularity\sin\s(\d\d\d\d)', line)
        if match_year:
            return match_year.group(1)
            inputfile.close()
            #print match_year.group(1)
            break


def build_rank_name(filename):
    dict_rank_name = {}
    inputfile = open(filename, 'rU')
    for line in inputfile:
        match_rank_name = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
        if match_rank_name:
          # evaluate boys name
          if match_rank_name.group(2) in dict_rank_name and dict_rank_name[match_rank_name.group(2)] > match_rank_name.group(1):
            dict_rank_name[match_rank_name.group(2)] = match_rank_name.group(1)
          else:
            dict_rank_name[match_rank_name.group(2)] = match_rank_name.group(1)
          # evaluate girls name
          if match_rank_name.group(3) in dict_rank_name and dict_rank_name[match_rank_name.group(3)] > match_rank_name.group(1):
            dict_rank_name[match_rank_name.group(3)] = match_rank_name.group(1)
          else:
            dict_rank_name[match_rank_name.group(3)] = match_rank_name.group(1)
    inputfile.close()
    return dict_rank_name


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    list = []
    # appends year to list
    list.append(return_year(filename))
    dict_rank_name = build_rank_name(filename)
    # sorts dictionary and appends entries to list
    for key in sorted(dict_rank_name): list.append("%s %s" % (key, dict_rank_name[key]))
    return list


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    
    if summary:
        for html_file in args:
            text = '\n' .join(extract_names(html_file)) + '\n'
            output = open(html_file + '.summary', 'w')
            output.write(text + '\n')
            output.close()
    else:
        for html_file in args: print extract_names(html_file)


if __name__ == '__main__':
    main()
