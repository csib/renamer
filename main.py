import os
import re


def rename_path(root, path):
    newfilepath = renamer_regex(path)
    os.rename(os.path.join(root, path), os.path.join(root, newfilepath))


def renamer_regex(name):
    return re.sub('[^\wa-zA-ZöüóőúéáűÜÓŐÚÉÁŰ. ]', '', name)


def walkfilesystem(dirroot):
    # Main Walk Through File System
    mappa = 0
    fajl = 0
    for root, dirs, files in os.walk(dirroot, topdown=False):

        for name in dirs:
            print('From Folder: ' + root + name)
            print('To __Folder: ' + root + renamer_regex(name))
            searchObj = renamer_regex(name)
            if searchObj:
                try:
                    rename_path(root, name)
                    mappa += 1
                except Exception as e:
                    print(e)

        for name in files:
            print('From File: ' + root + name)
            print('To __file: ' + root + renamer_regex(name))
            searchObj = renamer_regex(name)
            if searchObj:
                try:
                    rename_path(root, name)
                    fajl += 1
                except Exception as e:
                    print(e)
    print('Folders renamed: {}'.format(mappa))
    print('Files renamed: {}'.format(fajl))


if __name__ == "__main__":
    walkfilesystem('C:\\files')
    # walkfilesystem('/volume1/Public/')
