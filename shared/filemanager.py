from pathlib import Path


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
                'last edited': str(stat.st_mtime),
            }

    def list_files(self):
        text = 'stuff\n'  # TODO
        for k, v in self.register.items():
            # text += f'{k}:{v}'
            name = v['name'].ljust(40)
            size = v['size'].rjust(10)
            time = v['last edited'].rjust(10)

            text += f'{name} | {size} | {time}'
        return text
        # name | size | last edit

    def get_register(self):
        return self.register

    def remove_file(self, filename: str):
        pass

    def add_file(self, fileobj):
        pass

    def get_file(self, filename: str):
        pass


if __name__ == '__main__':
    files = FileManager('client/files')
    print(files.list_files())
