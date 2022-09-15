#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser("Git User Switcher")
parser.add_argument("--user", help="Switch to $user", type=str, required=True)
args = parser.parse_args()
if (args.user == "tea"):
    os.system("git config --global user.name #")
    os.system("git config --global user.email ###")
elif (args.user == "github"):
    os.system("git config --global user.name #")
    os.system("git config --global user.email ###")
elif (args.user == "current"):
    None # just skip output to show current git user
print("Git user is now:")
os.system("git config --global user.name")
os.system("git config --global user.email")