#!/usr/bin/env python3
import os
from os.path import isdir, isfile, join, relpath, normpath, dirname, basename
from os.path import realpath
import sys
import argparse
import zipfile
from shutil import rmtree, copy2, copytree

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Arduino conf dir (usually /home/username/.arduino15)")
args = parser.parse_args()

ARDUINO_DIR = realpath(args.directory)
SOURCE_DIR = dirname(realpath(__file__))

if not isdir(ARDUINO_DIR):
    print(ARDUINO_DIR, ": no such directory")
    quit()

hardware_dir = join(ARDUINO_DIR, "packages", "arduino", "hardware")
tools_dir = join(ARDUINO_DIR, "packages", "arduino", "tools")

if not isdir(hardware_dir) or not isdir(tools_dir):
    print(ARDUINO_DIR, ": incorrect directory content")
    quit()


# Delete old files
sam = join(hardware_dir, "sam")
rmtree(sam, ignore_errors=True)
arm_gcc = join(tools_dir, "arm-none-eabi-gcc")
rmtree(arm_gcc, ignore_errors=True)
bossac = join(tools_dir, "bossac")
rmtree(bossac, ignore_errors=True)

# Copy new files
arduino_core = join(sam, "1.6.11")
CORE_DIRS = [
    "cores",
    "firmwares",
    "libraries",
    "system",
    "variants",
]
CORE_FILES = [
    "boards.txt",
    "platform.txt",
    "programmers.txt",
]

for core_dir in CORE_DIRS:
    copytree(join(SOURCE_DIR, core_dir), join(arduino_core, core_dir))
for core_file in CORE_FILES:
    copy2(join(SOURCE_DIR, core_file), arduino_core)

tools = zipfile.ZipFile("tools.zip")
tools.extractall(tools_dir)

print("Done")
