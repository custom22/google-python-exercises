#!/usr/bin/python
import re
import sys


# def return_year(filename):
#     inputfile = open(filename, 'rU')
#     for line in inputfile:
#         match_year = re.search(r'(Popularity in )(\d\d\d\d)', line)
#         if match_year:
#             return match_year.group(2)
#             inputfile.close()
#             break


# def return_rank_name():
#   str = '<tr align="right"><td>123</td><td>Michael</td><td>Jessica</td>'
#   match_rank_name = re.search(r'<tr align="right"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', str)
#   if match_rank_name:
#     print match_rank_name.group(1)
#     print match_rank_name.group(2)
#     print match_rank_name.group(3)

def build_rank_name(filename):
    dict_rank_name = {}
    inputfile = open(filename, 'rU')
    for line in inputfile:
        match_rank_name = re.search(r'<tr align="right"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', line)
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
    filename = sys.argv[1]
    print filename
    # int_year = return_year(filename)
    # print int_year
    dict = build_rank_name(filename)
    for key in sorted(dict): print "%s %s" % (key,dict[key])


if __name__ == '__main__':
    main()
