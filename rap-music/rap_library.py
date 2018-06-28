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
