
import time
import subprocess
import os
from utils.system import decorate_exception


class SerialDownloader(object):

    def __init__(self):
        self.pre_bin_path = r""
        self.root_path = os.getcwd()
        self.script_path = os.path.join(self.root_path, "Utility")
        self.log_file = None
        self.log_path = None

    def gen_cmd_line(self, com_port, fw_path, oakgate, pre_bin_path):
        command_line = "cd /d {} && python two_step_download.py --oakgate={} --firmwarePath={} --preBinPath={} --serialPort={}"\
            .format(self.script_path, oakgate, fw_path, pre_bin_path, com_port)
        return command_line

    def execute_command(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            ret = process.poll()
            if ret is None:
                buff = process.stdout.readline()
                self.record_log(buff)
                time.sleep(1)
            else:
                break
        self.record_log(process.stderr.readline())
        return ret


    @decorate_exception
    def record_log(self, buffer):
        out_put = buffer.decode('utf-8', 'ignore') if type(buffer) is bytes else str(buffer)
        print(out_put)
        self.log_file.write(out_put)

    def save_log(self):
        log_file = "{}_{}.log".format("Serial_download", time.time())
        self.log_path = os.path.join(self.root_path, "Logs", log_file)
        self.log_file = open(self.log_path, "w")

    def close_log(self):
        if self.log_file is not None:
            self.log_file.close()

    def get_bin_path(self, fw_path, vol, commit):
        if os.path.isfile(fw_path):
            bin_path = fw_path
        else:
            bin_path = self.get_fw_path(fw_path, vol, commit)
        return bin_path

    def get_fw_path(self, fw_path, vol, commit):
        for file_name in os.listdir(fw_path):
            if os.path.isfile(os.path.join(fw_path, file_name)):
                if "_{}_".format(vol) in file_name and commit in file_name and file_name.endswith(".bin"):
                    return os.path.join(fw_path, file_name)
        return None

    def run(self, parameters):
        com_port = parameters["com"]
        fw_path = parameters["fw_path"]
        oakgate = parameters["ogt"]
        pre_bin_path = parameters["pre_bin"]
        vol = parameters["vol"]
        commit = parameters["commit"]
        self.save_log()
        bin_path = self.get_bin_path(fw_path, vol, commit)
        if bin_path is not None:
            command_line = self.gen_cmd_line(com_port, bin_path, oakgate, pre_bin_path)
            print(command_line)
            ret = self.execute_command(command_line)
        else:
            ret = 1
            self.record_log("Did not find fw bin at: {}".format(fw_path))
        self.close_log()
        return ret, self.log_file
