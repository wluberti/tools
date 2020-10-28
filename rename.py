#! /usr/bin/env python3

import os
from pathlib import Path

if __name__ == "__main__":
    dirpath = "."
    extention = ".mp4"

    paths = sorted(Path(dirpath).glob(f"*{extention}"), key=os.path.getctime)

    for count, filename in enumerate(paths):
        count += 1
        oldName = str(filename).split('-0_')[0]
        newName = (f"{count:03d}: {oldName}{extention}")

        os.rename(filename, newName)

