"""
The module contains a function accessing the files in a User provided folder
and returning the list of file names

"""


from pathlib import Path


def get_file_names(folder):
    dir_path = Path(folder)
# get all pdf files in directory
    pdfFileNames = []
    for file in dir_path.rglob('*.pdf'):
        pdfFileNames.append(file)

    return pdfFileNames
