from .module import Module

class Pywalfox(Module):
    def run(self):
        self._try_run_command(["pywalfox", "update"])
