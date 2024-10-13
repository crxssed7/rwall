from .module import Module

class Bspwm(Module):
    def run(self):
        colours = self._get_wal_colours()
        self._try_run_command(["bspc", "config", "normal_border_color", colours[1]])
        self._try_run_command(["bspc", "config", "active_border_color", colours[2]])
        self._try_run_command(["bspc", "config", "focused_border_color", colours[15]])
        self._try_run_command(["bspc", "config", "presel_feedback_color", colours[1]])
