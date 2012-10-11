hide-stash
==========

# hide_stash
Everyone has some stuff they don't want others to see or access. Unfortunately I don't have a Personal Computer, and I had some stuff I wanted to hide. I tried using some softwares but they just didn't seem right. So I made a small script that uses the oldest trick in the book - **Renaming Files**


## Disclaimer
I am not a very experienced programmer and have very little experience. So you might think this script is `Shitty`.
![This is how I feel](http://i.imgur.com/QffW8.jpg)


## Limitations
* The .py files have to be at the to of the diretory you want to hide.
* Directory names remain unhanged.
* Some filenames are reserved. (`hidden`, `temp` etc.)
* No Unit tests. (Read disclaimer)


## Features
* Rename files with a different extension.
* Rollback to original filenames
* Flexible configuration
* Can create backups in case things go wrong. (Not automatially)


## Usage
#### Hide files
Place the `.py` files in the diretory you want to hide. So if you put the files in `/foo/bar/`, it will hide all files inside of `bar`.

Run `python rename.py`

A file called `temp` will be created.

#### Unhide files
Run `python rename.py`

#### Backup filenames and structure
Run `python backup.py`

A file named `backup_pickle` will be created. Read the internals of `backup.py` for more info.

