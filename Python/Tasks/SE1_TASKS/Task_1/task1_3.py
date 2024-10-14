#!/usr/bin/python3

import os

get_var = input("Enter the env var: ")

print((os.getenv(get_var)))