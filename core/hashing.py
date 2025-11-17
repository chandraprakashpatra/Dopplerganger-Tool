import os
import hashlib
from collections import defaultdict

def compute_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def hash_folder(folder):
    result = defaultdict(list)
    for root, _, files in os.walk(folder):
        for f in files:
            p = os.path.join(root, f)
            try:
                h = compute_hash(p)
                result[h].append(p)
            except:
                pass
    return dict(result)
