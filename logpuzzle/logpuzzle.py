#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_sort_key(url):
  """Used to order the urls in increasing order by 2nd word if present."""
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # gets host name from file name
  underbar = filename.index('_')
  host = filename[underbar + 1:]
  # creates list, placing host + url in if criteria is met
  list_url = []
  file = open(filename, 'rU')
  for line in file:
    strGET = re.search(r'GET (\S*)[\s]', line)
    # criteria 1) strGET returns results 2) puzzle found in URL 3) does not exists in list_url
    if strGET and 'puzzle' in strGET.group(1) and not 'http://' + host + strGET.group(1) in list_url:
      list_url.append('http://' + host + strGET.group(1)) 
  file.close()
  # returns sorted results
  # 1st sort is for key sort
  #return sorted(list_url, key=url_sort_key)
  return sorted(list_url)
      
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  i = 0
  if not os.path.exists(dest_dir): os.mkdir(dest_dir)
  finput = open('picture.html', 'w')
  finput.write('<verbatim>\n<html>\n<body>\n')
  for url in img_urls:
    i = i + 1
    print 'Downloading %s as img%d.jpg' % (url, i)
    urllib.urlretrieve(url,dest_dir + '/img%d.jpg' % i)
    finput.write('<img src="%s\img%d.jpg">' % (dest_dir, i))
  finput.write('\n</html>\n</body>')
  finput.close()


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
