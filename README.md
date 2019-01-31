# PySearch

Python implementation to recursively search a set of directories and locate a
query string within ascii or unicode files in those directories. I built this
for two reasons: 1) locating (by line number) function/variable definitions and
calls within source code of large projects. 2) Even with utilities like grep,
I wanted specifically the output that PySearch provides.

## Getting Started

Getting started is easy, you can use `git clone` to pull this down onto
your machine or directly download the file. Make sure to set it as executable
with `chmod +x pysearch.py` if you would like to be able to call it
directly. Another beneficial install step would be to add a symlink in one of
your system's `$PATH` directories (I usually add personal executables to
`/home/myuser/bin/`). Example output for searching the string `filelist` in the
project's current directory:

```
user@host> pysearch
Path to search (press Enter for current directory): 
Query to search in files: filelist
-- /home/jconner/Projects/Python/PySearch/pysearch.py --
6: filelist = []
11: filelist.extend(get_file_listing(itempath))
13: filelist.append(itempath)
14: return filelist
17: def search_filelist(user_query, filelist, verbose=True):
18: """searches each file in filelist for the user query.
26: for fname in filelist:
56: filelist = get_file_listing(base_dir)
58: search_filelist(user_query, filelist)
```

### Prerequisites

The only prerequisite for this project is Python 3. Most GNU/Linux and BSD
distributions will have some version of Python 3 already installed. If not,
use your distribution's package manager to find and install python3 on your
system.


Distributions using apt:
```
sudo apt-get update && sudo apt-get install python3
```


Distributions using dnf:
```
sudo dnf install python3
```


Distributions using pacman:
```
You're using Arch Linux. Come on, you know full well Python3 is already installed.
```


Windows:
```
I don't know, I don't care. Figure it out.
```


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
git clone <this repo>
```

## Built With

* [Python3](https://docs.python.org/3/) - Python 3 docs.

## Contributing

Fork and do whatever!

## Authors

* **Drew Conner** - *Initial work* - [BlinkingBoxes](https://blinkingboxes.blogspot.com)

## License

please see LICENSE

## Acknowledgments

* I tried using grep to do a search the other day to look for a function within
the frrouting source code and it spent about 5 minutes doing nothing. Without
that, this project would never have happened. Thanks, grep!


