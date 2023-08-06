
import time
import subprocess
import os


class SerialDownloader(object):

    def __init__(self):
        self.pre_bin_path = r""
        self.root_path = os.getcwd()
        self.script_path = os.path.join(self.root_path, "Utility")

    def gen_cmd_line(self, com_port, fw_path, oakgate, pre_bin_path):
        command_line = "cd /d {} && python two_step_download.py --oakgate={} --firmwarePath={} --preBinPath={} --serialPort={}"\
            .format(self.script_path, oakgate, fw_path, pre_bin_path, com_port)
        return command_line

    def execute_command(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (std_output, std_error) = process.communicate()
        ret = process.poll()
        out_put = std_output.decode('utf-8','ignore') if type(std_output) is bytes else std_output
        error = std_error.decode('utf-8','ignore') if type(std_error) is bytes else std_error
        output = "{} \n {}".format(out_put, error)
        return output, ret

    def save_log(self, std_output):
        print(std_output)
        log_file = "{}_{}.log".format("Serial_download", time.time())
        log_path = os.path.join(self.root_path, "Logs", log_file)
        with open(log_path, "w") as file_:
            file_.write(std_output)
        return log_path

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
        print("Serail download", parameters)
        bin_path = self.get_bin_path(fw_path, vol, commit)
        if bin_path is not None:
            command_line = self.gen_cmd_line(com_port, bin_path, oakgate, pre_bin_path)
            print(command_line)
            std_output, ret = self.execute_command(command_line)
        else:
            ret = 1
            std_output = "Did not find fw bin at: {}".format(fw_path)
        log = self.save_log(std_output)
        return ret, log
