from subprocess import Popen, PIPE, STDOUT

from . import configuration
from .configuration import PlotmanConfig


class FarmPlot:
    """
    The final state to move files from tmp folder to given network hard drive devices
    """

    def __init__(self, cfg: PlotmanConfig):
        self.dsts = cfg.directories.dst
        self.checktmps = cfg.directories.tmp
        self.schedule = cfg.scheduling.polling_time_s
        self.log_file_path = configuration.get_log_path()

    def start_copyplot_spawn(self):
        for d in self.dsts:
            p = Popen(["plmo", self.checktmps, d, 50000000, self.log_file_path], stdout=PIPE, stderr=STDOUT)
            output, error = p.communicate()
            output = output.strip().decode("utf-8")
            print("start moving file from temp folder to network FS farm location {}".format(d))
            if p.returncode:
                print(f"E: {output}")
