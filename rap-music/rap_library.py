"""Let's demonstrate the power of implementing
two special methods: __len__ and __getitem__.

Example 1. A section of my rap library as a sequence of albums.
"""

import collections
import csv
from pprint import pprint
from random import choice

LIBRARY_CSV = "data\\rap_albums.csv"
# talk about namedtuples
Album = collections.namedtuple("Album", ['rapper', 'title', 'year'])

class RapLibrary:
    albums = None

    def __init__(self, csv_path):
        with open(LIBRARY_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.encodings = "flac mp3 wma aac wav m4a ogg m3u".split()
            self.albums = [Album(rapper=row['rapper'],
                                 title=row['title'],
                                 year=row['year']) for row in reader]

    def __getitem__(self, index):
        return self.albums[index]

    def __len__(self):
        return len(self.albums)

raplib = RapLibrary(LIBRARY_CSV)





print(raplib[5:-1])


# slicing and indexing

# Exercise 1: implement our own __contains__
# check for presence of object


# Exercise 2: sort by rapper name
# def sort_fn():
#     pass

# for album in sorted(raplib, key=sort_fn):
#     print(album)


"""Special methods are called by the Python interpreter.
Notice that we don't say raplib.__len__() but len(..)
except in special cases (actually more than a few cases)
when you would want to specifically call the magic method,"""
