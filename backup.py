#!/usr/bin/env

import os
from utils import md5_for_file
import pickle


backup_dict = {}

for dirpath, dirnames, filenames in os.walk(".", topdown=False):
    for filename in filenames:
        extension = os.path.splitext(filename)[1][1:]
        filepath = os.path.join(dirpath, filename)

        with open(filepath, 'rb') as f:
            md5 = md5_for_file(f)
            backup_dict[filepath] = md5

with open('backup_pickle', 'wb') as f:
    pickle.dump(backup_dict, f)
