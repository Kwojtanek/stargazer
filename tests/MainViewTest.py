__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import urlparse
import string
url = 'https://docs.python.org/2/library/urlparse.html'
print string.split(urlparse.urlsplit(url).path,'/')