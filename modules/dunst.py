import os
import re
import subprocess

from .module import Module

class Dunst(Module):
    def run(self):
        colours = self._get_wal_colours()
        dunstrc = os.path.expanduser("~/.config/dunst/dunstrc")
        if not os.path.isfile(dunstrc):
            print("ERROR: Dunstrc not found.")
            return
        dunstrc_contents = self._read_file_contents(dunstrc)
        new_contents = re.sub(r'background\s*=\s*"#([A-Fa-f0-9]{6})"', f"background = \"{colours[0]}\"", dunstrc_contents)
        new_contents = re.sub(r'foreground\s*=\s*"#([A-Fa-f0-9]{6})"', f"foreground = \"{colours[7]}\"", new_contents)
        with open(dunstrc, "w", encoding="utf-8") as f:
            f.write(new_contents)
        subprocess.run(["pkill", "-HUP", "dunst"], check=False)
