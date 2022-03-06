import os
import urllib
import librosa
import numpy as np
from funcs import *
import pandas as pd
import regex
from string import punctuation
from python_speech_features import mfcc, logfbank

song_df = pd.read_csv('./data/song_genres.csv')

song_df.info()