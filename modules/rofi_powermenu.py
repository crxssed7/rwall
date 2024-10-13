from .module import Module

class RofiPowermenu(Module):
    def run(self):
        self._try_run_command([f"{self.script_dir}/powermenu"])
