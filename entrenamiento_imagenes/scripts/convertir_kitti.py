# scripts/convertir_kitti.py
from pathlib import Path
from PIL import Image

MAPA = {"Car": 2, "Van": 2, "Truck": 7, "Tram": 6,
        "Pedestrian": 0, "Person_sitting": 0, "Cyclist": 0}

def convertir(labels_dir, imgs_dir, out_labels):
    out_labels.mkdir(parents=True, exist_ok=True)
    for txt in Path(labels_dir).glob("*.txt"):
        img = Path(imgs_dir) / f"{txt.stem}.png"
        if not img.exists():
            continue
        W, H = Image.open(img).size
        lineas = []
        for fila in txt.read_text().splitlines():
            p = fila.split()
            if p[0] not in MAPA:
                continue
            x1, y1, x2, y2 = map(float, p[4:8])
            x = (x1 + x2) / 2 / W
            y = (y1 + y2) / 2 / H
            w = (x2 - x1) / W
            h = (y2 - y1) / H
            lineas.append(f"{MAPA[p[0]]} {x:.6f} {y:.6f} {w:.6f} {h:.6f}")
        (out_labels / f"{txt.stem}.txt").write_text("\n".join(lineas))