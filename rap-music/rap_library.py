"""Let's demonstrate the power of implementing
two special methods: __len__ and __getitem__.

Example 1. A section of my rap library as a sequence of albums.
"""

import collections
import csv
from pprint import pprint
from random import choice

Album = collections.namedtuple("Album", ['rapper', 'title', 'year'])

class RapLibrary:
    albums = None

    def __init__(self, csv_path):
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # self.encodings
            self.albums = [Album(rapper=row['rapper'],
                                 title=row['title'],
                                 year=row['year']) for row in reader]

# about namedtuples
# RapLibrary("data/rap_album.csv")
