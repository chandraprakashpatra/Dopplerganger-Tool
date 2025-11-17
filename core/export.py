import os
import pandas as pd

def export_groups_to_csv(groups, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    gid = 0
    for h, files in groups.items():
        for f in files:
            rows.append({
                "group_id": gid,
                "hash": h,
                "path": f,
                "filename": os.path.basename(f)
            })
        gid += 1

    csv_path = os.path.join(out_dir, "duplicates_single.csv")
    pd.DataFrame(rows).to_csv(csv_path, index=False)
    return csv_path


def export_cross_to_csv(groups, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rows = []
    gid = 0
    for h, d in groups.items():
        for f in d["A"]:
            rows.append({
                "group_id": gid,
                "hash": h,
                "folder": "A",
                "path": f,
                "filename": os.path.basename(f)
            })
        for f in d["B"]:
            rows.append({
                "group_id": gid,
                "hash": h,
                "folder": "B",
                "path": f,
                "filename": os.path.basename(f)
            })
        gid += 1

    csv_path = os.path.join(out_dir, "duplicates_cross.csv")
    pd.DataFrame(rows).to_csv(csv_path, index=False)
    return csv_path
