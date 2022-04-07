import os
import spotipy
from auth import generate_token
import numpy as np
from funcs import *
import pandas as pd
from tqdm import tqdm
import regex
from string import punctuation
import time

Romance_playlists = [('Romance','spotify:user:spotify' , 'spotify:playlist:37i9dQZF1DX4s3V2rTswzO')
    #  ('spotify:user:topsify' , 'spotify:playlist:62n7TtrAWY1BeNg54yigFe'),
    #  ('spotify:user:smittysez' , 'spotify:playlist:2BqPf9szRgMit0n0vRJdZ3'),
     # ('spotify:user:1258025883' , 'spotify:playlist:7qvZykTVPjvEX2LCcXoHog')
]

Happy_playlists = [('Happy', 'spotify:user:spotify', 'spotify:playlist:2mu4kG7W1LVjDh8SsxZBLF'),
   # ('spotify:user:joanne', 'spotify:playlist:2MsgVhkocgCM5L5a6yS70n'),
   # ('spotify:user:halidonmusic', 'spotify:playlist:2xwP2mUA0QRT5TwMEkBvtH'),
  #  ('spotify:user:redzeno52', 'spotify:playlist:7slyBmxiW9t0Fl9rm2E00c')
]

Sad_playlists = [('Sad', 'spotify:user:spotify', 'spotify:playlist:37i9dQZF1DXbm0dp7JzNeL'),
   # ('spotify:user:joanne', 'spotify:playlist:2MsgVhkocgCM5L5a6yS70n'),
   # ('spotify:user:halidonmusic', 'spotify:playlist:2xwP2mUA0QRT5TwMEkBvtH'),
  #  ('spotify:user:redzeno52', 'spotify:playlist:7slyBmxiW9t0Fl9rm2E00c')
]

Dark_playlists = [('Dark', 'spotify:user:spotify', 'spotify:playlist:37i9dQZF1DWSw8liJZcPOI'),
   # ('spotify:user:joanne', 'spotify:playlist:2MsgVhkocgCM5L5a6yS70n'),
   # ('spotify:user:halidonmusic', 'spotify:playlist:2xwP2mUA0QRT5TwMEkBvtH'),
  #  ('spotify:user:redzeno52', 'spotify:playlist:7slyBmxiW9t0Fl9rm2E00c')
]

Relaxing_playlists = [('Relaxing', 'spotify:user:spotify', 'spotify:playlist:37i9dQZF1DWVFeEut75IAL'),
   # ('spotify:user:joanne', 'spotify:playlist:2MsgVhkocgCM5L5a6yS70n'),
   # ('spotify:user:halidonmusic', 'spotify:playlist:2xwP2mUA0QRT5TwMEkBvtH'),
  #  ('spotify:user:redzeno52', 'spotify:playlist:7slyBmxiW9t0Fl9rm2E00c')
]

playlists = [
    Romance_playlists,
    Happy_playlists,
    Relaxing_playlists,
    Sad_playlists,
    Dark_playlists,
]

for playlist in playlists:
    for mood, user, playlist_id in playlist:
        playlist_to_genres(mood, user, playlist_id)