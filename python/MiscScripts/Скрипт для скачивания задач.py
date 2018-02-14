#!/usr/bin/env python

#import sys

from urllib.request import urlopen
import re

resp = urlopen('http://habrahabr.ru')
page = resp.read()
st = str(page)
html_tags = re.compile('<.*?>')
for i in html_tags.findall(st):
	st = st.replace(i,'')
#page = page[page.find('Условие'):50]
#s = st.find('Условие')

print(page.decode('utf-8'))
input()