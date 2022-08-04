from glob import iglob


def load_from_file(files_pattern):
    """read and merge files which matches given file pattern, prepare for parsing and return it.
    """

    # read text
    text = ""
    for path in iglob(files_pattern):
        with open(path, 'r') as f:
            text += f.read().strip()

    return text
