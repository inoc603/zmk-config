import os
import time
import shutil

left_uploaded = False
right_uploaded = False


def try_upload(vol: str, file: str):
    if os.path.exists(vol):
        return False
    shutil.copy(file, vol)
    print(f"Uploaded {file} to {vol}")
    return True


while not left_uploaded or not right_uploaded:
    time.sleep(1)
    left_uploaded = left_uploaded or try_upload(
        "/Volumes/GLV80LHBOOT", "build/glove80_lh.uf2"
    )
    right_uploaded = right_uploaded or try_upload(
        "/Volumes/GLV80RHBOOT", "build/glove80_rh.uf2"
    )
