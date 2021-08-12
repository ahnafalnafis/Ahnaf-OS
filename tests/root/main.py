import os
from functions import read
from dotenv import load_dotenv


load_dotenv("etc/environment")
paths = os.getenv("ENV").split(";")

logged_in = False
hostname = read("etc/hostname")
load_dotenv("etc/fstab")
root_dir = os.getenv("root_dir")
bin_dir = root_dir+"bin/"
binaries = os.listdir(bin_dir)


def main(username):
    while True:
        found = False
        command = input(f"[{username}@{hostname} /]$ ")
        scripts = list()
        for path in paths:
            path = path[0].replace("/", root_dir) + path[1:]
            for dir in path.split():
                for item in os.listdir(dir):
                    scripts.append(item)

                if command == "shutdown":
                    exit("Shutting Down...")

                elif command.split()[0] in scripts:
                    os.system(f"python {path}/{command}")
                    found = True

        else:
            if not found:
                print(f"Command not found: {command.split()[0]}")
