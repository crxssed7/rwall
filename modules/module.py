import os
import subprocess

from abc import ABC, abstractmethod

class Module(ABC):
    def __init__(self, script_dir) -> None:
        super().__init__()
        self.script_dir = script_dir

    @abstractmethod
    def run(self):
        pass

    def _try_run_command(self, command):
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print(f"ERROR: An error occurred when running {command}. See above output.")

    def _get_wal_colours(self):
        wal_colours = os.path.expanduser("~/.cache/wal/colors")
        return self._read_file_contents(wal_colours).splitlines()

    def _read_file_contents(self, file):
        contents = ""
        with open(file, "r", encoding="utf-8") as f:
            contents = f.read()
        return contents
