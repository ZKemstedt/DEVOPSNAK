import os
import logging

from pathlib import Path

from shared.utils import format_time

log = logging.getLogger(__name__)


class FileManager(object):

    def __init__(self, path):
        self.folder = Path(path)
        self.register = {}
        self.remote = None
        self.todo = []
        for file in self.folder.iterdir():
            stat = file.stat()
            self.register[file.name] = {
                'name': file.name,
                'size': str(stat.st_size),
                'last edited': stat.st_mtime,
            }

    def list_files(self):
        # header
        headline = "-"*80
        name = 'filename'.ljust(40)
        size = 'size'.rjust(10)
        time = 'last edited'.rjust(10)

        text = f'\n{headline}\n{name} | {size} | {time}\n'

        # items
        for k, v in self.register.items():
            name = v['name'].ljust(40)
            size = v['size'].rjust(10)
            time = format_time(v['last edited']).rjust(10)

            text += f'{name} | {size} | {time}\n'
        return text

    def get_register(self):
        return self.register

    def remove_file(self, filename: str):
        file = Path(self.folder, filename)
        if file.exists():
            try:
                os.remove(file)
                del self.register[filename]
                return None
            except Exception as e:
                log.error(f'failed to remove file `{filename}`', exc_info=e)
        return f'failed to remove file `{filename}`'

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

# --- sync ---

    # clientside !
    def compare_registers(self):
        log.trace('comparing registers')
        if self.remote is None:
            log.debug('no remote')
            return
        self.todo = []
        for key, value in self.remote.items():
            if key not in self.register:
                self.todo.append(key)
            else:
                time1 = value['last edited']
                time2 = self.register[key]['last edited']
                if not check_timediff(time1, time2):
                    self.todo.append(key)


def check_timediff(time1, time2):
    """Return True if time1 is the same as time2"""
    log.trace(f't1: {time1}, t2 :{time2}')
    if abs(time1 - time2) > 10:
        return True
    return False


if __name__ == '__main__':
    files = FileManager('client/files')
    print(files.list_files())
