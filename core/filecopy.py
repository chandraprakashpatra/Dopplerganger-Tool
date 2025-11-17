import os
import shutil

def copy_grouped_images(groups, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    gid = 0
    for h, files in groups.items():
        for src in files:
            base = os.path.basename(src)
            dst = os.path.join(out_dir, f"{gid}_{base}")
            try:
                shutil.copy2(src, dst)
            except:
                pass
        gid += 1


def copy_cross(groups, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    gid = 0
    for h, d in groups.items():
        for src in d["A"]:
            base = os.path.basename(src)
            dst = os.path.join(out_dir, f"{gid}_A_{base}")
            shutil.copy2(src, dst)

        for src in d["B"]:
            base = os.path.basename(src)
            dst = os.path.join(out_dir, f"{gid}_B_{base}")
            shutil.copy2(src, dst)

        gid += 1
