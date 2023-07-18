import os
from ftplib import FTP
def upload_file(ftp, local_path, remote_path):
    with open(local_path, 'rb') as file:
        ftp.storbinary('STOR ' + remote_path, file)
ftp_host = ''
ftp_user = ''
ftp_password = ''
local_directory = ''
remote_directory = ''
ftp = FTP(ftp_host)
ftp.login(user=ftp_user, passwd=ftp_password)
ftp.cwd(remote_directory)
for root, dirs, files in os.walk(local_directory):
    for file in files:
        local_path = os.path.join(root, file)
        remote_path = os.path.join(remote_directory, os.path.relpath(local_path, local_directory))
        upload_file(ftp, local_path, remote_path)
ftp.quit()