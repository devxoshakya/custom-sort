import shutil
import os
import pathlib

def custom_sort(extension):
    arr = next(os.walk('.'))[2]
    isExist = os.path.exists(f"custom-sort({extension})/")
    if isExist == False:
        os.makedirs(f"custom-sort({extension})")
    for file in arr:
        if pathlib.Path(file).suffix == extension:
            shutil.move(file, f"custom-sort({extension})")

extension = input("Enter file extension :")


if __name__ == '__main__':
    custom_sort(extension)
