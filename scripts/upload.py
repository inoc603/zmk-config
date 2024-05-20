import os
import time
import shutil

left_uploaded = False
right_uploaded = False


def try_upload(vol: str, file: str):
    if not os.path.exists(f"{vol}/CURRENT.UF2"):
        return False
    print(f"Uploading {file} to {vol}...")
    shutil.copy(file, vol)
    print(f"Uploaded {file} to {vol}")
    return True

print("Watching glove80 volumes")

while not left_uploaded or not right_uploaded:
    time.sleep(1)
    right_uploaded = right_uploaded or try_upload(
        "/Volumes/GLV80RHBOOT", "build/glove80_rh.uf2"
    )
    left_uploaded = left_uploaded or try_upload(
        "/Volumes/GLV80LHBOOT", "build/glove80_lh.uf2"
    )
