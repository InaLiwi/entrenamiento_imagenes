# scripts/convertir_bdd100k.py
import json
from pathlib import Path
from PIL import Image

MAPA = {"pedestrian": 0, "rider": 0, "bicycle": 1, "car": 2, "motorcycle": 3,
        "bus": 5, "train": 6, "truck": 7, "traffic light": 9}

def convertir(json_path, imgs_dir, out_labels):
    out_labels.mkdir(parents=True, exist_ok=True)
    for item in json.loads(Path(json_path).read_text()):
        img = Path(imgs_dir) / item["name"]
        if not img.exists():
            continue
        W, H = 1280, 720
        lineas = []
        for obj in item.get("labels", []):
            if "box2d" not in obj or obj["category"] not in MAPA:
                continue
            b = obj["box2d"]
            x = (b["x1"] + b["x2"]) / 2 / W
            y = (b["y1"] + b["y2"]) / 2 / H
            w = (b["x2"] - b["x1"]) / W
            h = (b["y2"] - b["y1"]) / H
            lineas.append(f"{MAPA[obj['category']]} {x:.6f} {y:.6f} {w:.6f} {h:.6f}")
        (out_labels / f"{img.stem}.txt").write_text("\n".join(lineas))