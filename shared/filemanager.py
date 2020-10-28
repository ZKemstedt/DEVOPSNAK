import typing as t
from pathlib import Path

# folder = Path('client/files')
# text = 'name | size | last_modified\n'
# for file in folder.iterdir():
#     stat = file.stat()
#     line = f'{file.name} | {stat.st_size} | {stat.st_mtime}\n'
#     text += line
# print(text)


class FileManager(object):
    # register file to track state of the files we have.
    # is it necessary?
    # could just generate it from (list_files())
    # hmmm

    def __init__(self):
        # self.path
        # self.reg_no
        # self.reg
        pass

    def save_register(self):
        pass

    def load_register(self):
        pass

    def get_register(self):
        # register last edited at...
        # dict
        # > filename: last edited
        # ?> added/deleted compare
        pass

    def update_register(self, changed: t.Dict):
        pass

    def list_files(self):
        pass
        # name | size | last edit

    def remove_file(self, filename: str):
        pass

    def add_file(self, fileobj):
        pass

    def get_file(self, filename: str):
        pass
