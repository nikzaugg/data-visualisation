#! /usr/bin/env python
# retrieve_vis04_data.py

import formatter
import htmllib
import os
import re
import string
import urllib


def _attrs2dict(attrs):
    """Take an (attribute, value) list and make a dict"""
    dict = {}
    for (a,v) in attrs:
        dict[a] = v
    return dict

class FileList(htmllib.HTMLParser):
    """Logic to retrieve the first page which lists the files, then return the files' URLs for retrieval"""
    base_url = 'http://www.vets.ucar.edu/vg/isabeldata/'
        
    def __init__(self, save_dir, match_string='*', debug=False):
        htmllib.HTMLParser.__init__(self, formatter.NullFormatter())
        self.match = re.compile(match_string)
        self.save_dir = save_dir
        self.debug = debug

    def do_it(self):
        u = urllib.urlopen(self.base_url)
        self.feed(u.read())        
        
    def start_a(self, attrs):
        """We're looking for links to .gz files"""
        d = _attrs2dict(attrs)
        link = d.get('href', ' ')
        if len(link) >= 3 and link[-3:] == '.gz':
            m = self.match.search(link)
            if m:
                #Found a matching file.
                #Get the file name for saving
                fn = os.path.split(link)[1]
                print 'getting ' + link + ' to ' + self.save_dir
                if not self.debug:
                    try:
                        urllib.urlretrieve(self.base_url + link, os.path.join(self.save_dir, fn))
                    except Exception, e:
                        print '-- failure:  ' + str(e)

# retrive data
import sys

# no debugging desired
debug = False

# path to store the data (needs to exist)
path = 'data'

# matching string pattern
# temperatures: 'TCf*'
# surface tolology: 'HGT*'
# more variables in the section 'Variable Descriptions'
# http://www.vets.ucar.edu/vg/isabeldata/readme.html
match = 'HGT*'

# laod data
f = FileList(path, match, debug)
f.do_it()
