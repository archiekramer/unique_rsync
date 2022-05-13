from paramiko import SSHClient
import paramiko
from scp.scp import SCPClient
from paramiko import SSHClient
import sys

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(username="archiekramer", hostname="udun.ddns.net")

# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# SCPCLient takes a paramiko transport and progress callback as its arguments.
scp = SCPClient(ssh.get_transport(), progress=progress)

# you can also use progress4, which adds a 4th parameter to track IP and port
# useful with multiple threads to track source
# def progress4(filename, size, sent, peername):
#     sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
# scp = SCPClient(ssh.get_transport(), progress4=progress4)

scp.get('/home/archiekramer/Mediacentre/Divers/VSD_-_Avril_2022.pdf')
#scp.get('/home/archiekramer/Mediacentre/Divers/The.Batman.2022.MULTi.VF2.1080p.WEBRip.H265_10b-SC1LL4.mkv')
#
# Should now be printing the current progress of your put function.

scp.close()
