#!/usr/bin/env

import os
import os.path
import config
import utils
import pickle


try:
    f = open('temp', 'r+b')
    file_transform = pickle.load(f)
except (KeyError, IOError):
    f = open('temp', 'wb')
    file_transform = {'hidden': False}


if file_transform['hidden'] == False:
    for dirpath, dirnames, filenames in os.walk(".", topdown=False):
        # TODO
        # Rename subdirs

        for filename in filenames:
            # For a file /foo/bar/spam.eggs
            # extension        = 'eggs'
            # filepath         = '/foo/bar/spam.eggs'
            # base             = 'spam.eggs'
            # base_without_ext = 'spam'
            extension = os.path.splitext(filename)[1][1:]
            filepath = os.path.join(dirpath, filename)
            base = os.path.basename(filepath)  # No need to store in var
            base_without_ext = os.path.splitext(base)[0]

            if extension in config.transformation:
                new_name = os.path.join(dirpath, base_without_ext) + '.' + utils.transform(extension)
                if config.transformation[extension]['change_name']:
                    new_name = os.path.join(dirpath, utils.get_random_name()) + '.' + utils.transform(extension)

                # First save data for future unhiding
                file_transform[new_name] = filepath
                os.rename(filepath, new_name)
    file_transform['hidden'] = True
    pickle.dump(file_transform, f, pickle.HIGHEST_PROTOCOL)
    f.close()

else:
    f = open('temp', 'rb')
    file_transform = pickle.load(f)
    for key in file_transform:
        if key != 'hidden':
            os.rename(key, file_transform[key])
    f.close()
    os.remove('./temp')
