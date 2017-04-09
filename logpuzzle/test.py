'''import re

str = '10.1.40.113 - - [06/Aug/2007:00:13:48 -0700] "GET /edu/languages/google-python-class/images/puzzle/p-biai-bacj.jpg HTTP/1.0" 200 402 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"'
check = re.search(r'GET (\S*)[\s]', str)
print check.group()
if check and 'puzzle' in check.group(1): print check.group(1) '''

filename = 'place_code.google.com'
underbar = filename.index('_')
print underbar
host = filename[underbar + 1:]
print host