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
        pass


raplib = RapLibrary(LIBRARY_CSV)








# slicing and indexing

# Exercise 1: implement our own __contains__
# check for presence of object


# Exercise 2: sort by rapper name
# def sort_fn():
#     pass

# for album in sorted(raplib, key=sort_fn):
#     print(album)


# """Special methods are called by the Python interpreter.
# Notice that we don't say raplib.__len__() but len(..)
# except in special cases (actually more than a few cases)
# when you would want to specifically call the magic method,
