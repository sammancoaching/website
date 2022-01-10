#!/usr/bin/env python3

from ftplib import FTP_TLS, error_perm
import os 

def read_credentials(filename):
    with open(filename) as f:
        text = f.read()

    lines = text.splitlines()
    for line in lines:
        if line.startswith("user:"):
            user = line.split(": ")[1]
        if line.startswith("password:"):
            password = line.split(": ")[1]
        if line.startswith("server:"):
            server = line.split(": ")[1]
    return user, password, server


def placeFiles(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            try:
                print("STOR", name, localpath)
                ftp.storbinary('STOR ' + name, open(localpath,'rb'))
            except TimeoutError as e:
                print("timeout when storing file ", name)
        elif os.path.isdir(localpath):
            
            try:
                ftp.mkd(name)
                print("MKD", name)

            # ignore "directory already exists"
            except error_perm as e:
                if not e.args[0].startswith('550'): 
                    raise

            print("CWD", name)
            ftp.cwd(name)
            placeFiles(ftp, localpath)           
            print("CWD", "..")
            ftp.cwd("..")

def main():

    user, password, server = read_credentials("credentials.txt")
    print("found credentials", user, password, server)

    with FTP_TLS(host=server, user=user, passwd=password) as ftp:
        ftp.cwd("web")
        local_web = "_site"
        placeFiles(ftp, local_web)


if __name__ == "__main__":
    main()