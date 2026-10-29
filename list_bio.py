import os
for root, dirs, files in os.walk("."):
    for f in files:
        path = os.path.join(root, f)
        if f.lower().endswith((".txt",".md",".json")) or "bio" in f.lower() or "readme" in f.lower():
            print(path)
