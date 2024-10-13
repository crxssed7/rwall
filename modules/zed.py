import os
import shutil

from .module import Module

class Zed(Module):
    def run(self):
        self._try_run_command([f"{self.script_dir}/zed-theme-wal/generate_theme"])
        self._force_refresh_zed()

    def _force_refresh_zed(self):
        source = f"{self.script_dir}/zed-theme-wal/themes/wal-theme.json"
        destination = os.path.expanduser("~/.config/zed/themes/wal-theme.json")
        shutil.copy(source, destination)
