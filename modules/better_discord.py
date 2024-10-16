import os
from .module import Module

# Discord wal theme taken from https://github.com/Gremious/discord-wal-theme-template/blob/main/discord-pywal.css
class BetterDiscord(Module):
    def run(self):
        colours = list(map(self._convert_hex_to_rgb, self._get_wal_colours()))
        background = self._convert_rgb_to_decimal(colours[0])
        foreground = colours[15]
        cursor = colours[15]
        css = self._read_file_contents(f"{self.script_dir}/discord-pywal.css")
        css = css.replace("{foreground.rgb}", f"{foreground[0]}, {foreground[1]}, {foreground[2]}")
        css = css.replace("{cursor.rgb}", f"{cursor[0]}, {cursor[1]}, {cursor[2]}")
        css = css.replace("{background.red}", f"{background[0]}")
        css = css.replace("{background.green}", f"{background[1]}")
        css = css.replace("{background.blue}", f"{background[2]}")
        for i in range(len(colours)):
            colour = colours[i]
            css = css.replace("{color" + str(i) + ".rgb}", f"{colour[0]}, {colour[1]}, {colour[2]}")
        self._write_css(css)

    def _convert_hex_to_rgb(self, hex):
        hex = str(hex).replace("#", "")
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    def _write_css(self, css):
        theme_file = os.path.expanduser("~/.config/BetterDiscord/themes/discord-pywal.theme.css")
        with open(theme_file, "w", encoding="utf-8") as f:
            f.write(css)

    def _convert_rgb_to_decimal(self, colour):
        r = colour[0] / 255
        g = colour[1] / 255
        b = colour[2] / 255
        return [r, g, b]
