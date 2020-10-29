from pathlib import Path

from shared.utils import format_time


class FileManager(object):
    # register file to track state of the files we have.
    # is it necessary?
    # could just generate it from (list_files())
    # hmmm

    def __init__(self, path):
        self.folder = Path(path)
        self.register = {}
        for file in self.folder.iterdir():
            stat = file.stat()
            self.register[file.name] = {
                'name': file.name,
                'size': str(stat.st_size),
                'last edited': format_time(stat.st_mtime),
            }

    def list_files(self):
        text = (
            '\n' + '-'*80 + '\n' +
            'filename'.ljust(40) +
            ' | ' + 'size'.rjust(10) +
            ' | ' + 'last edited'.rjust(10) +
            '\n'
        )
        for k, v in self.register.items():
            # text += f'{k}:{v}'
            name = v['name'].ljust(40)
            size = v['size'].rjust(10)
            time = v['last edited'].rjust(10)

            text += f'{name} | {size} | {time}\n'
        return text
        # name | size | last edit

    def get_register(self):
        return self.register

    def remove_file(self, filename: str):
        pass

    def add_file(self, fileobj):
        pass

    def get_file(self, filename: str):
        """Return the fileobject as a bytes object if found, otherwise None"""
        file = Path(self.folder, filename)
        if file.exists():
            with file.open(mode='rb') as f:
                data = f.read()
            return data
        return None

    def write_file(self, filename, data):
        """Write a local file."""
        file = Path(self.folder, filename)
        with file.open(mode='wb') as f:
            f.write(data)


if __name__ == '__main__':
    files = FileManager('client/files')
    print(files.list_files())
