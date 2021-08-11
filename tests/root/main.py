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


def read_PATH(paths):
    dirs = list()
    scripts = list()
    for path in paths:
        path = path[0].replace("/", root_dir) + path[1:]
        dirs.append(path)
        for dir in os.listdir(path):
            scripts.append(dir)
    return scripts


def main(username):
    while True:
        command = input(f"[{username}@{hostname} /]$ ")
        if command == "shutdown":
            exit("Shutting Down...")

        elif command.split()[0] in read_PATH(paths):
            os.system(f"python {bin_dir}{command}")

        else:
            print(f"Command not found: {command.split()[0]}")
