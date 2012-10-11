#!/usr/bin/env

CHANGE_NAMES = True    # Change to False if you want filenames to remain unchanged.
RAND_RANGE = 999999    # Generate random nos. upto this number


# Make sure values don't appear as keys.
# e.g.
# 'rar': 'zip',
# 'zip': 'rar'
#
# Don't do that.

transformation = {
    'rar': {'to': 'hlp', 'change_name': True},
    'avi': {'to': 'dat', 'change_name': True},
    'wmv': {'to': 'dmp', 'change_name': True},
    'mov': {'to': 'log', 'change_name': True},
    'mpg': {'to': 'prx', 'change_name': True},
    'mp4': {'to': 'm4a', 'change_name': True},
    'jpg': {'to': 'ini', 'change_name': False},
    'jpeg': {'to': 'dll', 'change_name': False},
    'png': {'to': 'xml', 'change_name': False},
    'gif': {'to': 'xkcd', 'change_name': False}
}


# Generate heroku-like random names
# https://gist.github.com/1266756
adjs = [
    "autumn", "hidden", "bitter", "misty", "silent", "empty", "dry", "dark",
    "summer", "icy", "delicate", "quiet", "white", "cool", "spring", "winter",
    "patient", "twilight", "dawn", "crimson", "wispy", "weathered", "blue",
    "billowing", "broken", "cold", "damp", "falling", "frosty", "green",
    "long", "late", "lingering", "bold", "little", "morning", "muddy", "old",
    "red", "rough", "still", "small", "sparkling", "throbbing", "shy",
    "wandering", "withered", "wild", "black", "young", "holy", "solitary",
    "fragrant", "aged", "snowy", "proud", "floral", "restless", "divine",
    "polished", "ancient", "purple", "lively", "nameless"
  ]

nouns = [
    "waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning",
    "snow", "lake", "sunset", "pine", "shadow", "leaf", "dawn", "glitter",
    "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook",
    "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly",
    "feather", "grass", "haze", "mountain", "night", "pond", "darkness",
    "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder",
    "violet", "water", "wildflower", "wave", "water", "resonance", "sun",
    "wood", "dream", "cherry", "tree", "fog", "frost", "voice", "paper",
    "frog", "smoke", "star"
  ]
