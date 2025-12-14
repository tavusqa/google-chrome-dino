import json, os, shutil, sys

with open("skin.json", "r", encoding="utf-8") as f:
    skin = json.load(f).get("skin")

if not skin:
    print('skin.json must contain: { "skin": "name" }')
    sys.exit(1)

src = os.path.join("skins", skin)
dst = os.path.join("www", "assets")

layers = {
    "bg_sky.png": "bg_sky.png",
    "bg_far.png": "bg_far.png",
    "bg_mid.png": "bg_mid.png",
    "bg_near.png": "bg_near.png",
    "bg_front.png": "bg_front.png",
}

if not os.path.isdir(src):
    print(f"Skin folder not found: {src}")
    sys.exit(1)

os.makedirs(dst, exist_ok=True)

for name in layers:
    path = os.path.join(src, name)
    if not os.path.isfile(path):
        print(f"Missing {name} in skins/{skin}/")
        sys.exit(1)
    shutil.copy(path, os.path.join(dst, name))

print(f"Skin '{skin}' applied successfully")