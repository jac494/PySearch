#!/usr/bin/env python3

import os

def get_file_listing(start_dir):
    filelist = []
    for item in os.scandir(start_dir):
        itempath = os.path.join(start_dir, item.name)
        # print(itempath)
        if item.is_dir():
            filelist.extend(get_file_listing(itempath))
        elif item.is_file():
            filelist.append(itempath)
    return filelist


def search_filelist(user_query, filelist, verbose=True):
    """searches each file in filelist for the user query.
    
    when verbose is True (default), will print results as they are found.
    
    returns dictionary of file names and line numbers/line text tuples
    of lines containing the query text.
    """
    found_d = dict()
    for fname in filelist:
        try:
            with open(fname) as fp:
                lines = []
                for ln, line in enumerate(fp.readlines()):
                    if user_query in line:
                        line = line.strip()
                        # adding 1 to line number because
                        # of zero-based indexing on lists but one-based
                        # numbering on text editors
                        ln += 1
                        lines.append((ln, line))
                if len(lines) > 0:
                    if verbose:
                        print(f'-- {fname} --')
                        for line in lines:
                            print(f'{line[0]}: {line[1]}')
                    found_d[fname] = lines
        except Exception as e:
            continue
    return found_d


def main(base_dir=None, user_query=None):
    if not user_query:
        return
    
    if not base_dir:
        base_dir = os.getcwd()

    filelist = get_file_listing(base_dir)

    search_filelist(user_query, filelist)


if __name__ == "__main__":
    # TODO: implement argparse for full command-line support.
    search_path = input('Path to search (press Enter for current directory): ')
    search_path = search_path.strip()
    query_string = input('Query to search in files: ')
    query_string = query_string.strip()
    if search_path == '':
        main(base_dir=None, user_query=query_string)
    else:
        main(base_dir=search_path, user_query=query_string)

