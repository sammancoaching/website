from fabric import Connection
import os
from deploy import read_credentials

def upload_directory(conn, local_dir, remote_dir):
    for root, dirs, files in os.walk(local_dir):
        relative_path = os.path.relpath(root, local_dir)
        remote_path = os.path.join(remote_dir, relative_path)
        conn.run(f'mkdir -p {remote_path}')

        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(remote_path, file)
            conn.put(local_file, remote_file)

def main():
    if os.path.exists("credentials.txt"):
        ftp_user, ftp_password, ftp_server = read_credentials("credentials.txt")
    else:
        ftp_user = os.getenv('FTP_USER')
        ftp_password = os.getenv('FTP_PASSWORD')
        ftp_server = os.getenv('FTP_SERVER')

    if not ftp_user or not ftp_password or not ftp_server:
        raise ValueError("FTP credentials are not set in the environment variables and/or no credentials.txt found")

    local_dir = '_site'
    remote_dir = 'web'

    # Connect to the remote server
    conn = Connection(
        host=ftp_server,
        user=ftp_user,
        connect_kwargs={"password": ftp_password}
    )

    # Upload the directory
    upload_directory(conn, local_dir, remote_dir)
    print(f'Successfully uploaded {local_dir} to {ftp_server}/{remote_dir}')

if __name__ == '__main__':
    main()
