def duplicates_inside(folder_map):
    return {h: v for h, v in folder_map.items() if len(v) > 1}

def duplicates_across(map_a, map_b):
    keys = set(map_a.keys()) & set(map_b.keys())
    out = {}
    for h in keys:
        out[h] = {"A": map_a[h], "B": map_b[h]}
    return out
