from paramiko import SSHClient
import paramiko
from classes.scp.scp import SCPClient, SCPException

import sys


class GetScpConnexion:
    def __init__(self, INFO_CONNEXION_SCP):
        self.username = INFO_CONNEXION_SCP["login"]
        self.hostname = INFO_CONNEXION_SCP["host"]
        self.ssh = self.connect_ssh()
        self.scp = SCPClient(self.ssh.get_transport(), progress4=self.progress4)

    def connect_ssh(self):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(username=self.username, hostname=self.hostname)
        return ssh

    # Define progress callback that prints the current percentage completed for the file
    def progress(self, filename, size, sent):
        sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent) / float(size) * 100))

    def progress4(self, filename, size, sent, peername):
        sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (
        peername[0], peername[1], filename, float(sent) / float(size) * 100))

#    scp = SCPClient(ssh.get_transport(), progress4=progress4)

    # SCPCLient takes a paramiko transport and progress callback as its arguments.
    def get_file_scp(self, remote_path, local_path = None):
        try:
            if local_path is None:
                self.scp.get(remote_path=remote_path)
            else:
                self.scp.get(remote_path=remote_path, local_path=local_path)
            return 0
        except SCPException:
            print("erreur dans le téléchargement {} vers {}".format(remote_path, local_path ))
            self.scp.close()
            self.scp = SCPClient(self.ssh.get_transport(), progress4=self.progress4)
            return 1
        

    def get_list_repertoire(self, path_repository):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        stdin, stdout, stderr = self.ssh.exec_command('ls -lRh --time-style=long-iso {}'.format(path_repository))
        return stdout.read().splitlines()
        # for line in stdout.read().splitlines():
        #     print(line)
