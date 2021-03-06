#!/bin/python3
from getpass import getuser as user
import os


def move_files(source_folder, target_folder):
    try:
        for path, directory, files in os.walk(source_folder):
            for file in files:
                if not os.path.isfile(target_folder + file):
                    os.rename(
                        os.path.join(
                            path, file),
                        os.path.join(
                            target_folder, file)
                    )
        else:
            print('All files moved')
    except Exception as error:
        print(error)


move_files(f'/home/{user()}/Downloads/ISO/',
           f'/home/{user()}/Documents/')
