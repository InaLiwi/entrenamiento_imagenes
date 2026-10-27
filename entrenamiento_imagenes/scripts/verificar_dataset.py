"""Revisa que cada imagen tenga su etiqueta y que las clases sean válidas."""
from pathlib import Path
import yaml

RAIZ = Path(__file__).resolve().parent.parent
cfg = yaml.safe_load((RAIZ / "data.yaml").read_text(encoding="utf-8"))
n_clases = len(cfg["names"])

problemas = 0
for split in ("train", "val", "test"):
    imgs = RAIZ / cfg["path"] / split / "images"
    labs = RAIZ / cfg["path"] / split / "labels"
    if not imgs.exists():
        print(f"[{split}] no existe {imgs}")
        continue
    archivos = [p for p in imgs.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
    print(f"[{split}] {len(archivos)} imágenes")
    for img in archivos:
        lab = labs / f"{img.stem}.txt"
        if not lab.exists():
            print(f"  sin etiqueta: {img.name}")
            problemas += 1
            continue
        for linea in lab.read_text().splitlines():
            if not linea.strip():
                continue
            clase = int(linea.split()[0])
            if clase >= n_clases:
                print(f"  clase inválida {clase} en {lab.name}")
                problemas += 1

print("OK" if problemas == 0 else f"Problemas encontrados: {problemas}")
